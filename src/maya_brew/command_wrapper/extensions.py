from collections.abc import Callable, Sequence
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


def _maya_type_name(node_type: str | type[Node]) -> str:
    if isinstance(node_type, str):
        return node_type
    if node_type._maya_type is None:
        raise NodeException(
            f"Cannot filter by {node_type.__name__}: no native Maya type"
        )
    return node_type._maya_type


def ls(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> list[Node | str]:
    """Return wrapped nodes, leaving non-node results as strings.

    Accept wrapped nodes as targets, individually or in sequences. The type,
    exactType, excludeType flags and their aliases also accept wrapper classes
    or mixed sequences of classes and Maya type names.

    Components, attributes, UFE paths, UUIDs, and node-type names remain strings.
    showType and showNamespace retain Maya's flat, interleaved metadata layout.
    objectsOnly gives node-only results without metadata or string-returning
    flags. Use assemblies instead of Maya's Python-keyword alias "as".
    Maya runtime errors are raised as NodeException.
    """
    for flag in ("type", "typ", "exactType", "et", "excludeType", "ext"):
        if flag not in kwargs:
            continue
        value = kwargs[flag]
        if isinstance(value, Sequence) and not isinstance(value, str):
            kwargs[flag] = [_maya_type_name(node_type) for node_type in value]
        else:
            kwargs[flag] = _maya_type_name(value)
    targets: list[str] = []
    for argument in args:
        if isinstance(argument, (str, Node)):
            argument = [argument]
        for target in argument:
            targets.append(str(target) if isinstance(target, Node) else target)
    try:
        result = _maya_cmds.ls(*targets, **kwargs)
    except RuntimeError as e:
        raise NodeException(f"ls failed: {e}") from e
    if result is None:
        return []
    if not isinstance(result, list) or not all(
        isinstance(name, str) for name in result
    ):
        raise NodeException(f"Unexpected result from ls: {result!r}")
    if any(kwargs.get(flag) for flag in ("uuid", "uid", "nodeTypes", "nt")):
        return list(result)
    paired = any(
        kwargs.get(flag) for flag in ("showType", "st", "showNamespace", "sns")
    )
    if paired and len(result) % 2:
        raise NodeException(f"Expected name/metadata pairs from ls: {result!r}")
    wrapped: list[Node | str] = list(result)
    step = 2 if paired else 1
    for index in range(0, len(result), step):
        name = result[index]
        # UFE paths separate their runtime-specific segments with commas.
        if "." not in name and "," not in name:
            wrapped[index] = cast(name)
    return wrapped


def polyPlane(*args: str | Node, **kwargs: Any) -> Any:
    """Return created nodes as a tuple of wrappers instead of a list of names.

    Accept wrapped nodes as targets. nodeState queries return NodeState;
    other queries and edits retain Maya's return values.
    Maya runtime errors are raised as NodeException.
    """
    return _poly_primitive("polyPlane", _maya_cmds.polyPlane, args, kwargs)


def polySphere(*args: str | Node, **kwargs: Any) -> Any:
    """Return created nodes as a tuple of wrappers instead of a list of names.

    Accept wrapped nodes as targets. nodeState queries return NodeState;
    other queries and edits retain Maya's return values.
    Maya runtime errors are raised as NodeException.
    """
    return _poly_primitive("polySphere", _maya_cmds.polySphere, args, kwargs)


def _poly_primitive(
    name: str,
    command: Callable[..., Any],
    args: Sequence[str | Node],
    kwargs: dict[str, Any],
) -> Any:
    try:
        result = command(
            *(str(target) if isinstance(target, Node) else target for target in args),
            **kwargs,
        )
    except RuntimeError as e:
        raise NodeException(f"{name} failed: {e}") from e
    if (kwargs.get("query") or kwargs.get("q")) and (
        kwargs.get("nodeState") or kwargs.get("nds")
    ):
        try:
            return NodeState(result)
        except (ValueError, TypeError) as e:
            raise NodeException(f"Unexpected node state from {name}: {result!r}") from e
    if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")):
        return result
    if not isinstance(result, list) or not all(
        isinstance(name, str) for name in result
    ):
        raise NodeException(f"Unexpected result from {name}: {result!r}")
    return tuple(cast(name) for name in result)
