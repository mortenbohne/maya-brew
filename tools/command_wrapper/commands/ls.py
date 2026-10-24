MAX_PRECISE_TUPLE_TYPES = 3


# Maya combines these selectors additively with type/exactType, not as intersections.
ADDITIVE_FLAGS = (
    "assemblies",
    "cameras",
    "ca",
    "containers",
    "con",
    "containerType",
    "ct",
    "dagObjects",
    "dag",
    "dependencyNodes",
    "dep",
    "geometry",
    "g",
    "lights",
    "lt",
    "materials",
    "mat",
    "planes",
    "pl",
    "partitions",
    "pr",
    "references",
    "rf",
    "renderGlobals",
    "rg",
    "renderQualities",
    "rq",
    "renderResolutions",
    "rr",
    "renderSetups",
    "rs",
    "shapes",
    "s",
    "sets",
    "set",
    "textures",
    "tex",
    "transforms",
    "tr",
)


def _render_overload(
    argument_type: str,
    flags: dict[str, str],
    required: str | None,
    return_type: str,
) -> str:
    # Explicit keywords also work in IDEs without full Unpack[TypedDict] support.
    parameters = "".join(
        f"    {flag}: {annotation}" + ("" if flag == required else " = ...") + ",\n"
        for flag, annotation in flags.items()
    )
    return (
        f"\n@overload\ndef ls(\n    *args: {argument_type},\n"
        f"{parameters}) -> {return_type}: ...\n"
    )


def generate_ls_overloads(argument_type: str, flags: dict[str, str]) -> str:
    type_flags = {flag: flags[flag] for flag in ("type", "typ", "exactType", "et")}
    string_flags = {flag: flags[flag] for flag in ("uuid", "uid", "nodeTypes", "nt")}
    object_flags = {flag: flags[flag] for flag in ("objectsOnly", "o")}
    metadata_flags = {
        flag: flags[flag]
        for flag in ("showType", "st", "showNamespace", "sns", "ufeObjects", "ufe")
        if flag in flags
    }
    additive_flags = {flag: flags[flag] for flag in ADDITIVE_FLAGS if flag in flags}
    typed_flags: dict[str, str] = {
        **flags,
        **{
            flag: "Literal[False]" if annotation == "bool" else "Never"
            for flag, annotation in additive_flags.items()
        },
    }
    # Maya's `type` keyword must not shadow the builtin in IDE annotation lookup.
    node_class = "builtins.type[_LsNodeT]"
    tuple_type_variables = [
        f"_LsNodeT{index}" for index in range(1, MAX_PRECISE_TUPLE_TYPES + 1)
    ]
    class_filters: list[tuple[str, str]] = []
    class_filter_aliases: list[tuple[str, str]] = []
    for size in range(1, MAX_PRECISE_TUPLE_TYPES + 1):
        element_types = tuple_type_variables[:size]
        alias = f"_LsClassFilter{size}"
        classes = ", ".join(f"builtins.type[{name}]" for name in element_types)
        class_filter_aliases.append((alias, f"tuple[{classes}]"))
        class_filters.append((alias, " | ".join(element_types)))
    class_filter_aliases.append(
        (
            "_LsClassFilterAny",
            "_LsClass | tuple[_LsClass, *tuple[_LsClass, ...]]",
        )
    )
    class_filters.append(("_LsClassFilterAny", "_LsNodeT"))
    node_only_flags: dict[str, str] = {
        flag: "Literal[False]" for flag in string_flags | metadata_flags
    }
    lines = [
        "\nimport builtins\n",
        "\nfrom collections.abc import Sequence\n",
        "from typing import Literal, Never, TypeAlias, TypeVar, overload\n",
        "from maya_brew.nodes._foundation.node_extensions import Node\n",
        '\n_LsNodeT = TypeVar("_LsNodeT", bound=Node)\n',
        *(
            f'{name} = TypeVar("{name}", bound=Node)\n'
            for name in tuple_type_variables
        ),
        "_LsClass: TypeAlias = builtins.type[_LsNodeT]\n",
        *(f"{name}: TypeAlias = {annotation}\n" for name, annotation in class_filter_aliases),
    ]
    for required in string_flags:
        lines.append(
            _render_overload(
                argument_type,
                flags | {required: "Literal[True]"},
                required,
                "list[str]",
            )
        )
    # Empty sequences disable Maya's type filter; only non-empty tuples can narrow.
    # Positive Maya type filters exclude components and attributes themselves.
    for filter_type, node_type in class_filters:
        filtered_flags: dict[str, str] = typed_flags | {
            flag: filter_type for flag in type_flags
        }
        for required_type in type_flags:
            lines.append(
                _render_overload(
                    argument_type,
                    filtered_flags | node_only_flags,
                    required_type,
                    f"list[{node_type}]",
                )
            )
            lines.append(
                _render_overload(
                    argument_type,
                    filtered_flags,
                    required_type,
                    f"list[{node_type} | str]",
                )
            )
    for required in object_flags:
        lines.append(
            _render_overload(
                argument_type,
                flags | node_only_flags | {required: "Literal[True]"},
                required,
                "list[Node]",
            )
        )
    lines.append(_render_overload(argument_type, flags, None, "list[Node | str]"))
    return "".join(lines)

