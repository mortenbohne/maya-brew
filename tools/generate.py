"""Generate versioned node and command artifacts for the active Maya runtime.

Usage:
    mayapy -m tools.generate

The entry point coordinates two generation pipelines:

1) Node hierarchy snapshots (`tools.node_hierarchy.generate`), which emit
   classes/stubs and a `TYPE_CLASSES` map for the active Maya major version.
2) Command wrapper files (`tools.command_wrapper.generate`), which emit runtime
   wrappers and `.pyi` stubs based on extension metadata and `cmds.help()`.

Artifacts are written under versioned generated packages so runtime loading can
select the closest matching snapshot for the running Maya build.
"""

from pathlib import Path

import maya.cmds as cmds
from maya_brew.log import get_logger
from maya_brew.nodes import _generated
from maya_brew.nodes._foundation.native_node_hierarchy import discover_node_types
from maya_brew.nodes._foundation.node_registry import snapshot_package_name
from tools.command_wrapper.generate import write_wrappers
from tools.node_hierarchy.generate import generate_node_files

logger = get_logger(__name__)
logger.setLevel("INFO")


def generate() -> None:
    """Regenerate all versioned node and command artifacts for this Maya session."""
    nodes = discover_node_types()
    version = cmds.about(majorVersion=True)
    package_name = snapshot_package_name(version)
    destination = Path(_generated.__file__).parent / package_name.rpartition(".")[2]
    destination.mkdir(exist_ok=True)
    for filename, content in generate_node_files(nodes).items():
        (destination / filename).write_text(content, encoding="utf-8", newline="\n")
    write_wrappers(nodes, version)
    logger.info(f"Generated node and command wrappers for Maya {version}")


if __name__ == "__main__":
    generate()
