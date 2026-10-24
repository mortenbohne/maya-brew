from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ..extension_utils import _call_command, _node_target_names


def CreateWrap(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> None:
    """Mirror Maya's runtime wrap-creation command and return None."""
    targets = _node_target_names(args)
    command = getattr(_maya_cmds, "CreateWrap")
    result = _call_command("CreateWrap", command, targets, kwargs)
    if result is not None:
        raise NodeException(f"Unexpected result from CreateWrap: {result!r}")
    return None
