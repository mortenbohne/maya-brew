from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.casting import cast
from ..extension_utils import _call_command, _node_target_names


def mirrorJoint(
    *args: str | Node | Sequence[str | Node], **kwargs: Any
) -> tuple[Node, ...]:
    """Return mirrored nodes as a tuple of native wrappers instead of names.

    Non-joint descendants retain their native wrapper types. Accept wrapped
    targets individually or in flat sequences; preserve Maya's selection behavior.
    Maya runtime errors are raised as NodeException.
    """
    targets = _node_target_names(args)
    result = _call_command("mirrorJoint", _maya_cmds.mirrorJoint, targets, kwargs)
    if not isinstance(result, list) or not all(
        isinstance(name, str) for name in result
    ):
        raise NodeException(f"Unexpected result from mirrorJoint: {result!r}")
    return tuple(cast(name) for name in result)
