from typing import assert_type

from maya_brew.command_wrapper import createNode
from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_types import Joint, Transform


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
