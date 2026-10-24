from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ...nodes.node_types import DirectionalLight
from ..extension_utils import _call_command, _node_result, _node_target_names


def directionalLight(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    """Return a DirectionalLight wrapper on creation; edits and queries keep Maya results."""
    targets = _node_target_names(args)
    result = _call_command(
        "directionalLight", _maya_cmds.directionalLight, targets, kwargs
    )
    if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")):
        return result
    return _node_result("directionalLight", result, DirectionalLight)
