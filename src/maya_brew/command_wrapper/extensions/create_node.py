from typing import Any

from ... import _maya_cmds
from ...exceptions import AbstractNodeCreationError, NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes._foundation.node_registry import registry
from ...nodes.casting import cast


def createNode(node_type: str | type[Node], **kwargs: Any) -> Node | None:
    """Return a wrapped node instead of a name; shared existing nodes return None.

    Accept a wrapper class as node_type and a wrapped node as parent (or p).
    Maya runtime errors are raised as NodeException subclasses.
    """
    wrapper = None
    if not isinstance(node_type, str):
        wrapper = node_type
        if wrapper._abstract or wrapper._maya_type is None:
            raise AbstractNodeCreationError(
                f"Cannot create a node from abstract class {wrapper.__name__}"
            )
        node_type = wrapper._maya_type
    for flag in ("parent", "p"):
        if isinstance(kwargs.get(flag), Node):
            kwargs[flag] = str(kwargs[flag])
    try:
        name = _maya_cmds.createNode(node_type, **kwargs)
    except RuntimeError as e:
        if registry.get_or_create_class(node_type)._abstract:
            raise AbstractNodeCreationError(
                f"Cannot create a node of abstract Maya type {node_type}"
            ) from e
        raise NodeException(f"Cannot create {node_type}: {e}") from e
    if name is None:
        return None
    node = cast(name)
    return wrapper(str(node)) if wrapper is not None else node
