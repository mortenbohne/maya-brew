import maya.cmds as cmds
import maya_brew
import maya_brew.nodes.casting
import pytest
from maya_brew.exceptions import NodeCastingException, NodeException
from maya_brew.nodes.casting import cast
from maya_brew.nodes.node_types import (
    DagNode,
    Joint,
    Mesh,
    MultiplyDivide,
    Transform,
    Unknown,
)


def test_string_to_dag_path(test_cube, test_namespace, test_cube_short_name):
    cube_full_path = cmds.ls(test_cube, long=True)[0]
    assert cube_full_path == f"|{test_namespace}:{test_cube_short_name}"
    dag_path = maya_brew.nodes.casting.get_dag_path_from_string(cube_full_path)
    assert isinstance(dag_path, maya_brew.OpenMaya2.MDagPath)


def test_invalid_string_to_dag_path(test_cube, test_cube_short_name):
    with pytest.raises(maya_brew.nodes.casting.NonExistingDagPath):
        maya_brew.nodes.casting.get_dag_path_from_string("invalid_name")
    with pytest.raises(maya_brew.nodes.casting.NonExistingDagPath):
        maya_brew.nodes.casting.get_dag_path_from_string(test_cube_short_name)
    with pytest.raises(maya_brew.nodes.casting.InvalidDagPath):
        maya_brew.nodes.casting.get_dag_path_from_string("lambert1")


def test_get_long_name_from_maya_string(
    test_cube, test_namespace, test_cube_short_name
):
    cube_full_name = f"{test_namespace}:{test_cube_short_name}"
    cube_full_path = maya_brew.nodes.casting.get_long_name_from_maya_string(
        cube_full_name
    )
    assert cube_full_path == f"|{cube_full_name}"
    grouped_cube = cmds.polyCube(name=test_cube_short_name)[0]
    group_name = "my_group"
    cmds.group(name=group_name, empty=True)
    cmds.parent(grouped_cube, group_name)
    grouped_cube_full_path = maya_brew.nodes.casting.get_long_name_from_maya_string(
        grouped_cube
    )
    assert group_name in grouped_cube_full_path
    new_cube_with_same_short_name = cmds.polyCube(name=test_cube_short_name)[0]
    # we can cast it from maya's return value
    new_cube_full_path = maya_brew.nodes.casting.get_long_name_from_maya_string(
        new_cube_with_same_short_name
    )
    # if we try to cast it based on short name we should get two matches
    with pytest.raises(maya_brew.nodes.casting.MultipleMatchingNodes):
        maya_brew.nodes.casting.get_long_name_from_maya_string(test_cube_short_name)
    assert test_namespace not in new_cube_full_path
    with pytest.raises(maya_brew.nodes.casting.NoMatchingNodes):
        maya_brew.nodes.casting.get_long_name_from_maya_string("invalid_name")


@pytest.fixture
def native_nodes():
    transform, _ = cmds.polyCube(name="cast_cube")
    shape = cmds.listRelatives(transform, shapes=True, fullPath=True)[0]
    joint = cmds.createNode("joint", name="cast_joint")
    utility = cmds.createNode("multiplyDivide", name="cast_utility")
    return {
        "transform": transform,
        "mesh": shape,
        "joint": joint,
        "multiply_divide": utility,
    }


def test_cast_returns_exact_native_class(native_nodes):
    assert type(cast(native_nodes["transform"])) is Transform
    assert type(cast(native_nodes["mesh"])) is Mesh
    assert type(cast(native_nodes["joint"])) is Joint
    assert type(cast(native_nodes["multiply_divide"])) is MultiplyDivide


@pytest.fixture
def unknown_node():
    return cmds.createNode("unknown", name="cast_unknown")


def test_cast_unknown_node(unknown_node):
    wrapped = cast(unknown_node)
    assert type(wrapped) is Unknown
    assert str(wrapped) == unknown_node


def test_cast_expected_type_preserves_actual_subclass(native_nodes):
    assert type(cast(native_nodes["joint"], Transform)) is Joint
    assert type(cast(native_nodes["mesh"], DagNode)) is Mesh


def test_cast_expected_type_mismatch_raises(native_nodes):
    with pytest.raises(
        NodeCastingException, match="Expected Transform.*MultiplyDivide"
    ):
        cast(native_nodes["multiply_divide"], Transform)


@pytest.mark.parametrize("value", ["", "node.tx", "node.vtx[0]", None, 123])
def test_cast_rejects_non_node_inputs(value):
    with pytest.raises(NodeException):
        cast(value)
