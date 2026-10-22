import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.exceptions import NodeException
from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import (
    PolyCone,
    PolyCube,
    PolyCylinder,
    PolyHelix,
    PolyPipe,
    PolyPlane,
    PolyPlatonicSolid,
    PolyPrism,
    PolyPyramid,
    PolySphere,
    PolyTorus,
    Transform,
)


@pytest.fixture(
    params=[
        pytest.param((cmds.polyPlane, PolyPlane, "width"), id="polyPlane"),
        pytest.param(
            (cmds.polyPlatonicSolid, PolyPlatonicSolid, "radius"),
            id="polyPlatonicSolid",
        ),
        pytest.param((cmds.polyPrism, PolyPrism, "sideLength"), id="polyPrism"),
        pytest.param((cmds.polyCone, PolyCone, "radius"), id="polyCone"),
        pytest.param((cmds.polyCylinder, PolyCylinder, "radius"), id="polyCylinder"),
        pytest.param((cmds.polyHelix, PolyHelix, "radius"), id="polyHelix"),
        pytest.param((cmds.polyPipe, PolyPipe, "radius"), id="polyPipe"),
        pytest.param((cmds.polySphere, PolySphere, "radius"), id="polySphere"),
        pytest.param((cmds.polyTorus, PolyTorus, "radius"), id="polyTorus"),
        pytest.param((cmds.polyCube, PolyCube, "width"), id="polyCube"),
        pytest.param((cmds.polyPyramid, PolyPyramid, "sideLength"), id="polyPyramid"),
    ]
)
def primitive(request):
    return request.param


@pytest.fixture(
    params=[
        ({}, (Transform, "history")),
        ({"constructionHistory": False}, (Transform,)),
        ({"ch": False}, (Transform,)),
        ({"object": False}, ("history",)),
        ({"o": False, "ch": False}, ("history",)),
    ]
)
def created_primitive(request, primitive):
    command, history_type, _ = primitive
    flags, wrappers = request.param
    expected = tuple(history_type if item == "history" else item for item in wrappers)
    return command(name="wrapped_primitive", **flags), expected


def test_creation_returns_wrapped_tuple(created_primitive):
    nodes, expected = created_primitive
    assert isinstance(nodes, tuple)
    assert tuple(type(node) for node in nodes) == expected
    if isinstance(nodes[0], Transform):
        assert maya_cmds.ls(str(nodes[0]), shortNames=True) == ["wrapped_primitive"]


@pytest.fixture
def primitive_nodes(primitive):
    command, _, _ = primitive
    return command()


@pytest.fixture(params=list(NodeState))
def primitive_state(request, primitive_nodes):
    node = primitive_nodes[1]
    maya_cmds.setAttr(f"{node}.nodeState", int(request.param))
    return node, request.param


@pytest.mark.parametrize(
    "query, state",
    [("query", "nodeState"), ("query", "nds"), ("q", "nodeState"), ("q", "nds")],
)
def test_node_state_query(primitive, primitive_state, query, state):
    command, _, _ = primitive
    node, expected = primitive_state
    assert command(node, **{query: True, state: True}) is expected


@pytest.fixture(params=["nodeState", "nds"])
def primitive_created_with_state(request, primitive):
    command, _, _ = primitive
    return command(**{request.param: NodeState.HAS_NO_EFFECT})[1]


def test_creation_accepts_node_state(primitive, primitive_created_with_state):
    command, _, _ = primitive
    assert (
        command(primitive_created_with_state, q=True, nds=True)
        is NodeState.HAS_NO_EFFECT
    )


@pytest.mark.parametrize("edit, state", [("edit", "nodeState"), ("e", "nds")])
def test_node_state_edit(primitive, primitive_nodes, edit, state):
    command, _, _ = primitive
    assert (
        command(primitive_nodes[1], **{edit: True, state: NodeState.BLOCKING})
        == "Values edited."
    )
    assert command(primitive_nodes[1], q=True, nds=True) is NodeState.BLOCKING


@pytest.fixture(params=["axis", "ax"])
def oriented_primitive(request, primitive):
    command, _, _ = primitive
    return command(**{request.param: (1.0, 0.0, 0.0)})


@pytest.mark.parametrize("target", [0, 1])
@pytest.mark.parametrize("query, axis", [("query", "axis"), ("q", "ax")])
def test_axis_query(primitive, oriented_primitive, target, query, axis):
    command, _, _ = primitive
    assert command(oriented_primitive[target], **{query: True, axis: True}) == [
        1.0,
        0.0,
        0.0,
    ]


@pytest.fixture
def primitive_without_history(primitive):
    command, _, _ = primitive
    return command(ch=False)[0]


def test_query_errors_are_chained(primitive, primitive_without_history):
    command, _, dimension = primitive
    with pytest.raises(NodeException, match=f"{command.__name__} failed") as caught:
        command(primitive_without_history, **{"q": True, dimension: True})
    assert isinstance(caught.value.__cause__, RuntimeError)
