from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ..extension_utils import (
    _normalize_node_flag_value,
    _single_node_result,
    mode_node_command,
)


class DeformerType:
    BLEND_SHAPE = "blendShape"
    CLUSTER = "cluster"
    DELTA_MUSH = "deltaMush"
    LATTICE = "lattice"
    NON_LINEAR = "nonLinear"
    PROXIMITY_WRAP = "proximityWrap"
    SCULPT = "sculpt"
    SKIN_CLUSTER = "skinCluster"
    SOFT_MOD = "softMod"
    TENSION = "tension"
    TEXTURE_DEFORMER = "textureDeformer"
    WIRE = "wire"


_deformer_command = mode_node_command(
    name="deformer",
    command_getter=lambda: _maya_cmds.deformer,
    expected_type=Node,
    result_processor=_single_node_result,
    docstring=(
        "Return a wrapped deformer node on creation; edits and queries keep Maya "
        "results. The type/typ flag accepts strings (use DeformerType constants)."
    ),
)


def deformer(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    for flag in ("geometry", "g"):
        if flag in kwargs:
            kwargs[flag] = _normalize_node_flag_value(kwargs[flag])
    return _deformer_command(*args, **kwargs)
