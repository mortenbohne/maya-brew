from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.node_types import NonLinear
from ..extension_utils import (
    _first_node_result,
    _normalize_node_flag_value,
    mode_node_command,
)


class NonLinearType:
    BEND = "bend"
    FLARE = "flare"
    SINE = "sine"
    SQUASH = "squash"
    TWIST = "twist"
    WAVE = "wave"


_non_linear_command = mode_node_command(
    name="nonLinear",
    command_getter=lambda: _maya_cmds.nonLinear,
    expected_type=NonLinear,
    result_processor=_first_node_result,
    docstring=(
        "Return a NonLinear wrapper on creation; edits and queries keep Maya results. "
        "The type/typ flag accepts strings."
    ),
)


def nonLinear(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    normalized_kwargs = dict(kwargs)
    for flag in ("type", "typ"):
        if flag in normalized_kwargs:
            value = normalized_kwargs[flag]
            if not isinstance(value, str):
                raise NodeException(f"Unsupported nonLinear type value: {value!r}")
            normalized_kwargs[flag] = value
    for flag in ("geometry", "g"):
        if flag in normalized_kwargs:
            normalized_kwargs[flag] = _normalize_node_flag_value(normalized_kwargs[flag])
    return _non_linear_command(*args, **normalized_kwargs)



