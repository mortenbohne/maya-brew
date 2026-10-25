from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.casting import cast
from ..extension_utils import _call_command, _node_target_names


class WrinkleStyle:
    RADIAL = "radial"
    LINES = "lines"


def wrinkle(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> tuple[Node, ...]:
    """Return wrinkle-created nodes as wrapped native node instances.

    Note: Maya 2027 runtime accepts ``style`` values ``"radial"`` and ``"lines"``.
    """
    targets = _node_target_names(args)
    result = _call_command("wrinkle", _maya_cmds.wrinkle, targets, kwargs)
    if not isinstance(result, list) or not all(isinstance(name, str) for name in result):
        raise NodeException(f"Unexpected result from wrinkle: {result!r}")
    return tuple(cast(name) for name in result)


