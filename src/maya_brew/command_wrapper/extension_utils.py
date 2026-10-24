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
    args: Sequence[object],
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


def _single_node_result(name: str, result: Any, expected_type: type[T]) -> T:
    if isinstance(result, str):
        return cast(result, expected_type)
    if isinstance(result, list) and len(result) == 1 and isinstance(result[0], str):
        return cast(result[0], expected_type)
    raise NodeException(f"Unexpected result from {name}: {result!r}")


def _first_node_result(name: str, result: Any, expected_type: type[T]) -> T:
    if isinstance(result, str):
        return cast(result, expected_type)
    if isinstance(result, list) and result and isinstance(result[0], str):
        return cast(result[0], expected_type)
    raise NodeException(f"Unexpected result from {name}: {result!r}")


def mode_node_command(
    name: str,
    command_getter: Callable[[], Callable[..., Any]],
    expected_type: type[T],
    result_processor: Callable[[str, Any, type[T]], T],
    docstring: str,
) -> Callable[..., Any]:
    """Build a command wrapper that preserves Maya edit/query results."""

    def wrapper(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
        targets = _node_target_names(args)
        result = _call_command(name, command_getter(), targets, kwargs)
        if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")):
            return result
        return result_processor(name, result, expected_type)

    wrapper.__name__ = name
    wrapper.__qualname__ = name
    wrapper.__doc__ = docstring
    return wrapper


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


def _history_primitive(
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
