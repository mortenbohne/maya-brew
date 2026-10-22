from typing import TYPE_CHECKING, TypeVar, overload

from .. import OpenMaya2, _maya_cmds
from ..exceptions import (
    InvalidDagPath,
    MultipleMatchingNodes,
    NodeCastingException,
    NodeException,
    NoMatchingNodes,
    NonExistingDagPath,
)

if TYPE_CHECKING:
    from ._foundation.node_extensions import Node

T = TypeVar("T", bound="Node")


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


def get_long_name_from_maya_string(name: str) -> str:
    """
    Convert a unique maya.cmds node string to a long name.
    """
    matching_nodes = _maya_cmds.ls(name, long=True)
    if not matching_nodes:
        raise NoMatchingNodes(f"No objects matching '{name}' in scene")
    num_nodes = len(matching_nodes)
    if num_nodes > 1:
        raise MultipleMatchingNodes(
            f"Multiple objects matching '{name}' in scene. Found {num_nodes} nodes: {matching_nodes}"
        )
    return matching_nodes[0]


@overload
def cast(node_path: str) -> "Node": ...


@overload
def cast(node_path: str, expected_type: type[T]) -> T: ...


def cast(node_path: str, expected_type: "type[T] | None" = None) -> "Node | T":
    """Wrap a unique node name, optionally checking an expected wrapper type."""
    from ._foundation.node_registry import registry

    if not isinstance(node_path, str) or not node_path or "." in node_path:
        raise NodeException("Expected a node name, not an attribute or component")
    try:
        long_name = get_long_name_from_maya_string(node_path)
        maya_type = _maya_cmds.nodeType(long_name)
    except RuntimeError as e:
        raise NodeException(f"Cannot resolve node {node_path!r}: {e}") from e
    node = registry.get_or_create_class(maya_type)(long_name)
    if expected_type is not None:
        if not isinstance(node, expected_type):
            raise NodeCastingException(
                f"Expected {expected_type.__name__} for {node_path!r}, "
                f"got {type(node).__name__}"
            )
        return node
    return node
