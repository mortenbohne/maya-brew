from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.node_types import FlexorShape
from ..extension_utils import _first_node_result, mode_node_command


class FlexorType:
    SCULPT = "sculpt"
    JOINT_LATTICE = "jointLattice"
    BONE_LATTICE = "boneLattice"
    JOINT_CLUSTER = "jointCluster"


class FlexorDeformerCommand:
    SCULPT = "sculpt"
    LATTICE = "lattice"
    JOINT_CLUSTER = "jointCluster"


_flexor_command = mode_node_command(
    name="flexor",
    command_getter=lambda: _maya_cmds.flexor,
    expected_type=FlexorShape,
    result_processor=_first_node_result,
    docstring=(
        "Return a FlexorShape wrapper on creation; list/query/edit keep Maya results. "
        "type/typ and deformerCommand/dc accept strings."
    ),
)


def flexor(*args: str | Node, **kwargs: Any) -> Any:
    normalized_kwargs = dict(kwargs)
    for flag in ("type", "typ", "deformerCommand", "dc"):
        if flag in normalized_kwargs:
            value = normalized_kwargs[flag]
            if not isinstance(value, str):
                raise NodeException(f"Unsupported flexor {flag} value: {value!r}")
            normalized_kwargs[flag] = value
    return _flexor_command(*args, **normalized_kwargs)
