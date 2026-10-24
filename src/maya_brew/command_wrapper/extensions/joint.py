from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.casting import cast
from ...nodes.node_types import Joint
from ..extension_utils import _node_target_names


def joint(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    """Return a Joint wrapper on creation; edits and queries retain Maya's results.

    Accept wrapped nodes as targets, individually or in flat sequences.
    Selection, parenting, and flag behavior are unchanged. The exists/ex flag
    retains Maya's boolean result even without query mode.
    Maya runtime errors are raised as NodeException.
    """
    targets = _node_target_names(args)
    try:
        result = _maya_cmds.joint(*targets, **kwargs)
    except RuntimeError as e:
        raise NodeException(f"joint failed: {e}") from e
    if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")) or any(
        flag in kwargs for flag in ("exists", "ex")
    ):
        return result
    if not isinstance(result, str):
        raise NodeException(f"Unexpected result from joint: {result!r}")
    return cast(result, Joint)
