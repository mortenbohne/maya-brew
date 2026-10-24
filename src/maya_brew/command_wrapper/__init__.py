from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated.maya_2027.commands import *  # noqa: F403, F401
    from ._generated.maya_2027.commands import (  # noqa: F401
        blendShape as blendShape,
        deltaMush as deltaMush,
        skinCluster as skinCluster,
    )
else:
    from ._snapshot import load_commands

    _commands = load_commands()
    __all__ = _commands.__all__
    for _name in __all__:
        globals()[_name] = getattr(_commands, _name)
