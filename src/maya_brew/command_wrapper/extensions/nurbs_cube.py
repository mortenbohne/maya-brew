from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ..extension_utils import _poly_primitive


def nurbsCube(*args: str | Node, **kwargs: Any) -> Any:
    """Return created nodes as wrappers while preserving Maya query/edit behavior."""
    return _poly_primitive("nurbsCube", _maya_cmds.nurbsCube, args, kwargs)
