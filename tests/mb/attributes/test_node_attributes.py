from mb.attributes.node_attribute import Attribute, FloatAttribute, MessageAttribute
import maya.cmds as cmds
import pytest
from mb.nodes.node_types import DagNode, Node
from mb import OpenMaya2


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


def test_factory_with_mplug(translatex_plug):
    a = Attribute(translatex_plug)
    assert isinstance(a, FloatAttribute)
    assert a.get() == 0


def test_subclass_with_mplug(translatex_plug):
    fa = FloatAttribute(translatex_plug)
    assert fa.get() == 0


def test_invalid_path_missing_dot():
    with pytest.raises(ValueError):
        Attribute("bad_path_without_dot")


def test_invalid_plug_type():
    with pytest.raises(ValueError):
        Attribute(123)  # type: ignore


def test_get_node_from_plug_dag_and_non_dag(translatex_plug, non_dag_plug):
    dag = Attribute._get_node_from_plug(translatex_plug)
    assert isinstance(dag, DagNode)
    expected_dag_path = OpenMaya2.MFnDagNode(translatex_plug.node()).fullPathName()
    assert str(dag) == expected_dag_path

    non_dag = Attribute._get_node_from_plug(non_dag_plug)
    assert isinstance(non_dag, Node)
    assert not isinstance(non_dag, DagNode)
    expected_non_dag_name = OpenMaya2.MFnDependencyNode(non_dag_plug.node()).name()
    non_dag_name = str(non_dag)
    assert non_dag_name == expected_non_dag_name
