from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.node_types import TextureDeformer
from ..extension_utils import (
    _first_node_result,
    _normalize_node_flag_value,
    mode_node_command,
)


class TextureDeformerDirection:
    NORMAL = "Normal"
    HANDLE = "Handle"
    VECTOR = "Vector"


class TextureDeformerPointSpace:
    WORLD = "World"
    LOCAL = "Local"
    UV = "UV"


class TextureDeformerVectorSpace:
    OBJECT = "Object"
    WORLD = "World"
    TANGENT = "Tangent"


_texture_deformer_command = mode_node_command(
    name="textureDeformer",
    command_getter=lambda: _maya_cmds.textureDeformer,
    expected_type=TextureDeformer,
    result_processor=_first_node_result,
    docstring=(
        "Return a TextureDeformer wrapper on creation; edits and queries keep Maya "
        "results. direction/pointSpace/vectorSpace accept constants or strings."
    ),
)


def textureDeformer(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    normalized_kwargs = dict(kwargs)
    for flag in ("direction", "d", "pointSpace", "ps", "vectorSpace", "vsp"):
        if flag in normalized_kwargs:
            value = normalized_kwargs[flag]
            if not isinstance(value, str):
                raise NodeException(
                    f"Unsupported textureDeformer {flag} value: {value!r}"
                )
            normalized_kwargs[flag] = value
    for flag in ("geometry", "g"):
        if flag in normalized_kwargs:
            normalized_kwargs[flag] = _normalize_node_flag_value(
                normalized_kwargs[flag]
            )
    return _texture_deformer_command(*args, **normalized_kwargs)
