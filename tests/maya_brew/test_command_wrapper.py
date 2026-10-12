import pytest

from maya_brew import cmds
from maya_brew.command_wrapper import createNode
from maya_brew.exceptions import AbstractNodeCreationError
from maya_brew.nodes.node_types import DagNode, Joint, MultiplyDivide


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
