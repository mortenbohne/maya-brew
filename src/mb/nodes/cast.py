from mb import OpenMaya2
import mb.exceptions

class NodeCastingException(mb.exceptions.MayaBrewException):
    """Base class for node casting exceptions."""
    pass


class InvalidDagPath(NodeCastingException, RuntimeError, ValueError, TypeError):
    """Exception raised when a DAG path is invalid."""
    pass

class NonExistingDagPath(NodeCastingException, RuntimeError, ValueError, TypeError):
    """Exception raised when a DAG path is invalid."""
    pass


def get_dag_path_from_string(node_path: str) -> OpenMaya2.MDagPath:
    """
    Convert a string representation of a node path to an OpenMaya2.MDagPath object.
    """
    selection_list = OpenMaya2.MSelectionList()
    try:
        selection_list.add(node_path)
        dag_path = selection_list.getDagPath(0)
    except RuntimeError as e:
        if "Object does not exist" in str(e):
            raise NonExistingDagPath(f"Dag Path does not exist: {node_path}") from e
        raise
    except TypeError as e:
        if "item is not a DAG path" in str(e):
            raise InvalidDagPath(f"{node_path} exists but is not a dag object") from e
        raise
    return dag_path

