from typing import Any, Literal, assert_type

from maya_brew import cmds
from maya_brew.command_wrapper import (
    createNode,
    ls,
    polyCone,
    polyCube,
    polyPlane,
    polyPyramid,
    polySphere,
)
from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import (
    Joint,
    PolyCone,
    PolyCube,
    PolyPlane,
    PolyPyramid,
    PolySphere,
    Transform,
)


class CustomJoint(Joint):
    pass


def check_poly_cone_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyCone()
    assert_type(nodes, tuple[Transform, PolyCone])
    assert_type(polyCone(ch=False), tuple[Transform])
    assert_type(polyCone(constructionHistory=False), tuple[Transform])
    assert_type(polyCone(object=False), tuple[PolyCone])
    assert_type(polyCone(o=False, ch=False), tuple[PolyCone])
    assert_type(
        polyCone(constructionHistory=history, object=create_object),
        tuple[Transform, PolyCone] | tuple[Transform] | tuple[PolyCone],
    )
    assert_type(polyCone(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyCone(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyCone(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyCone(nodes[0], q=True, nds=True), NodeState)
    assert_type(polyCone(nodes[1], edit=True, radius=2.0), Literal["Values edited."])
    assert_type(
        polyCone(nodes[0], e=True, rcp=True, tx=False), Literal["Values edited."]
    )
    assert_type(polyCone(nodes[1], q=True, radius=True), Any)
    assert_type(
        polyCone(axis=(0.0, 1.0, 0.0), sx=10, sy=3, sz=2, roundCap=True),
        tuple[Transform, PolyCone],
    )


def check_poly_pyramid_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyPyramid()
    assert_type(nodes, tuple[Transform, PolyPyramid])
    assert_type(polyPyramid(ch=False), tuple[Transform])
    assert_type(polyPyramid(constructionHistory=False), tuple[Transform])
    assert_type(polyPyramid(object=False), tuple[PolyPyramid])
    assert_type(polyPyramid(o=False, ch=False), tuple[PolyPyramid])
    assert_type(
        polyPyramid(constructionHistory=history, object=create_object),
        tuple[Transform, PolyPyramid] | tuple[Transform] | tuple[PolyPyramid],
    )
    assert_type(polyPyramid(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyPyramid(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyPyramid(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyPyramid(nodes[0], q=True, nds=True), NodeState)
    assert_type(
        polyPyramid(nodes[1], edit=True, sideLength=2.0), Literal["Values edited."]
    )
    assert_type(polyPyramid(nodes[0], e=True, texture=False), Literal["Values edited."])
    assert_type(polyPyramid(nodes[1], q=True, sideLength=True), Any)
    assert_type(
        polyPyramid(axis=(0.0, 1.0, 0.0), ns=5, nsi=5, sc=2, sh=3, tx=False),
        tuple[Transform, PolyPyramid],
    )


def check_poly_cube_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyCube()
    assert_type(nodes, tuple[Transform, PolyCube])
    assert_type(polyCube(ch=False), tuple[Transform])
    assert_type(polyCube(constructionHistory=False), tuple[Transform])
    assert_type(polyCube(object=False), tuple[PolyCube])
    assert_type(polyCube(o=False, ch=False), tuple[PolyCube])
    assert_type(
        polyCube(constructionHistory=history, object=create_object),
        tuple[Transform, PolyCube] | tuple[Transform] | tuple[PolyCube],
    )
    assert_type(polyCube(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyCube(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyCube(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyCube(nodes[0], q=True, nds=True), NodeState)
    assert_type(polyCube(nodes[1], edit=True, width=2.0), Literal["Values edited."])
    assert_type(polyCube(nodes[0], e=True, d=3.0), Literal["Values edited."])
    assert_type(polyCube(nodes[1], q=True, width=True), Any)
    assert_type(polyCube(nodes[1], query=True, axis=True), Any)
    assert_type(
        polyCube(axis=(0.0, 1.0, 0.0), sx=10, sy=15, sz=5),
        tuple[Transform, PolyCube],
    )


def check_poly_sphere_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polySphere()
    assert_type(nodes, tuple[Transform, PolySphere])
    assert_type(polySphere(ch=False), tuple[Transform])
    assert_type(polySphere(constructionHistory=False), tuple[Transform])
    assert_type(polySphere(object=False), tuple[PolySphere])
    assert_type(polySphere(o=False, ch=False), tuple[PolySphere])
    assert_type(
        polySphere(constructionHistory=history, object=create_object),
        tuple[Transform, PolySphere] | tuple[Transform] | tuple[PolySphere],
    )
    assert_type(polySphere(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polySphere(nodes[0], query=True, nds=True), NodeState)
    assert_type(polySphere(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polySphere(nodes[0], q=True, nds=True), NodeState)
    assert_type(polySphere(nodes[1], edit=True, radius=2.0), Literal["Values edited."])
    assert_type(
        polySphere(nodes[0], e=True, nds=NodeState.BLOCKING),
        Literal["Values edited."],
    )
    assert_type(polySphere(nodes[1], q=True, radius=True), Any)
    assert_type(polySphere(nodes[1], query=True, axis=True), Any)
    assert_type(
        polySphere(axis=(0.0, 1.0, 0.0), sx=10, sy=15), tuple[Transform, PolySphere]
    )


def check_ls_types(node: Node, nodes: list[Transform], mode: bool) -> None:
    assert_type(ls(), list[Node | str])
    assert_type(cmds.ls(node), list[Node | str])
    assert_type(ls([node, "pPlane*"]), list[Node | str])
    assert_type(ls(nodes), list[Node | str])
    assert_type(ls((node, "pPlane*"), type=["mesh", "transform"]), list[Node | str])
    assert_type(ls(typ=("mesh", "transform"), assemblies=True), list[Node | str])
    assert_type(ls(uuid=True), list[str])
    assert_type(ls(uid=True), list[str])
    assert_type(ls(nodeTypes=True), list[str])
    assert_type(ls(nt=True), list[str])
    assert_type(ls(objectsOnly=True), list[Node])
    assert_type(ls(o=True, selection=True), list[Node])
    assert_type(ls(o=True, uid=True), list[str])
    assert_type(ls(o=True, showType=True), list[Node | str])
    assert_type(ls(o=True, ufeObjects=True), list[Node | str])
    assert_type(ls(showNamespace=True), list[Node | str])
    assert_type(ls(uuid=mode), list[Node | str])
    assert_type(cmds.ls(type=Transform), list[Node | str])
    assert_type(ls(typ=[Transform, "joint"]), list[Node | str])
    assert_type(ls(exactType=Joint), list[Node | str])
    assert_type(ls(et=(Joint, Transform)), list[Node | str])
    assert_type(ls(excludeType=Transform), list[Node | str])
    assert_type(ls(ext=[Joint], objectsOnly=True), list[Node])


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
