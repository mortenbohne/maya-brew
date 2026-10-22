from typing import Any

from .. import _maya_cmds
from ..exceptions import AbstractNodeCreationError, NodeException
from ..nodes._foundation.node_extensions import Node
from ..nodes._foundation.node_registry import registry
from ..nodes.casting import cast
from ..nodes.node_state import NodeState


class Unset:
    """Distinguish omitted command flags from explicitly supplied values."""


UNSET = Unset()


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


def polyPlane(*args: str | Node, **kwargs: Any) -> Any:
    """Return created nodes as a tuple and queried node states as NodeState."""
    try:
        result = _maya_cmds.polyPlane(
            *(str(target) if isinstance(target, Node) else target for target in args),
            **kwargs,
        )
    except RuntimeError as e:
        raise NodeException(f"polyPlane failed: {e}") from e
    if (kwargs.get("query") or kwargs.get("q")) and (
        kwargs.get("nodeState") or kwargs.get("nds")
    ):
        try:
            return NodeState(result)
        except (ValueError, TypeError) as e:
            raise NodeException(
                f"Unexpected node state from polyPlane: {result!r}"
            ) from e
    if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")):
        return result
    if not isinstance(result, list) or not all(
        isinstance(name, str) for name in result
    ):
        raise NodeException(f"Unexpected result from polyPlane: {result!r}")
    return tuple(cast(name) for name in result)
