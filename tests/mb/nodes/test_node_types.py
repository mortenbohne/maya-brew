import mb.nodes.node_types
import mb.nodes.cast
import logging


def test_dag_node_string(test_cube, caplog):
    dag_node = mb.nodes.node_types.DagNode(test_cube)
    full_node_path = mb.nodes.cast.get_long_name_from_maya_string(test_cube)
    assert str(dag_node) == full_node_path
    mb.cmds.delete(test_cube)
    with caplog.at_level(logging.WARNING):
        node_path = str(dag_node)


def test_dag_node_rename(test_cube, caplog):
    dag_node = mb.nodes.node_types.DagNode(test_cube)
    new_name = "new_name"
    new_resolved_name = dag_node.rename(new_name)
    assert new_resolved_name == new_name
    another_cube = mb.cmds.polyCube(name="another_cube")[0]
    another_dag_node = mb.nodes.node_types.DagNode(another_cube)
    another_cube_new_name = another_dag_node.rename(new_name)
    assert another_cube_new_name != new_name
    assert another_cube_new_name == "new_name1"
    another_dag_node_full_path = f"|{another_cube_new_name}"
    assert str(another_dag_node) == another_dag_node_full_path
    assert another_dag_node.dag_path.fullPathName() == another_dag_node_full_path
