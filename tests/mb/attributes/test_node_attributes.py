from mb.attributes.node_attribute import Attribute
import maya.cmds as cmds


def test_attribute_get_value(empty_transform):
    value = Attribute._get_value(empty_transform, "translateX")
    assert value == 0
    cmds.setAttr(f"{empty_transform.node_path}.translateX", 5)
    value = Attribute._get_value(empty_transform, "translateX")
    assert value == 5
