from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ...nodes.node_types import DeltaMush
from ..extension_utils import (
    _call_command,
    _node_target_names,
    _single_node_result,
)


def deltaMush(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    """Return a DeltaMush wrapper on creation; edits and queries keep Maya results."""
    targets = _node_target_names(args)
    result = _call_command("deltaMush", _maya_cmds.deltaMush, targets, kwargs)
    if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")):
        return result
    return _single_node_result("deltaMush", result, DeltaMush)
