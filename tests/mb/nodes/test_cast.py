import pytest
import mb
import mb.nodes.cast


def test_string_to_dag_path(test_cube, test_namespace, test_cube_short_name):
    cube_full_path = mb.cmds.ls(test_cube, long=True)[0]
    assert cube_full_path == f"|{test_namespace}:{test_cube_short_name}"
    dag_path = mb.nodes.cast.get_dag_path_from_string(cube_full_path)
    assert isinstance(dag_path, mb.OpenMaya2.MDagPath)


def test_invalid_string_to_dag_path(test_cube, test_cube_short_name):
    with pytest.raises(mb.nodes.cast.NonExistingDagPath):
        mb.nodes.cast.get_dag_path_from_string("invalid_name")
    with pytest.raises(mb.nodes.cast.NonExistingDagPath):
        mb.nodes.cast.get_dag_path_from_string(test_cube_short_name)
    with pytest.raises(mb.nodes.cast.InvalidDagPath):
        mb.nodes.cast.get_dag_path_from_string("lambert1")


def test_get_long_name_from_maya_string(
    test_cube, test_namespace, test_cube_short_name
    ):
    cube_full_name = f"{test_namespace}:{test_cube_short_name}"
    cube_full_path = mb.nodes.cast.get_long_name_from_maya_string(cube_full_name)
    assert cube_full_path == f"|{cube_full_name}"
    grouped_cube = mb.cmds.polyCube(name=test_cube_short_name)[0]
    group_name = "my_group"
    mb.cmds.group(name=group_name, empty=True)
    mb.cmds.parent(grouped_cube, group_name)
    grouped_cube_full_path = mb.nodes.cast.get_long_name_from_maya_string(grouped_cube)
    assert group_name in grouped_cube_full_path
    new_cube_with_same_short_name = mb.cmds.polyCube(name=test_cube_short_name)[0]
    # we can cast it from maya's return value
    new_cube_full_path = mb.nodes.cast.get_long_name_from_maya_string(
        new_cube_with_same_short_name
    )
    # if we try to cast it based on short name we should get two matches
    with pytest.raises(mb.nodes.cast.MultipleMatchingNodes):
        mb.nodes.cast.get_long_name_from_maya_string(test_cube_short_name)
    assert test_namespace not in new_cube_full_path
    with pytest.raises(mb.nodes.cast.NoMatchingNodes):
        mb.nodes.cast.get_long_name_from_maya_string("invalid_name")
