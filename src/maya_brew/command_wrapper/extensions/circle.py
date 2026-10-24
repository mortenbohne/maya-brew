from typing import Any

from ... import _maya_cmds
from ...nodes._foundation.node_extensions import Node
from ..extension_utils import _poly_primitive


def circle(*args: str | Node, **kwargs: Any) -> Any:
    """Return created nodes as wrappers while preserving Maya query/edit behavior.

    Runtime verification shows nodeState/nds query and edit are supported here,
    so this wrapper preserves NodeState conversion like other primitive wrappers.
    """
    return _poly_primitive("circle", _maya_cmds.circle, args, kwargs)
