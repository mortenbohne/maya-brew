from mb.log import get_logger
import mb.nodes.cast as cast
from mb import OpenMaya2, cmds

logger = get_logger(__name__)
logger.setLevel("DEBUG")


class Node:
    def __init__(self, node_path: str):
        self.node_path = node_path

    def rename(self, new_name: str, *args, **kwargs) -> str:
        """
        Rename the current node. If new name is not unique maya will resolve a new unique name.
        :param new_name: The new name of the node.
        :return: The new name of the node.
        """
        actual_new_name = cmds.rename(str(self), new_name, *args, **kwargs)
        self.node_path = actual_new_name
        return actual_new_name


class DagNode(Node):
    def __init__(self, node_path: str):
        super().__init__(node_path)
        self.dag_path = cast.get_dag_path_from_string(node_path)

    def __str__(self):
        return self.get_full_path()

    def get_depend_node(self) -> OpenMaya2.MObject:
        """
        Get the depend node of the current node.
        :return: The depend node of the current node.
        """
        return self.dag_path.node()

    def get_full_path(self) -> str:
        """
        Get the full path of the current node.
        :return: The full path of the current node.
        """
        full_path = self.dag_path.fullPathName()
        if not full_path:
            logger.warning(f"Node has been deleted. Original path: {self.node_path}")
        return full_path
