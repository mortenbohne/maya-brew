from collections.abc import Callable, Sequence
from typing import Any, TypeVar

from ..exceptions import NodeException
from ..nodes._foundation.node_extensions import Node
from ..nodes.casting import cast
from ..nodes.node_state import NodeState

T = TypeVar("T", bound=Node)


def _call_command(
    name: str,
    command: Callable[..., Any],
    args: Sequence[str],
    kwargs: dict[str, Any],
) -> Any:
    try:
        return command(*args, **kwargs)
    except RuntimeError as e:
        raise NodeException(f"{name} failed: {e}") from e


def _node_result(name: str, result: Any, expected_type: type[T]) -> T:
    if not isinstance(result, str):
        raise NodeException(f"Unexpected result from {name}: {result!r}")
    return cast(result, expected_type)


class Unset:
    """Distinguish omitted command flags from explicitly supplied values."""


UNSET = Unset()


def _node_target_names(
    args: Sequence[str | Node | Sequence[str | Node]],
) -> list[str]:
    targets: list[str] = []
    for argument in args:
        if isinstance(argument, (str, Node)):
            argument = [argument]
        for target in argument:
            targets.append(str(target) if isinstance(target, Node) else target)
    return targets


def _poly_primitive(
    name: str,
    command: Callable[..., Any],
    args: Sequence[str | Node],
    kwargs: dict[str, Any],
) -> Any:
    targets = [str(target) if isinstance(target, Node) else target for target in args]
    result = _call_command(name, command, targets, kwargs)
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
