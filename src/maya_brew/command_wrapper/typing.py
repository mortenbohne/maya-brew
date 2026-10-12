from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


@dataclass(frozen=True)
class NodeReturn:
    type_argument: str
    nullable_flags: tuple[str, ...]
    node_arguments: tuple[str, ...]
    flag_types: dict[str, str]


NODE_RETURNS: dict[Callable[..., Any], NodeReturn] = {}


def node_return(
    type_argument: str,
    nullable_flags: tuple[str, ...] = (),
    node_arguments: tuple[str, ...] = (),
    flag_types: dict[str, str] | None = None,
) -> Callable[[F], F]:
    """Declare node-return typing for stub generation without wrapping the call."""

    def decorate(function: F) -> F:
        NODE_RETURNS[function] = NodeReturn(
            type_argument, nullable_flags, node_arguments, dict(flag_types or {})
        )
        return function

    return decorate
