from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ...nodes.node_types import IkSolver
from ..extension_utils import _call_command, _node_result, _node_target_names


def ikSolver(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    """Return a native solver wrapper on creation instead of its name.

    Accept wrapped targets individually or in flat sequences. Edits and queries
    retain Maya's results. Maya runtime errors are raised as NodeException.
    """
    targets = _node_target_names(args)
    result = _call_command("ikSolver", _maya_cmds.ikSolver, targets, kwargs)
    if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")):
        return result
    return _node_result("ikSolver", result, IkSolver)
