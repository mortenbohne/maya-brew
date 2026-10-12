"""
Discover Maya node types and their inheritance for wrapper class generation.

Includes abstract types and unlisted ancestors, with optional plug-in types.
Provides consistent Python class naming for generated and runtime wrappers.
"""

import keyword
import re
from dataclasses import dataclass

import maya.cmds as cmds
from maya_brew.exceptions import NodeTypeInheritanceError


@dataclass
class NodeType:
    name: str
    inheritance: tuple[str, ...]
    abstract: bool = False

    @property
    def parent(self) -> str | None:
        if len(self.inheritance) < 2:
            return None
        return self.inheritance[-2]


def python_class_name(name: str) -> str:
    parts = [part for part in re.split(r"[^a-zA-Z0-9_]+", name) if part]
    result = "".join(part[0].upper() + part[1:] for part in parts)
    if not result:
        raise NodeTypeInheritanceError(f"Cannot name Python class for {name!r}")
    if result[0].isdigit():
        result = "Node" + result
    if keyword.iskeyword(result):
        result += "Node"
    return result


def query_node_type(name: str) -> tuple[str, ...]:
    # Maya's abstract "node" sentinel returns no inherited chain.
    if name == "node":
        return (name,)
    try:
        inheritance = tuple(cmds.nodeType(name, inherited=True, isTypeName=True) or ())
    except RuntimeError as e:
        raise NodeTypeInheritanceError(f"Cannot query node type {name!r}: {e}") from e
    return inheritance


def discover_node_types(include_plugins: bool = False) -> dict[str, NodeType]:
    """Preserve Maya's exact chains, including unlisted internal ancestors."""
    try:
        concrete_types = set(cmds.allNodeTypes() or ())
        all_types = {
            name.removesuffix(" (abstract)")
            for name in (cmds.allNodeTypes(includeAbstract=True) or ())
        }
        plugin_types: set[str] = set()
        if not include_plugins:
            for plugin in cmds.pluginInfo(query=True, listPlugins=True) or ():
                plugin_types.update(
                    cmds.pluginInfo(plugin, query=True, dependNode=True) or ()
                )
    except RuntimeError as e:
        raise NodeTypeInheritanceError(f"Cannot enumerate node types: {e}") from e

    inheritances: dict[str, tuple[str, ...]] = {}
    for name in all_types - plugin_types:
        chain = query_node_type(name)
        for index, ancestor in enumerate(chain):
            inheritances[ancestor] = chain[: index + 1]

    return {
        name: NodeType(name, chain, abstract=name not in concrete_types)
        for name, chain in inheritances.items()
    }
