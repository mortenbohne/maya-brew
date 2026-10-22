import importlib
from pathlib import Path
from types import ModuleType

from .. import cmds
from ..exceptions import MayaBrewException
from ..log import get_logger
from . import _generated

logger = get_logger(__name__)
COMMANDS_MODULE = "commands"


def snapshot_package_name(version: str | int) -> str:
    return f"{_generated.__name__}.maya_{version}"


def load_commands() -> ModuleType:
    try:
        version = cmds.about(majorVersion=True)
    except RuntimeError as e:
        raise MayaBrewException(f"Cannot determine Maya version: {e}") from e
    package = snapshot_package_name(version)
    module = f"{package}.{COMMANDS_MODULE}"
    try:
        return importlib.import_module(module)
    except ModuleNotFoundError as e:
        if e.name not in {package, module}:
            raise
    versions = [
        int(path.name.split("_")[1])
        for path in Path(_generated.__file__).parent.glob("maya_[0-9][0-9][0-9][0-9]")
        if path.is_dir()
    ]
    if not versions:
        raise MayaBrewException("No generated command snapshots are available")
    latest = max(versions)
    logger.warning(
        f"No generated command snapshot for Maya {version}; "
        f"using Maya {latest} command wrappers."
    )
    return importlib.import_module(f"{snapshot_package_name(latest)}.{COMMANDS_MODULE}")
