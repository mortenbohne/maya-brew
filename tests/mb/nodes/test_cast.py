import pytest
import mb
import mb.nodes.cast


def test_string_to_dag_path():
    namespace_name = "my_new_namespace"
    cube, history = mb.cmds.polyCube(name=f"{namespace_name}:my_cube")
    cube_full_path = mb.cmds.ls(cube, long=True)[0]
    assert namespace_name in cube_full_path
    dag_path = mb.nodes.cast.get_dag_path_from_string(cube_full_path)
    assert isinstance(dag_path, mb.OpenMaya2.MDagPath)



def test_invalid_string_to_dag_path():
    namespace_name = "my_new_namespace"
    cube_short_name = "my_cube"
    cube, history = mb.cmds.polyCube(name=f"{namespace_name}:{cube_short_name}")
    with pytest.raises(mb.nodes.cast.InvalidDagPath):
        invalid_dag_path = mb.nodes.cast.get_dag_path_from_string("invalid_name")
    with pytest.raises(mb.nodes.cast.InvalidDagPath):
        invalid_dag_path = mb.nodes.cast.get_dag_path_from_string("cube_short_name")