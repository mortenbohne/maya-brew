from typing import Any

from .. import cmds
from ..exceptions import AbstractNodeCreationError, NodeException
from ..nodes._foundation.node_extensions import Node
from ..nodes._foundation.node_registry import registry
from ..nodes.casting import cast
from .typing import node_return


class Unset:
    """Distinguish omitted command flags from explicitly supplied values."""


UNSET = Unset()


@node_return(
    type_argument="node_type",
    nullable_flags=("shared", "s"),
    node_arguments=("parent", "p"),
)
def createNode(node_type: str | type[Node], **kwargs: Any) -> Node | None:
    """Wrap the created node; shared existing nodes return None, as in Maya."""
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
        name = cmds.createNode(node_type, **kwargs)
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
