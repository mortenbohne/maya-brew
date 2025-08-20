from mb.attributes.node_attribute import Attribute, FloatAttribute
import maya.cmds as cmds


def test_cast_float_attribute(empty_transform):
    a = Attribute(f"{empty_transform.node_path}.translateX")
    assert isinstance(a, FloatAttribute)


def test_attribute_get_value(empty_transform):
    value = FloatAttribute._get_value(empty_transform, "translateX")
    assert value == 0
    cmds.setAttr(f"{empty_transform.node_path}.translateX", 5)
    value = FloatAttribute._get_value(empty_transform, "translateX")
    assert value == 5
