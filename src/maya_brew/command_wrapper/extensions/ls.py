from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes._foundation.node_registry import registry
from ...nodes.casting import cast
from ..extension_utils import _node_target_names


def _maya_type_name(node_type: str | type[Node]) -> str:
    if isinstance(node_type, str):
        return node_type
    if node_type._maya_type is None:
        raise NodeException(
            f"Cannot filter by {node_type.__name__}: no native Maya type"
        )
    return node_type._maya_type


def _wrap_filtered_node(name: str, node_types: list[type[Node]]) -> Node:
    node = cast(name)
    for node_type in node_types:
        if isinstance(node, node_type):
            return node
        native_type = node_type._maya_type
        if native_type is not None and isinstance(
            node, registry.get_or_create_class(native_type)
        ):
            return node_type(str(node))
    return node


def ls(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> list[Node | str]:
    """Return wrapped nodes, leaving non-node results as strings.

    Accept wrapped nodes as targets, individually or in sequences. The type,
    exactType, excludeType flags and their aliases also accept wrapper classes
    or mixed sequences of classes and Maya type names.
    Positive class filters preserve the requested wrapper type, including custom
    subclasses. Native subclasses are retained when they satisfy that type.

    Components, attributes, UFE paths, UUIDs, and node-type names remain strings.
    showType and showNamespace retain Maya's flat, interleaved metadata layout.
    objectsOnly gives node-only results without metadata or string-returning
    flags. Use assemblies instead of Maya's Python-keyword alias "as".
    Maya runtime errors are raised as NodeException.
    """
    node_types: list[type[Node]] = []
    for flag in ("type", "typ", "exactType", "et", "excludeType", "ext"):
        if flag not in kwargs:
            continue
        value = kwargs[flag]
        if isinstance(value, Sequence) and not isinstance(value, str):
            kwargs[flag] = [_maya_type_name(node_type) for node_type in value]
        else:
            kwargs[flag] = _maya_type_name(value)
        if flag in ("type", "typ", "exactType", "et"):
            values = (
                value
                if isinstance(value, Sequence) and not isinstance(value, str)
                else (value,)
            )
            node_types.extend(
                node_type for node_type in values if isinstance(node_type, type)
            )
    targets = _node_target_names(args)
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
            wrapped[index] = _wrap_filtered_node(name, node_types)
    return wrapped
