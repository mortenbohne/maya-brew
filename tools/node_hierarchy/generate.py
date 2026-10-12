"""Build native node hierarchy source and typing stubs."""

# @not-generated

from maya_brew.nodes._foundation import node_extensions
from maya_brew.nodes._foundation.native_node_hierarchy import (
    NodeType,
    python_class_name,
)
from maya_brew.nodes._foundation.node_registry import (
    SNAPSHOT_MODULE,
)

CLASSES_MODULE = "classes"
HEADER = "# AUTO-GENERATED; DO NOT EDIT.\n# @generated\n"


def generate_node_files(hierarchy: dict[str, NodeType]) -> dict[str, str]:
    ordered = sorted(
        hierarchy.values(), key=lambda node: (len(node.inheritance), node.name)
    )
    package, _, module = node_extensions.__name__.rpartition(".")
    get_bases = node_extensions.get_bases.__name__
    root = f"ne.{node_extensions.Node.__name__}"
    lines = [HEADER, f"from {package} import {module} as ne\n"]
    stub_lines = [
        HEADER,
        "from typing import ClassVar\n\n",
        f"from {package} import {module} as ne\n",
    ]
    wrappers: dict[str, type[node_extensions.Node]] = {}
    for node in ordered:
        class_name = python_class_name(node.name)
        parent = python_class_name(node.parent) if node.parent else root
        parent_class = wrappers[node.parent] if node.parent else node_extensions.Node
        bases = node_extensions.get_bases(class_name, parent_class)
        wrappers[node.name] = type(class_name, bases, {})
        stub_bases = ", ".join(
            parent if base is parent_class else f"ne.{base.__name__}"
            for base in bases
        )
        stub_lines.append(
            f"\n\nclass {class_name}({stub_bases}):\n"
            "    _maya_type: ClassVar[str]\n"
            "    _abstract: ClassVar[bool]\n"
        )
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
        f"{CLASSES_MODULE}.pyi": "".join(stub_lines),
        f"{SNAPSHOT_MODULE}.py": "".join(constants),
        "__init__.py": HEADER,
    }
