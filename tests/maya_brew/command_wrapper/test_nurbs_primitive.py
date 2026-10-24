from dataclasses import dataclass

import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.exceptions import NodeException
from maya_brew.nodes import node_types
from maya_brew.nodes.node_state import NodeState


@dataclass(frozen=True)
class PrimitiveCase:
    command: str
    history_class_name: str
    flag: str
    value: float


CASES = (
    PrimitiveCase("circle", "MakeNurbCircle", "radius", 2.5),
    PrimitiveCase("cone", "MakeNurbCone", "radius", 3.5),
    PrimitiveCase("cylinder", "MakeNurbCylinder", "radius", 4.5),
    PrimitiveCase("sphere", "MakeNurbSphere", "radius", 5.5),
    PrimitiveCase("torus", "MakeNurbTorus", "radius", 6.5),
    PrimitiveCase("nurbsPlane", "MakeNurbPlane", "width", 7.5),
    PrimitiveCase("nurbsCube", "MakeNurbCube", "width", 8.5),
    PrimitiveCase("nurbsSquare", "MakeNurbsSquare", "sideLength1", 9.5),
)


@pytest.fixture(params=[pytest.param(case, id=case.command) for case in CASES])
def primitive(request):
    return request.param


@pytest.fixture
def primitive_nodes(primitive):
    return getattr(cmds, primitive.command)()


def test_creation_returns_wrapped_tuple(primitive, primitive_nodes):
    history_class = getattr(node_types, primitive.history_class_name)
    assert isinstance(primitive_nodes, tuple)
    assert isinstance(primitive_nodes[0], node_types.Transform)
    assert isinstance(primitive_nodes[1], history_class)


@pytest.mark.parametrize(
    "flags, expected",
    [
        ({}, (node_types.Transform, "history")),
        ({"constructionHistory": False}, (node_types.Transform,)),
        ({"ch": False}, (node_types.Transform,)),
        ({"object": False}, ("history",)),
        ({"o": False, "ch": False}, ("history",)),
    ],
)
def test_creation_flag_variants(primitive, flags, expected):
    command = getattr(cmds, primitive.command)
    history_class = getattr(node_types, primitive.history_class_name)
    nodes = command(**flags)
    expected_types = tuple(
        history_class if item == "history" else item for item in expected
    )
    assert tuple(type(node) for node in nodes) == expected_types


@pytest.mark.parametrize("query", ["query", "q"])
def test_queries_match_maya(primitive, primitive_nodes, query):
    command = getattr(cmds, primitive.command)
    native = getattr(maya_cmds, primitive.command)
    options = {query: True, primitive.flag: True}
    assert command(primitive_nodes[1], **options) == native(
        str(primitive_nodes[1]), **options
    )


@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize("query", ["query", "q"])
def test_edits_wrapped_target(primitive, primitive_nodes, edit, query):
    command = getattr(cmds, primitive.command)
    assert (
        command(primitive_nodes[1], **{edit: True, primitive.flag: primitive.value})
        == "Values edited."
    )
    assert (
        command(primitive_nodes[1], **{query: True, primitive.flag: True})
        == primitive.value
    )


@pytest.mark.parametrize(
    "query, state",
    [
        ("query", "nodeState"),
        ("query", "nds"),
        ("q", "nodeState"),
        ("q", "nds"),
    ],
)
def test_node_state_query(primitive, primitive_nodes, query, state):
    command = getattr(cmds, primitive.command)
    node = primitive_nodes[1]
    command(node, e=True, nds=NodeState.BLOCKING)
    assert command(node, **{query: True, state: True}) is NodeState.BLOCKING


def test_query_errors_are_chained(primitive):
    command = getattr(cmds, primitive.command)
    target = command(ch=False)[0]
    with pytest.raises(NodeException, match=f"{primitive.command} failed") as caught:
        command(target, q=True, **{primitive.flag: True})
    assert isinstance(caught.value.__cause__, RuntimeError)
