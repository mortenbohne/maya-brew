from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ..extension_utils import _call_command, _node_target_names


def connectJoint(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> None:
    """Accept wrapped targets individually or in flat sequences.

    Preserve Maya's selection behavior and return value.
    Maya runtime errors are raised as NodeException.
    """
    targets = _node_target_names(args)
    _call_command("connectJoint", _maya_cmds.connectJoint, targets, kwargs)
