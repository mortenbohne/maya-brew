from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.node_types import NonLinear
from ..extension_utils import _first_node_result, mode_node_command


class NonLinearType:
    BEND = "bend"
    FLARE = "flare"
    SINE = "sine"
    SQUASH = "squash"
    TWIST = "twist"
    WAVE = "wave"


def _normalize_non_linear_type(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) != 1:
            raise NodeException("nonLinear type expects exactly one type value")
        return _normalize_non_linear_type(value[0])
    raise NodeException(f"Unsupported nonLinear type value: {value!r}")


def _normalize_geometry(value: Any) -> Any:
    if isinstance(value, Node):
        return str(value)
    if isinstance(value, Sequence) and not isinstance(value, str):
        return [str(item) if isinstance(item, Node) else item for item in value]
    return value


_non_linear_command = mode_node_command(
    name="nonLinear",
    command_getter=lambda: _maya_cmds.nonLinear,
    expected_type=NonLinear,
    result_processor=_first_node_result,
    docstring=(
        "Return a NonLinear wrapper on creation; edits and queries keep Maya results. "
        "The type/typ flag accepts strings or single-item sequences of strings."
    ),
)


def nonLinear(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    normalized_kwargs = dict(kwargs)
    for flag in ("type", "typ"):
        if flag in normalized_kwargs:
            normalized_kwargs[flag] = _normalize_non_linear_type(normalized_kwargs[flag])
    for flag in ("geometry", "g"):
        if flag in normalized_kwargs:
            normalized_kwargs[flag] = _normalize_geometry(normalized_kwargs[flag])
    return _non_linear_command(*args, **normalized_kwargs)



