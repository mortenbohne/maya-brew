from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ..extension_utils import _poly_primitive


def polyPrimitive(*args: str | Node, **kwargs: Any) -> Any:
    """Return created nodes as a tuple of wrappers instead of a list of names.

    The history node is PolyPrimitiveMisc. Accept wrapped nodes as targets.
    nodeState queries return NodeState; other queries and edits retain Maya's
    return values. Maya runtime errors are raised as NodeException.
    """
    return _poly_primitive("polyPrimitive", _maya_cmds.polyPrimitive, args, kwargs)
