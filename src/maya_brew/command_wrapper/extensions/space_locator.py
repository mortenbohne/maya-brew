from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.casting import cast
from ...nodes.node_types import Transform
from ..extension_utils import _call_command, _node_target_names


def spaceLocator(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    """Return a Transform wrapper on creation; edits and queries keep Maya results."""
    targets = _node_target_names(args)
    result = _call_command("spaceLocator", _maya_cmds.spaceLocator, targets, kwargs)
    if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")):
        return result
    if (
        not isinstance(result, list)
        or len(result) != 1
        or not isinstance(result[0], str)
    ):
        raise NodeException(f"Unexpected result from spaceLocator: {result!r}")
    return cast(result[0], Transform)
