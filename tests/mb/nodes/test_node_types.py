import mb.nodes.node_types
import mb.nodes.cast
import logging


def test_dag_node_string(test_cube, caplog):
    dag_node = mb.nodes.node_types.DagNode(test_cube)
    full_node_path = mb.nodes.cast.get_long_name_from_maya_string(test_cube)
    assert str(dag_node) == full_node_path
    # rename to see warning display correct node path when deleted
    new_name = "new_name"
    dag_node.rename(new_name)
    mb.cmds.delete(str(dag_node))
    with caplog.at_level(logging.WARNING):
        str(dag_node)
        node_path = dag_node.node_path
        assert node_path in str(caplog.text)


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


def test_Transform_repr():
    name = "hello"
    dag_node = mb.nodes.node_types.Transform.create(name)
    repr = dag_node.__repr__()
    assert name in repr
    assert dag_node.get_full_path() in repr
    assert type(dag_node).__name__ in repr

