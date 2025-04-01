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