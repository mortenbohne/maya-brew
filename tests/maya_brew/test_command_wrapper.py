import pytest
from maya_brew import cmds
from maya_brew.command_wrapper import createNode, polyPlane
from maya_brew.exceptions import AbstractNodeCreationError, NodeException
from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import (
    DagNode,
    Joint,
    MultiplyDivide,
    PolyPlane,
    Transform,
)


@pytest.fixture(
    params=[
        ("joint", Joint),
        ("multiplyDivide", MultiplyDivide),
    ]
)
def created_node(request):
    node_type, wrapper = request.param
    return createNode(node_type, name="wrapped_node", skipSelect=True), wrapper


def test_create_node_returns_native_wrapper(created_node):
    node, wrapper = created_node
    assert type(node) is wrapper
    assert cmds.nodeType(str(node)) == wrapper._maya_type
    assert cmds.ls(str(node), shortNames=True) == ["wrapped_node"]
    assert not cmds.ls(selection=True)


@pytest.fixture
def shared_node():
    original = cmds.createNode("transform", name="shared_node")
    return createNode("transform", n=original, shared=True)


def test_create_shared_node_preserves_none(shared_node):
    assert shared_node is None


@pytest.mark.parametrize("node_type", ["dagNode", DagNode])
def test_create_node_rejects_abstract_type(node_type):
    with pytest.raises(AbstractNodeCreationError):
        createNode(node_type)


@pytest.fixture(params=["parent", "p"])
def parented_node(request):
    parent = createNode("transform", name="wrapped_parent")
    child = createNode("transform", n="wrapped_child", **{request.param: parent})
    return parent, child


def test_create_node_accepts_brew_parent(parented_node):
    parent, child = parented_node
    assert str(child) == f"{parent}|wrapped_child"


def test_omitted_flags_are_not_forwarded(monkeypatch):
    from maya_brew.command_wrapper import extensions

    calls = []

    def record_call(node_type, **kwargs):
        calls.append((node_type, kwargs))

    monkeypatch.setattr(extensions, "createNode", record_call)
    createNode("transform", name="supplied", shared=False)
    assert calls == [("transform", {"name": "supplied", "shared": False})]


class CustomJoint(Joint):
    pass


@pytest.fixture(params=[Joint, CustomJoint])
def node_from_class(request):
    return createNode(request.param, name="class_joint"), request.param


def test_create_node_accepts_brew_class(node_from_class):
    node, wrapper = node_from_class
    assert type(node) is wrapper
    assert cmds.nodeType(str(node)) == "joint"


@pytest.fixture(
    params=[
        ({}, [Transform, PolyPlane]),
        ({"constructionHistory": False}, [Transform]),
        ({"ch": False}, [Transform]),
        ({"object": False}, [PolyPlane]),
        ({"o": False, "ch": False}, [PolyPlane]),
    ]
)
def created_plane(request):
    kwargs, node_types = request.param
    return polyPlane(name="wrapped_plane", **kwargs), node_types


def test_poly_plane_returns_native_wrappers(created_plane):
    nodes, node_types = created_plane
    assert isinstance(nodes, tuple)
    assert [type(node) for node in nodes] == node_types


@pytest.fixture
def plane_with_history():
    return polyPlane(name="query_plane")


@pytest.mark.parametrize(
    "target_index, flags, expected",
    [
        (0, {"query": True, "width": True}, 1.0),
        (1, {"query": True, "axis": True}, [0.0, 1.0, 0.0]),
        (1, {"q": True, "ax": True}, [0.0, 1.0, 0.0]),
    ],
)
def test_poly_plane_query_returns_maya_value(
    plane_with_history, flags, expected, target_index
):
    nodes = plane_with_history
    assert polyPlane(nodes[target_index], **flags) == expected


@pytest.fixture
def plane_without_history():
    return polyPlane(constructionHistory=False)[0]


def test_poly_plane_query_failure_is_chained(plane_without_history):
    with pytest.raises(NodeException) as caught:
        polyPlane(plane_without_history, query=True, width=True)
    assert isinstance(caught.value.__cause__, RuntimeError)


@pytest.fixture(params=[("query", "nodeState"), ("q", "nds")])
def plane_with_node_state(request):
    query_flag, state_flag = request.param
    nodes = polyPlane(**{state_flag: NodeState.HAS_NO_EFFECT})
    return nodes[1], query_flag, state_flag


def test_poly_plane_queries_node_state(plane_with_node_state):
    plane, query_flag, state_flag = plane_with_node_state
    state = polyPlane(plane, **{query_flag: True, state_flag: True})
    assert state is NodeState.HAS_NO_EFFECT


def test_poly_plane_edits_node_state(plane_with_history):
    _, plane = plane_with_history
    polyPlane(plane, edit=True, nodeState=NodeState.BLOCKING)
    assert polyPlane(plane, q=True, nds=True) is NodeState.BLOCKING


@pytest.mark.parametrize("edit_flag", ["edit", "e"])
def test_poly_plane_edit_returns_message(plane_with_history, edit_flag):
    _, plane = plane_with_history
    assert polyPlane(plane, **{edit_flag: True, "width": 5.0}) == "Values edited."
    assert polyPlane(plane, query=True, width=True) == 5.0


@pytest.fixture(params=list(NodeState))
def plane_in_each_state(request, plane_with_history):
    _, plane = plane_with_history
    cmds.setAttr(f"{plane}.nodeState", int(request.param))
    return plane, request.param


def test_poly_plane_queries_all_node_states(plane_in_each_state):
    plane, state = plane_in_each_state
    assert polyPlane(plane, query=True, nodeState=True) is state
