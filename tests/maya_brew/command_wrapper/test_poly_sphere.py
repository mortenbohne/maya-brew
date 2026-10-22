import maya.cmds as maya_cmds
import pytest

from maya_brew import cmds
from maya_brew.exceptions import NodeException
from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import PolySphere, Transform


@pytest.fixture(
    params=[
        ({}, (Transform, PolySphere)),
        ({"constructionHistory": False}, (Transform,)),
        ({"ch": False}, (Transform,)),
        ({"object": False}, (PolySphere,)),
        ({"o": False, "ch": False}, (PolySphere,)),
    ]
)
def created_sphere(request):
    flags, wrappers = request.param
    return cmds.polySphere(name="wrapped_sphere", **flags), wrappers


def test_poly_sphere_returns_wrapped_tuple(created_sphere):
    nodes, wrappers = created_sphere
    assert isinstance(nodes, tuple)
    assert tuple(type(node) for node in nodes) == wrappers
    if isinstance(nodes[0], Transform):
        assert maya_cmds.ls(str(nodes[0]), shortNames=True) == ["wrapped_sphere"]


@pytest.fixture
def sphere():
    return cmds.polySphere(radius=2.0, subdivisionsX=10, subdivisionsY=15)


@pytest.mark.parametrize(
    "flags",
    [
        {"query": True, "radius": True},
        {"q": True, "r": True},
        {"q": True, "sx": True},
        {"query": True, "subdivisionsY": True},
        {"query": True, "axis": True},
        {"q": True, "ax": True},
    ],
)
@pytest.mark.parametrize("target", [0, 1])
def test_poly_sphere_queries_match_maya(sphere, flags, target):
    assert cmds.polySphere(sphere[target], **flags) == maya_cmds.polySphere(
        str(sphere[target]), **flags
    )


@pytest.mark.parametrize("edit, radius", [("edit", "radius"), ("e", "r")])
def test_poly_sphere_edits_wrapped_target(sphere, edit, radius):
    result = cmds.polySphere(sphere[1], **{edit: True, radius: 3.0})
    assert result == "Values edited."
    assert cmds.polySphere(sphere[1], q=True, radius=True) == 3.0


@pytest.fixture(params=list(NodeState))
def sphere_state(request, sphere):
    maya_cmds.setAttr(f"{sphere[1]}.nodeState", int(request.param))
    return sphere[1], request.param


@pytest.mark.parametrize(
    "query, state",
    [("query", "nodeState"), ("query", "nds"), ("q", "nodeState"), ("q", "nds")],
)
def test_poly_sphere_queries_node_state(sphere_state, query, state):
    node, expected = sphere_state
    assert cmds.polySphere(node, **{query: True, state: True}) is expected


def test_poly_sphere_edits_node_state(sphere):
    cmds.polySphere(sphere[1], e=True, nds=NodeState.BLOCKING)
    assert cmds.polySphere(sphere[1], q=True, nds=True) is NodeState.BLOCKING


@pytest.fixture
def sphere_without_history():
    return cmds.polySphere(ch=False)[0]


def test_poly_sphere_chains_query_errors(sphere_without_history):
    with pytest.raises(NodeException, match="polySphere failed") as caught:
        cmds.polySphere(sphere_without_history, q=True, radius=True)
    assert isinstance(caught.value.__cause__, RuntimeError)


@pytest.fixture
def oriented_sphere():
    return cmds.polySphere(axis=(1.0, 0.0, 0.0))


def test_poly_sphere_accepts_axis_vector(oriented_sphere):
    assert cmds.polySphere(oriented_sphere[1], q=True, axis=True) == [1.0, 0.0, 0.0]
