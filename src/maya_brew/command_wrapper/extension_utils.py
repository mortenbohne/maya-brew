from collections.abc import Callable, Sequence
from typing import Any

from ..exceptions import NodeException
from ..nodes._foundation.node_extensions import Node
from ..nodes.casting import cast
from ..nodes.node_state import NodeState


class Unset:
    """Distinguish omitted command flags from explicitly supplied values."""


UNSET = Unset()


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
