import pytest
import mb
import mb.nodes.cast


def test_string_to_dag_path(test_cube, test_namespace, test_cube_name):
    cube_full_path = mb.cmds.ls(test_cube, long=True)[0]
    assert cube_full_path == f"|{test_namespace}:{test_cube_name}"
    dag_path = mb.nodes.cast.get_dag_path_from_string(cube_full_path)
    assert isinstance(dag_path, mb.OpenMaya2.MDagPath)


def test_invalid_string_to_dag_path(test_cube, test_cube_name):
    with pytest.raises(mb.nodes.cast.InvalidDagPath):
        mb.nodes.cast.get_dag_path_from_string("invalid_name")
    with pytest.raises(mb.nodes.cast.InvalidDagPath):
        mb.nodes.cast.get_dag_path_from_string(test_cube_name)
