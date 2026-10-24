from typing import Any

from ... import _maya_cmds
from ..extension_utils import _call_command


def jointDisplayScale(*args: float, **kwargs: Any) -> float | None:
    """Preserve Maya's scale and diameter semantics; runtime errors become NodeException."""
    return _call_command(
        "jointDisplayScale", _maya_cmds.jointDisplayScale, args, kwargs
    )
