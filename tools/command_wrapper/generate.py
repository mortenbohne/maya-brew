"""Generate command signatures from Maya help and handwritten extensions."""

# @not-generated

import inspect
import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

from maya_brew import cmds
from maya_brew.command_wrapper import _generated, _snapshot, extensions
from maya_brew.command_wrapper.typing import NODE_RETURNS, NodeReturn
from maya_brew.exceptions import MayaBrewException
from maya_brew.nodes._foundation import node_extensions
from maya_brew.nodes._foundation.native_node_hierarchy import (
    NodeType,
    python_class_name,
)
from maya_brew.nodes._foundation.node_registry import snapshot_package_name
from tools.node_hierarchy.generate import CLASSES_MODULE

HEADER = "# AUTO-GENERATED; DO NOT EDIT.\n# @generated\n"
CONCRETE_NODES_MODULE = "concrete_nodes"
CONCRETE_NODE_ALIAS = "ConcreteNode"


def command_flags(
    command: str, help_text: str, overrides: dict[str, str]
) -> dict[str, str]:
    types = {
        "": "bool",
        "String": "str",
        "Int": "int",
        "Float": "float",
        "Boolean": "bool",
    }
    flags: dict[str, str] = {}
    for line in help_text.splitlines():
        if not line.lstrip().startswith("-"):
            continue
        match = re.fullmatch(r"\s*-(\w+)\s+-(\w+)\s*(.*?)\s*", line)
        if match is None:
            raise ValueError(f"{command}: unsupported flag help line {line!r}")
        alias, name, maya_type = match.groups()
        annotation = overrides.get(name, overrides.get(alias, types.get(maya_type)))
        if annotation is None:
            raise ValueError(
                f"{command}.{name}: unsupported help type {maya_type!r}; "
                "supply a flag_types override"
            )
        flags[name] = annotation
        flags[alias] = annotation
    if not flags and not overrides:
        raise ValueError(f"{command}: no flags found in Maya help; supply flag_types")
    flags.update(overrides)
    return flags


def generate_concrete_node_stub(hierarchy: dict[str, NodeType], version: str) -> str:
    # Concrete descendants are already accepted through their concrete ancestor.
    concrete_root_names = [
        name
        for name, node in sorted(hierarchy.items())
        if not node.abstract
        and not any(
            not hierarchy[ancestor].abstract for ancestor in node.inheritance[:-1]
        )
    ]
    return "".join(
        [
            HEADER,
            "from typing import TypeAlias\n\n",
            f"from {snapshot_package_name(version)} import {CLASSES_MODULE} as native\n\n",
            f"{CONCRETE_NODE_ALIAS}: TypeAlias = (\n",
            "    "
            + "\n    | ".join(
                f"native.{python_class_name(name)}" for name in concrete_root_names
            ),
            "\n)\n",
        ]
    )


def generate_command_definition(
    function_name: str, policy: NodeReturn, flags: dict[str, str], kwargs_name: str
) -> str:
    node_class = node_extensions.Node.__name__
    unset_class = extensions.Unset.__name__
    runtime_flags = ",\n".join(
        f"    {flag}: {annotation} | {unset_class} = UNSET"
        for flag, annotation in flags.items()
    )
    supplied_flags = ",\n".join(f'        "{flag}": {flag}' for flag in flags)
    return (
        f"\n\ndef {function_name}(\n"
        f"    {policy.type_argument}: str | type[{node_class}],\n"
        f"    *,\n{runtime_flags},\n"
        f") -> {node_class} | None:\n"
        f"    {kwargs_name} = {{\n{supplied_flags},\n    }}\n"
        f"    return extensions.{function_name}(\n"
        f"        {policy.type_argument},\n"
        f"        **{{flag: value for flag, value in {kwargs_name}.items() "
        "if value is not UNSET},\n"
        "    )\n"
    )


def generate_command_overloads(
    function_name: str, policy: NodeReturn, flags: dict[str, str]
) -> str:
    node_class = node_extensions.Node.__name__
    if policy.nullable_flags:
        cases = [
            ("type[T]", "Literal[False]", "T"),
            ("type[T]", "bool", "T | None"),
            ("str", "bool", f"{node_class} | None"),
        ]
    else:
        cases = [("type[T]", None, "T"), ("str", None, node_class)]
    lines = []
    for argument_type, nullable_type, return_type in cases:
        stub_flags = ", ".join(
            (
                f"{flag}: {nullable_type} = False"
                if flag in policy.nullable_flags
                else f"{flag}: {annotation} = ..."
            )
            for flag, annotation in flags.items()
        )
        lines.append(
            "\n\n@overload\n"
            f"def {function_name}({policy.type_argument}: {argument_type}, *, "
            f"{stub_flags}) -> {return_type}: ...\n"
        )
    return "".join(lines)


def command_kwargs_name(function: Callable[..., Any], policy: NodeReturn) -> str:
    parameters = list(inspect.signature(function).parameters.values())
    if (
        len(parameters) != 2
        or parameters[0].name != policy.type_argument
        or parameters[0].kind != inspect.Parameter.POSITIONAL_OR_KEYWORD
        or parameters[0].default is not inspect.Parameter.empty
        or parameters[1].kind != inspect.Parameter.VAR_KEYWORD
    ):
        raise ValueError(
            f"{function.__name__}: expected a required type argument followed by **kwargs"
        )
    return parameters[1].name


def resolve_command_flags(function_name: str, policy: NodeReturn) -> dict[str, str]:
    try:
        help_text = cmds.help(function_name)
    except RuntimeError as e:
        raise MayaBrewException(
            f"Cannot query command help for {function_name}: {e}"
        ) from e
    flags = command_flags(function_name, help_text, policy.flag_types)
    unknown_flags = set(policy.nullable_flags + policy.node_arguments) - flags.keys()
    if unknown_flags:
        raise ValueError(f"{function_name}: unknown policy flags {unknown_flags}")
    for flag in policy.node_arguments:
        flags[flag] = f"str | {node_extensions.Node.__name__}"
    return flags


def generate_command_files(
    hierarchy: dict[str, NodeType], version: str
) -> dict[str, str]:
    node_class = node_extensions.Node.__name__
    runtime = [
        HEADER,
        f"from {extensions.__name__} import UNSET, {extensions.Unset.__name__}\n",
        f"from {extensions.__package__} import "
        f"{extensions.__name__.rpartition('.')[2]} as extensions\n",
        f"from {node_extensions.__name__} import {node_class}\n",
    ]
    stub = [
        HEADER,
        "from typing import Literal, TypeVar, overload\n\n",
        f"from {node_extensions.__name__} import {node_class}\n",
        f"from .{CONCRETE_NODES_MODULE} import {CONCRETE_NODE_ALIAS}\n",
        f'\nT = TypeVar("T", bound={CONCRETE_NODE_ALIAS})\n',
    ]
    command_names = []
    for function_name, function in inspect.getmembers(extensions, inspect.isfunction):
        policy = NODE_RETURNS.get(function)
        if policy is None:
            continue
        command_names.append(function_name)
        kwargs_name = command_kwargs_name(function, policy)
        flags = resolve_command_flags(function_name, policy)
        runtime.append(
            generate_command_definition(function_name, policy, flags, kwargs_name)
        )
        stub.append(generate_command_overloads(function_name, policy, flags))
    exports = (
        "\n\n__all__ = [" + ", ".join(f'"{name}"' for name in command_names) + "]\n"
    )
    runtime.append(exports)
    stub.append(exports)
    return {
        f"{_snapshot.COMMANDS_MODULE}.py": "".join(runtime),
        f"{_snapshot.COMMANDS_MODULE}.pyi": "".join(stub),
        f"{CONCRETE_NODES_MODULE}.pyi": generate_concrete_node_stub(hierarchy, version),
        "__init__.py": HEADER,
    }


def write_wrappers(hierarchy: dict[str, NodeType], version: str) -> None:
    artifacts = generate_command_files(hierarchy, version)
    package_name = _snapshot.snapshot_package_name(version)
    destination = Path(_generated.__file__).parent / package_name.rpartition(".")[2]
    destination.mkdir(exist_ok=True)
    for filename, content in artifacts.items():
        (destination / filename).write_text(content, encoding="utf-8", newline="\n")
