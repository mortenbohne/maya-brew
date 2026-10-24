from typing import Any

from ... import _maya_cmds
from ..extension_utils import _call_command


def ikSystemInfo(*args: bool, **kwargs: Any) -> bool | None:
    """Preserve Maya's system-control result, including None in standalone mode."""
    return _call_command("ikSystemInfo", _maya_cmds.ikSystemInfo, args, kwargs)
