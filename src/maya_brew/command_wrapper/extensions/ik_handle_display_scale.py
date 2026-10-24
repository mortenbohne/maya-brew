from typing import Any

from ... import _maya_cmds
from ..extension_utils import _call_command


def ikHandleDisplayScale(*args: float, **kwargs: Any) -> float | None:
    """Preserve Maya's global scale result, including None in standalone mode."""
    return _call_command(
        "ikHandleDisplayScale", _maya_cmds.ikHandleDisplayScale, args, kwargs
    )
