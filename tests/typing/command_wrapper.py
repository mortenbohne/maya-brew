from typing import Any, Literal, assert_type

from maya_brew.command_wrapper import createNode, polyPlane
from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import Joint, PolyPlane, Transform


class CustomJoint(Joint):
    pass


def check_create_node_types(node_type: str, shared: bool) -> None:
    transform = createNode(Transform)
    assert_type(transform, Transform)
    assert_type(createNode("joint"), Node | None)
    assert_type(createNode(Joint, shared=False), Joint)
    assert_type(createNode(Joint, s=False), Joint)
    assert_type(createNode(Joint, shared=True), Joint | None)
    assert_type(createNode(Joint, s=True), Joint | None)
    assert_type(createNode(Joint, shared=shared), Joint | None)
    assert_type(createNode(Joint, s=shared), Joint | None)
    assert_type(createNode(Joint, shared=False, s=True), Joint | None)
    assert_type(createNode(node_type), Node | None)
    assert_type(createNode(node_type, shared=shared), Node | None)
    assert_type(createNode(Joint, parent=transform, skipSelect=True), Joint)
    assert_type(createNode(Joint, p=transform, n="child", ss=True), Joint)
    assert_type(createNode(Joint), Joint)
    assert_type(createNode(CustomJoint), CustomJoint)
    assert_type(createNode(node_type=Joint, shared=shared), Joint | None)
    if transform is not None:
        assert_type(transform.rename("renamed"), str)
        node: Node = transform
        assert_type(node, Node)


def check_generic_node_is_rejected() -> None:
    createNode(Node)  # type: ignore[type-var]


def check_poly_plane_types(history: bool, create_object: bool) -> None:
    nodes = polyPlane()
    assert_type(nodes, tuple[Transform, PolyPlane])
    assert_type(nodes[0], Transform)
    assert_type(nodes[1], PolyPlane)
    assert_type(polyPlane(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyPlane(nodes[0], q=True, nds=True), NodeState)
    assert_type(
        polyPlane(nodes[1], edit=True, nodeState=NodeState.BLOCKING),
        Literal["Values edited."],
    )
    assert_type(polyPlane(nodes[0], e=True, width=2.0), Literal["Values edited."])
    assert_type(polyPlane(constructionHistory=False), tuple[Transform])
    assert_type(polyPlane(ch=False), tuple[Transform])
    assert_type(polyPlane(object=False), tuple[PolyPlane])
    assert_type(polyPlane(o=False, ch=False), tuple[PolyPlane])
    assert_type(
        polyPlane(constructionHistory=history, object=create_object),
        tuple[Transform, PolyPlane] | tuple[Transform] | tuple[PolyPlane],
    )
    assert_type(polyPlane(query=True, width=True), Any)
    assert_type(polyPlane("pPlane1", query=True, axis=True), Any)
    assert_type(polyPlane("pPlane1", q=True, ax=True), Any)
    assert_type(polyPlane(axis=(0.0, 1.0, 0.0)), tuple[Transform, PolyPlane])
    assert_type(
        polyPlane("pPlane1", edit=True, axis=(0.0, 0.0, 1.0)),
        Literal["Values edited."],
    )
    query: bool = True
    assert_type(polyPlane(q=query, w=True), Any)
    assert_type(polyPlane(nodeState=NodeState.NORMAL), tuple[Transform, PolyPlane])
    assert_type(polyPlane(nds=NodeState.HAS_NO_EFFECT), tuple[Transform, PolyPlane])
    assert_type(polyPlane("polyPlane1", query=True, nodeState=True), NodeState)
    assert_type(polyPlane("polyPlane1", query=True, nds=True), NodeState)
    assert_type(polyPlane("polyPlane1", q=True, nodeState=True), NodeState)
    assert_type(polyPlane("polyPlane1", q=True, nds=True), NodeState)
    assert_type(
        polyPlane("polyPlane1", e=True, nds=NodeState.BLOCKING),
        Literal["Values edited."],
    )
    assert_type(polyPlane(nodes[1], edit=True, query=query, width=True), Any)
