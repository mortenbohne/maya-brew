"""Generate command signatures from Maya help and handwritten extensions."""

# @not-generated

import ast
import inspect
import keyword
from collections.abc import Callable
from pathlib import Path
from typing import Any

import maya.cmds as cmds
from maya_brew.command_wrapper import _generated, _snapshot, extensions
from maya_brew.exceptions import MayaBrewException
from maya_brew.nodes._foundation import node_extensions
from maya_brew.nodes._foundation.native_node_hierarchy import (
    NodeType,
    python_class_name,
)
from maya_brew.nodes._foundation.node_registry import snapshot_package_name
from tools.command_wrapper.help import command_flags
from tools.command_wrapper.metadata import COMMANDS, CommandMetadata
from tools.node_hierarchy.generate import CLASSES_MODULE

HEADER = "# AUTO-GENERATED; DO NOT EDIT.\n# @generated\n"
CONCRETE_NODES_MODULE = "concrete_nodes"
CONCRETE_NODE_ALIAS = "ConcreteNode"


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
    function_name: str,
    policy: CommandMetadata,
    flags: dict[str, str],
    kwargs_name: str,
    args_name: str | None,
    return_type: str,
    docstring: str | None = None,
) -> str:
    node_class = node_extensions.Node.__name__
    if args_name is None:
        signature_arguments = (
            f"    {policy.type_argument}: str | type[{node_class}],\n    *,\n"
        )
        call_arguments = f"        {policy.type_argument},\n"
    else:
        target_type = policy.target_type or (
            f"str | {node_class}" if policy.node_targets else "str"
        )
        signature_arguments = f"    *{args_name}: {target_type},\n"
        call_arguments = f"        *{args_name},\n"
    unset_class = extensions.Unset.__name__
    runtime_flags = ",\n".join(
        f"    {flag}: {annotation} | {unset_class} = UNSET"
        for flag, annotation in flags.items()
    )
    supplied_flags = ",\n".join(f'        "{flag}": {flag}' for flag in flags)
    return (
        f"\n\ndef {function_name}(\n"
        f"{signature_arguments}{runtime_flags},\n"
        f") -> {return_type}:\n"
        + (f"    {docstring!r}\n" if docstring else "")
        + f"    {kwargs_name} = {{\n{supplied_flags},\n    }}\n"
        f"    return extensions.{function_name}(\n"
        f"{call_arguments}"
        f"        **{{flag: value for flag, value in {kwargs_name}.items() "
        "if value is not UNSET},\n"
        "    )\n"
    )


def generate_command_overloads(
    function_name: str,
    policy: CommandMetadata,
    flags: dict[str, str],
    return_type: str,
) -> str:
    signature_path = Path(__file__).with_name("signatures") / f"{function_name}.pyi"
    if signature_path.is_file():
        return "\n\n" + signature_path.read_text(encoding="utf-8")
    node_class = node_extensions.Node.__name__
    if policy.type_argument is None:
        stub_flags = ", ".join(
            f"{flag}: {annotation} = ..." for flag, annotation in flags.items()
        )
        target_type = policy.target_type or (
            f"str | {node_class}" if policy.node_targets else "str"
        )
        return (
            f"\n\ndef {function_name}(*args: {target_type}, {stub_flags}) "
            f"-> {return_type}: ...\n"
        )
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


def command_parameter_names(
    function: Callable[..., Any], policy: CommandMetadata
) -> tuple[str | None, str]:
    parameters = list(inspect.signature(function).parameters.values())
    if policy.type_argument is None:
        if (
            len(parameters) != 2
            or parameters[0].kind != inspect.Parameter.VAR_POSITIONAL
            or parameters[1].kind != inspect.Parameter.VAR_KEYWORD
        ):
            raise ValueError(
                f"{function.__name__}: expected *args followed by **kwargs"
            )
        return parameters[0].name, parameters[1].name
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
    return None, parameters[1].name


def resolve_command_flags(
    function_name: str, policy: CommandMetadata
) -> dict[str, str]:
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
    return {
        flag: annotation
        for flag, annotation in flags.items()
        if not keyword.iskeyword(flag)
    }


def consolidate_stub_imports(source: str) -> str:
    imports: dict[str, set[str]] = {}
    lines = source.splitlines(keepends=True)
    for statement in ast.parse(source).body:
        if isinstance(statement, ast.ImportFrom):
            prefix = f"from {'.' * statement.level}{statement.module or ''} import "
        elif isinstance(statement, ast.Import):
            prefix = "import "
        else:
            continue
        names = imports.setdefault(prefix, set())
        for alias in statement.names:
            names.add(ast.unparse(alias))
        assert statement.end_lineno is not None
        for index in range(statement.lineno - 1, statement.end_lineno):
            lines[index] = ""
    body = "".join(lines).removeprefix(HEADER).lstrip("\n")
    import_lines = [
        prefix + ", ".join(sorted(names)) + "\n"
        for prefix, names in sorted(imports.items())
    ]
    return HEADER + "".join(import_lines) + "\n" + body


def generate_command_files(
    hierarchy: dict[str, NodeType], version: str
) -> dict[str, str]:
    node_class = node_extensions.Node.__name__
    runtime = [
        HEADER,
        "from collections.abc import Sequence\n",
        "from typing import Any\n",
        f"from {extensions.__name__} import UNSET, {extensions.Unset.__name__}\n",
        f"from {extensions.__package__} import "
        f"{extensions.__name__.rpartition('.')[2]} as extensions\n",
        f"from {node_extensions.__name__} import {node_class}\n",
    ]
    stub = [
        HEADER,
        "from collections.abc import Sequence\n",
        "from typing import Any, Literal, TypeVar, overload\n\n",
        f"from {node_extensions.__name__} import {node_class}\n",
        f"from .{CONCRETE_NODES_MODULE} import {CONCRETE_NODE_ALIAS}\n",
        f'\nT = TypeVar("T", bound={CONCRETE_NODE_ALIAS})\n',
    ]
    command_names = []
    for function, policy in sorted(COMMANDS.items(), key=lambda item: item[0].__name__):
        function_name = function.__name__
        command_names.append(function_name)
        args_name, kwargs_name = command_parameter_names(function, policy)
        return_annotation = inspect.signature(function).return_annotation
        if return_annotation is inspect.Signature.empty:
            raise ValueError(f"{function_name}: missing return annotation")
        return_type = inspect.formatannotation(return_annotation).replace(
            f"{node_extensions.__name__}.", ""
        )
        flags = resolve_command_flags(function_name, policy)
        runtime.append(
            generate_command_definition(
                function_name,
                policy,
                flags,
                kwargs_name,
                args_name,
                return_type,
                inspect.getdoc(function),
            )
        )
        stub.append(
            generate_command_overloads(function_name, policy, flags, return_type)
        )
    exports = (
        "\n\n__all__ = [" + ", ".join(f'"{name}"' for name in command_names) + "]\n"
    )
    runtime.append(exports)
    stub.append(exports)
    return {
        f"{_snapshot.COMMANDS_MODULE}.py": "".join(runtime),
        f"{_snapshot.COMMANDS_MODULE}.pyi": consolidate_stub_imports("".join(stub)),
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
