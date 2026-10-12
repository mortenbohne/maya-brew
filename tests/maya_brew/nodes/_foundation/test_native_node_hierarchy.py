import pytest
from maya_brew import cmds
from maya_brew.exceptions import NodeTypeInheritanceError
from maya_brew.nodes import _generated
from maya_brew.nodes._foundation import native_node_hierarchy as hierarchy


def test_abstract_node_uses_single_type_chain():
    assert hierarchy.query_node_type("node") == ("node",)


def test_discovery_preserves_native_metadata():
    nodes = hierarchy.discover_node_types()
    assert "dagNode (abstract)" not in nodes
    assert nodes["dagNode"].abstract
    assert not nodes["transform"].abstract
    assert nodes["dagNode"].name == "dagNode"
    assert nodes["node"].parent is None
    assert nodes["transform"].parent == "dagNode"
    assert nodes["joint"].parent == "transform"
    assert nodes["mesh"].parent == "surfaceShape"


def test_discovery_excludes_plugin_types(plugin_type):
    nodes = hierarchy.discover_node_types()
    assert plugin_type not in nodes
    plugin_nodes = hierarchy.discover_node_types(include_plugins=True)
    assert plugin_type in plugin_nodes
    for ancestor in hierarchy.query_node_type(plugin_type)[:-1]:
        assert ancestor in plugin_nodes


def test_unknown_type_query_is_typed_and_chained():
    with pytest.raises(NodeTypeInheritanceError) as caught:
        hierarchy.query_node_type("nonexistentBrewNodeType")
    assert isinstance(caught.value.__cause__, RuntimeError)


@pytest.mark.parametrize(
    ("maya_name", "class_name"),
    [
        ("transform", "Transform"),
        ("THdependNode", "THdependNode"),
        ("my-node", "MyNode"),
        ("2DTexture", "Node2DTexture"),
    ],
)
def test_python_class_names(maya_name, class_name):
    assert hierarchy.python_class_name(maya_name) == class_name


def test_generated_classes_match_maya_inheritance():
    version = cmds.about(majorVersion=True)
    constants = pytest.importorskip(f"{_generated.__name__}.maya_{version}.constants")
    classes = constants.TYPE_CLASSES
    observed = hierarchy.discover_node_types()
    assert observed.keys() == classes.keys()
    for name, wrapper in classes.items():
        assert hierarchy.python_class_name(name) == wrapper.__name__
        chain = tuple(
            base.__dict__["_maya_type"]
            for base in reversed(wrapper.__mro__)
            if base.__dict__.get("_maya_type") is not None
        )
        assert chain == observed[name].inheritance
        assert wrapper._maya_type == name
        assert wrapper._abstract == observed[name].abstract
