import maya.cmds as cmds
import pytest
from maya_brew.exceptions import AbstractNodeCreationError
from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_types import DagNode, Joint, MultiplyDivide, Transform


class MyTransform(Transform):
    pass


@pytest.fixture
def transform():
    return cmds.createNode("transform", name="extension_transform")


def test_direct_constructors_do_not_dispatch(transform):
    assert type(Node(transform)) is Node
    assert type(MyTransform(transform)) is MyTransform


def test_abstract_creation_rejected():
    with pytest.raises(AbstractNodeCreationError):
        DagNode.create("invalid_abstract")
    with pytest.raises(AbstractNodeCreationError):
        Node.create("invalid_base")


@pytest.mark.parametrize("wrapper", [MultiplyDivide, Joint, MyTransform])
def test_create_uses_native_type(wrapper):
    node = wrapper.create("created")
    assert type(node) is wrapper
    assert cmds.nodeType(str(node)) == wrapper._maya_type
