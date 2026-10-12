"""Generate native node classes for the running Maya version.

Run from the repository root with the target release's mayapy:
    mayapy -m tools.node_hierarchy.generate
"""

# @not-generated

from pathlib import Path

from maya_brew import cmds
from maya_brew.log import get_logger
from maya_brew.nodes import _generated
from maya_brew.nodes._foundation import node_extensions
from maya_brew.nodes._foundation.native_node_hierarchy import (
    NodeType,
    discover_node_types,
    python_class_name,
)
from maya_brew.nodes._foundation.node_registry import (
    SNAPSHOT_MODULE,
    snapshot_package_name,
)

logger = get_logger(__name__)
logger.setLevel("INFO")

CLASSES_MODULE = "classes"
HEADER = "# AUTO-GENERATED; DO NOT EDIT.\n# @generated\n"


def generate_artifacts(hierarchy: dict[str, NodeType]) -> dict[str, str]:
    ordered = sorted(
        hierarchy.values(), key=lambda node: (len(node.inheritance), node.name)
    )
    package, _, module = node_extensions.__name__.rpartition(".")
    get_bases = node_extensions.get_bases.__name__
    root = f"ne.{node_extensions.Node.__name__}"
    lines = [HEADER, f"from {package} import {module} as ne\n"]
    for node in ordered:
        class_name = python_class_name(node.name)
        parent = python_class_name(node.parent) if node.parent else root
        lines.extend(
            [
                "\n\n",
                f'class {class_name}(*ne.{get_bases}("{class_name}", {parent})):\n',
                f'    _maya_type = "{node.name}"\n',
                f"    _abstract = {node.abstract!r}\n",
            ]
        )
    constants = [HEADER, f"from . import {CLASSES_MODULE}\n\nTYPE_CLASSES = {{\n"]
    for name in sorted(hierarchy):
        constants.append(f'    "{name}": {CLASSES_MODULE}.{python_class_name(name)},\n')
    constants.append("}\n")
    return {
        f"{CLASSES_MODULE}.py": "".join(lines),
        f"{SNAPSHOT_MODULE}.py": "".join(constants),
        "__init__.py": HEADER,
    }


def main() -> None:
    nodes = discover_node_types()
    version = cmds.about(majorVersion=True)
    package_name = snapshot_package_name(version)
    destination = Path(_generated.__file__).parent / package_name.rpartition(".")[2]
    destination.mkdir(exist_ok=True)
    for filename, content in generate_artifacts(nodes).items():
        (destination / filename).write_text(content, encoding="utf-8", newline="\n")
    logger.info(f"Generated {len(nodes)} types for Maya {version} in {destination}")


if __name__ == "__main__":
    main()
