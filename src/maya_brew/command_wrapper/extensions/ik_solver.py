from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.casting import cast
from ...nodes.node_types import IkSolver
from ..extension_utils import _node_target_names


def ikSolver(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    """Return a native solver wrapper on creation instead of its name.

    Accept wrapped targets individually or in flat sequences. Edits and queries
    retain Maya's results. Maya runtime errors are raised as NodeException.
    """
    targets = _node_target_names(args)
    try:
        result: Any = _maya_cmds.ikSolver(*targets, **kwargs)
    except RuntimeError as e:
        raise NodeException(f"ikSolver failed: {e}") from e
    if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")):
        return result
    if not isinstance(result, str):
        raise NodeException(f"Unexpected result from ikSolver: {result!r}")
    return cast(result, IkSolver)
