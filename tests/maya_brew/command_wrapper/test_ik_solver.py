import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.command_wrapper import ikSolver
from maya_brew.exceptions import NodeCastingException, NodeException
from maya_brew.nodes.node_types import IkRPsolver, IkSCsolver, IkSplineSolver


@pytest.fixture(
    params=[
        ("ikSCsolver", IkSCsolver),
        ("ikRPsolver", IkRPsolver),
        ("ikSplineSolver", IkSplineSolver),
    ]
)
def solver_type(request):
    return request.param


@pytest.fixture(params=["long", "short"])
def solver(request, solver_type):
    name, wrapper = solver_type
    if request.param == "long":
        node = cmds.ikSolver(
            solverType=name, name="custom_solver", epsilon=0.5, maxIterations=25
        )
    else:
        node = ikSolver(st=name, n="custom_solver", ep=0.5, mxi=25)
    return node, wrapper


def test_ik_solver_creation_returns_native_wrapper(solver):
    node, wrapper = solver
    assert type(node) is wrapper
    assert maya_cmds.nodeType(str(node)) == wrapper._maya_type
    assert maya_cmds.ikSolver(str(node), q=True, n=True) == "custom_solver"
    assert maya_cmds.ikSolver(str(node), q=True, ep=True) == 0.5
    assert maya_cmds.ikSolver(str(node), q=True, mxi=True) == 25


@pytest.mark.parametrize("mode", ["query", "q"])
@pytest.mark.parametrize(
    "flag", ["epsilon", "ep", "maxIterations", "mxi", "name", "n", "solverType", "st"]
)
@pytest.mark.parametrize("target_kind", ["wrapped", "string", "list", "tuple"])
def test_ik_solver_queries_match_maya(solver, mode, flag, target_kind):
    node, _ = solver
    target = {"wrapped": node, "string": str(node), "list": [node], "tuple": (node,)}[
        target_kind
    ]
    flags = {mode: True, flag: True}
    assert cmds.ikSolver(target, **flags) == maya_cmds.ikSolver(str(node), **flags)


@pytest.mark.parametrize("mode", ["edit", "e"])
@pytest.mark.parametrize(
    "flag,value,query",
    [
        ("epsilon", 0.25, "ep"),
        ("ep", 0.25, "epsilon"),
        ("maxIterations", 50, "mxi"),
        ("mxi", 50, "maxIterations"),
    ],
)
def test_ik_solver_edits_match_maya(solver, mode, flag, value, query):
    node, _ = solver
    original = maya_cmds.ikSolver(str(node), q=True, **{query: True})
    flags = {mode: True, flag: value}
    expected = maya_cmds.ikSolver(str(node), **flags)
    maya_cmds.ikSolver(str(node), e=True, **{flag: original})
    assert cmds.ikSolver(node, **flags) == expected
    assert maya_cmds.ikSolver(str(node), q=True, **{query: True}) == value


@pytest.fixture
def solver_handle(solver):
    node, _ = solver
    root = cmds.joint()
    tip = cmds.joint(p=(0, 4, 0))
    return node, cmds.ikHandle(sj=root, ee=tip, solver=node)


def test_ik_solver_integrates_with_ik_handle(solver_handle):
    solver, nodes = solver_handle
    assert cmds.ikHandle(nodes[0], q=True, solver=True) == str(solver)


@pytest.mark.parametrize("flags", [{}, {"solverType": "invalid"}])
def test_ik_solver_runtime_errors_are_chained(flags):
    with pytest.raises(NodeException, match="ikSolver failed") as error:
        cmds.ikSolver(**flags)
    assert isinstance(error.value.__cause__, RuntimeError)



@pytest.fixture
def wrong_result_node():
    return cmds.createNode("transform")


def test_ik_solver_rejects_wrong_node_type(monkeypatch, wrong_result_node):
    monkeypatch.setattr(
        maya_cmds, "ikSolver", lambda *args, **kwargs: str(wrong_result_node)
    )
    with pytest.raises(NodeCastingException, match="Expected IkSolver"):
        cmds.ikSolver(st="ikSCsolver")
