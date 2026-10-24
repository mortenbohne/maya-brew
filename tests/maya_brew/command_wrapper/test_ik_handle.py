import maya.cmds as maya_cmds
import pytest

from maya_brew import cmds
from maya_brew.command_wrapper import extensions, ikHandle
from maya_brew.exceptions import NodeCastingException, NodeException
from maya_brew.nodes.casting import cast
from maya_brew.nodes.node_types import IkEffector, IkHandle, Transform


@pytest.fixture
def joint_chain():
    root = cmds.joint(name="root")
    middle = cmds.joint(name="middle", p=(0, 4, 0))
    tip = cmds.joint(name="tip", p=(1, 8, 0))
    return root, middle, tip


@pytest.fixture(params=["long", "short"])
def created_handle(request, joint_chain):
    root, _, tip = joint_chain
    if request.param == "long":
        return cmds.ikHandle(startJoint=root, endEffector=tip, name="leg")
    return ikHandle(sj=str(root), ee=str(tip), n="leg")


def test_ik_handle_creation_returns_wrapped_tuple(created_handle):
    assert isinstance(created_handle, tuple)
    handle, effector = created_handle
    assert type(handle) is IkHandle
    assert type(effector) is IkEffector
    assert maya_cmds.ikHandle(str(handle), q=True, name=True) == "leg"
    assert maya_cmds.ikHandle(str(handle), q=True, ee=True) == "effector1"
    assert maya_cmds.ls(selection=True, long=True) == [str(handle)]


@pytest.fixture(params=["ikRPsolver", "ikSCsolver", "ikSplineSolver"])
def solver_handle(request, joint_chain):
    return (
        cmds.ikHandle(sj=joint_chain[0], ee=joint_chain[-1], solver=request.param),
        request.param,
    )


def test_ik_handle_solver_creation(solver_handle):
    nodes, solver = solver_handle
    assert type(nodes[0]) is IkHandle
    assert type(nodes[1]) is IkEffector
    assert maya_cmds.ikHandle(str(nodes[0]), q=True, sol=True) == solver
    if solver == "ikSplineSolver":
        assert len(nodes) == 3
        assert type(nodes[2]) is Transform
        assert (
            maya_cmds.nodeType(
                maya_cmds.listRelatives(str(nodes[2]), shapes=True, fullPath=True)[0]
            )
            == "nurbsCurve"
        )
    else:
        assert len(nodes) == 2


@pytest.fixture
def spline_without_curve(joint_chain):
    return cmds.ikHandle(
        sj=joint_chain[0], ee=joint_chain[-1], sol="ikSplineSolver", ccv=False
    )


def test_ik_handle_spline_without_curve_returns_pair(spline_without_curve):
    assert len(spline_without_curve) == 2
    assert type(spline_without_curve[0]) is IkHandle
    assert type(spline_without_curve[1]) is IkEffector


@pytest.fixture(params=["single", "pair", "arguments", "sequence"])
def selection_handle(request, joint_chain):
    root, _, tip = joint_chain
    if request.param == "single":
        maya_cmds.select(str(tip))
        return cmds.ikHandle()
    if request.param == "pair":
        maya_cmds.select(str(root), str(tip))
        return cmds.ikHandle()
    if request.param == "arguments":
        return cmds.ikHandle(root, tip)
    return cmds.ikHandle([root, str(tip)])


def test_ik_handle_preserves_selection_based_creation(selection_handle, joint_chain):
    handle = selection_handle[0]
    assert maya_cmds.ikHandle(str(handle), q=True, sj=True) == "root"
    assert maya_cmds.ikHandle(str(handle), q=True, jl=True) == ["root", "middle"]


@pytest.fixture(params=["curve", "c"])
def supplied_curve_handle(request, joint_chain):
    curve = cast(maya_cmds.curve(d=2, p=[(0, 0, 0), (0, 4, 0), (1, 8, 0)]))
    nodes = cmds.ikHandle(
        sj=joint_chain[0],
        ee=joint_chain[-1],
        sol="ikSplineSolver",
        ccv=False,
        pcv=False,
        fj=True,
        **{request.param: curve},
    )
    return nodes, curve


def test_ik_handle_accepts_and_returns_supplied_curve(supplied_curve_handle):
    nodes, curve = supplied_curve_handle
    assert len(nodes) == 3
    assert str(nodes[2]) == str(curve)
    queried = cmds.ikHandle(nodes[0], q=True, c=True)
    assert isinstance(queried, str)
    assert maya_cmds.ls(queried, long=True) == maya_cmds.listRelatives(
        str(curve), shapes=True, fullPath=True
    )


@pytest.fixture(params=["solver", "sol"])
def wrapped_solver_handle(request, joint_chain):
    solver = cmds.createNode("ikRPsolver", name="custom_solver")
    return (
        cmds.ikHandle(sj=joint_chain[0], ee=joint_chain[-1], **{request.param: solver}),
        solver,
    )


def test_ik_handle_accepts_wrapped_solver(wrapped_solver_handle):
    nodes, solver = wrapped_solver_handle
    assert maya_cmds.ikHandle(str(nodes[0]), q=True, sol=True) == str(solver)


@pytest.fixture
def reused_effector_handle(joint_chain):
    effector = cmds.createNode("ikEffector", parent=joint_chain[1])
    maya_cmds.xform(str(effector), worldSpace=True, translation=(1, 8, 0))
    return cmds.ikHandle(sj=joint_chain[0], ee=effector), effector


def test_ik_handle_accepts_wrapped_effector(reused_effector_handle):
    nodes, original_effector = reused_effector_handle
    assert len(nodes) == 1
    queried = cmds.ikHandle(nodes[0], q=True, ee=True)
    assert maya_cmds.ls(queried, long=True) == [str(original_effector)]


@pytest.mark.parametrize("mode", ["query", "q"])
@pytest.mark.parametrize(
    "flag",
    [
        "startJoint",
        "sj",
        "endEffector",
        "ee",
        "jointList",
        "jl",
        "solver",
        "sol",
        "name",
        "n",
        "priority",
        "p",
        "weight",
        "w",
        "positionWeight",
        "pw",
        "forceSolver",
        "fs",
        "sticky",
        "s",
        "snapHandleFlagToggle",
        "shf",
        "rootOnCurve",
        "roc",
        "rootTwistMode",
        "rtm",
        "twistType",
        "tws",
        "curve",
        "c",
    ],
)
def test_ik_handle_queries_match_maya(created_handle, mode, flag):
    handle = created_handle[0]
    flags = {mode: True, flag: True}
    assert cmds.ikHandle(handle, **flags) == maya_cmds.ikHandle(str(handle), **flags)


@pytest.mark.parametrize("mode", ["edit", "e"])
@pytest.mark.parametrize(
    "flag,value,query",
    [
        ("priority", 3, "p"),
        ("p", 3, "priority"),
        ("weight", 0.5, "w"),
        ("w", 0.5, "weight"),
        ("positionWeight", 0.25, "pw"),
        ("pw", 0.25, "positionWeight"),
        ("sticky", "sticky", "s"),
        ("s", "sticky", "sticky"),
    ],
)
def test_ik_handle_edits_wrapped_targets(created_handle, mode, flag, value, query):
    handle = created_handle[0]
    assert cmds.ikHandle([handle], **{mode: True, flag: value}) is None
    assert maya_cmds.ikHandle(str(handle), q=True, **{query: True}) == value


@pytest.mark.parametrize(
    "disable,enable", [("disableHandles", "enableHandles"), ("dh", "eh")]
)
def test_ik_handle_enable_disable_and_snap(created_handle, disable, enable):
    handle = created_handle[0]
    assert cmds.ikHandle(handle, e=True, **{disable: True}) is None
    assert maya_cmds.getAttr(f"{handle}.ikBlend") == 0
    assert cmds.ikHandle(handle, e=True, **{enable: True}) is None
    assert maya_cmds.getAttr(f"{handle}.ikBlend") == 1
    assert cmds.ikHandle(handle, e=True, snapHandleToEffector=True) is None
    assert cmds.ikHandle(handle, e=True, autoPriority=True) is None


@pytest.fixture
def two_handles(joint_chain):
    first = cmds.ikHandle(sj=joint_chain[0], ee=joint_chain[-1])[0]
    maya_cmds.select(clear=True)
    root = cmds.joint(p=(5, 0, 0))
    tip = cmds.joint(p=(5, 4, 0))
    second = cmds.ikHandle(sj=root, ee=tip)[0]
    return first, second


def test_ik_handle_edits_multiple_wrapped_targets(two_handles):
    assert cmds.ikHandle([two_handles[0], str(two_handles[1])], e=True, dh=True) is None
    for handle in two_handles:
        assert maya_cmds.getAttr(f"{handle}.ikBlend") == 0
    assert cmds.ikHandle(*two_handles, e=True, eh=True) is None
    for handle in two_handles:
        assert maya_cmds.getAttr(f"{handle}.ikBlend") == 1


@pytest.mark.parametrize("flag", ["exists", "ex"])
@pytest.mark.parametrize("mode", [{}, {"q": True}, {"e": True}])
@pytest.mark.parametrize("value", ["leg", "missing_handle", True, False, ""])
def test_ik_handle_existence_matches_maya(created_handle, flag, mode, value):
    flags = {**mode, flag: value}
    handle = created_handle[0]
    if mode.get("q") and isinstance(value, str):
        with pytest.raises(TypeError):
            maya_cmds.ikHandle(str(handle), **flags)
        with pytest.raises(TypeError):
            cmds.ikHandle(handle, **flags)
        return
    assert cmds.ikHandle(handle, **flags) == maya_cmds.ikHandle(str(handle), **flags)


def test_ik_handle_runtime_errors_are_chained(joint_chain):
    with pytest.raises(NodeException, match="ikHandle failed") as error:
        cmds.ikHandle(sj=joint_chain[0], ee=joint_chain[-1], solver="invalid")
    assert isinstance(error.value.__cause__, RuntimeError)


def test_ik_handle_omitted_flags_are_not_forwarded(monkeypatch):
    calls = []

    def record_call(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(extensions, "ikHandle", record_call)
    ikHandle(name="supplied", createCurve=False, query=False)
    assert calls == [((), {"name": "supplied", "createCurve": False, "query": False})]


@pytest.mark.parametrize("result", [None, [], ["a", "b", "c", "d"], [1, 2], "h"])
def test_ik_handle_rejects_unexpected_creation_results(monkeypatch, result):
    monkeypatch.setattr(maya_cmds, "ikHandle", lambda *args, **kwargs: result)
    with pytest.raises(NodeException, match="Unexpected result from ikHandle"):
        cmds.ikHandle()


def test_ik_handle_rejects_wrong_creation_node_type(monkeypatch, joint_chain):
    monkeypatch.setattr(
        maya_cmds, "ikHandle", lambda *args, **kwargs: [str(joint_chain[0])]
    )
    with pytest.raises(NodeCastingException, match="Expected IkHandle"):
        cmds.ikHandle()
