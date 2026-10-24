from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ..extension_utils import _history_primitive


def polyCylinder(*args: str | Node, **kwargs: Any) -> Any:
    """Return created nodes as a tuple of wrappers instead of a list of names.

    Accept wrapped nodes as targets. nodeState queries return NodeState;
    other queries and edits retain Maya's return values.
    Maya runtime errors are raised as NodeException.
    """
    return _history_primitive("polyCylinder", _maya_cmds.polyCylinder, args, kwargs)
