from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ...nodes.node_types import Joint
from ..extension_utils import _call_command, _node_result, _node_target_names


def insertJoint(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Joint:
    """Return the inserted Joint wrapper instead of its name.

    Accept wrapped targets individually or in flat sequences. Preserve Maya's
    selection and parenting behavior. Maya runtime errors become NodeException.
    """
    targets = _node_target_names(args)
    result = _call_command("insertJoint", _maya_cmds.insertJoint, targets, kwargs)
    return _node_result("insertJoint", result, Joint)
