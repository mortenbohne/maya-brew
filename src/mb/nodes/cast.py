from mb import OpenMaya2
import mb.exceptions

class NodeCastingException(mb.exceptions.MayaBrewException):
    """Base class for node casting exceptions."""
    pass

class InvalidDagPath(NodeCastingException, RuntimeError, ValueError):
    """Exception raised when a DAG path is invalid."""
    pass


def get_dag_path_from_string(node_path: str) -> OpenMaya2.MDagPath:
    """
    Convert a string representation of a node path to an OpenMaya2.MDagPath object.
    """
    selection_list = OpenMaya2.MSelectionList()
    try:
        selection_list.add(node_path)
    except RuntimeError as e:
        if "Object does not exist" in str(e):
            raise InvalidDagPath(f"Invalid DAG path: {node_path}") from e
        raise
    dag_path = selection_list.getDagPath(0)
    return dag_path
