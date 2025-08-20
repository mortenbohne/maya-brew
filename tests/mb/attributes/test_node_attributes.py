from mb.attributes.node_attribute import Attribute, FloatAttribute, MessageAttribute
import maya.cmds as cmds
import pytest


def test_cast_attributes(empty_transform):
    tx = Attribute(f"{empty_transform.node_path}.translateX")
    assert isinstance(tx, FloatAttribute)
    message = Attribute(f"{empty_transform}.message")
    assert isinstance(message, MessageAttribute)


def test_message_attribute_get_value_error(empty_transform):
    with pytest.raises(AttributeError):
        Attribute._get_value(empty_transform, "message")


def test_attribute_get_value(empty_transform):
    tx = Attribute(f"{empty_transform.node_path}.translateX")
    value = tx.get()
    assert value == 0
    cmds.setAttr(f"{empty_transform.node_path}.translateX", 5)
    value = FloatAttribute._get_value(empty_transform, "translateX")
    assert value == 5


def test_factory_with_mplug(translateX_plug):
    a = Attribute(translateX_plug)
    assert isinstance(a, FloatAttribute)
    assert a.get() == 0


def test_subclass_with_mplug(translateX_plug):
    fa = FloatAttribute(translateX_plug)
    assert fa.get() == 0


def test_invalid_path_missing_dot():
    with pytest.raises(ValueError):
        Attribute("bad_path_without_dot")


def test_invalid_plug_type():
    with pytest.raises(ValueError):
        Attribute(123)  # type: ignore
