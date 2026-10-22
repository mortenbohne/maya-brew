"""Generate native node snapshots and command wrappers with the target mayapy."""

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
