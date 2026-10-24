from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ...nodes.node_types import Sculpt
from ..extension_utils import _call_command, _first_node_result, _node_target_names


def sculpt(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    """Return a Sculpt wrapper on creation; edits and queries keep Maya results."""
    targets = _node_target_names(args)
    result = _call_command("sculpt", _maya_cmds.sculpt, targets, kwargs)
    if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")):
        return result
    return _first_node_result("sculpt", result, Sculpt)

