"""Generate the shared typing contract for polygon primitive commands."""

from tools.command_wrapper.modes import (
    mode_selectors,
    render_overload,
    render_typed_dict,
)


def generate_primitive_overloads(
    command: str, history_type: str, flags: dict[str, str]
) -> str:
    prefix = "_" + command[0].upper() + command[1:]
    mode_flags = f"{prefix}ModeFlags"
    create_flags = f"{prefix}CreateFlags"
    mode_parameters = {"edit", "e", "query", "q", "nodeState", "nds"}
    creation_parameters = {"constructionHistory", "ch", "object", "o"}
    mode_fields = {
        flag: annotation
        for flag, annotation in flags.items()
        if flag not in mode_parameters
    }
    create_fields = {flag: "Literal[False]" for flag in ("edit", "e", "query", "q")}
    for flag, annotation in flags.items():
        if flag not in mode_parameters | creation_parameters:
            # Axis accepts a query boolean, but creation requires a vector.
            create_fields[flag] = (
                "tuple[float, float, float]" if flag in ("axis", "ax") else annotation
            )
        elif flag in ("nodeState", "nds"):
            create_fields[flag] = annotation
    lines = [
        "\n\nfrom typing import Any, Literal, TypedDict, Unpack, overload\n",
        "from maya_brew.nodes.node_state import NodeState\n",
        f"from maya_brew.nodes.node_types import {history_type}, Transform\n",
    ]
    for name, fields in ((mode_flags, mode_fields), (create_flags, create_fields)):
        lines.append(render_typed_dict(name, fields))

    lines.extend(
        [
            generate_creation_overloads(command, history_type, create_flags),
            generate_query_overloads(command, history_type, mode_flags),
            generate_edit_overloads(command, history_type, mode_flags),
            render_overload(
                command,
                f"str | {history_type} | Transform",
                mode_flags,
                [
                    "edit: bool = False",
                    "e: bool = False",
                    "query: bool = False",
                    "q: bool = False",
                    "nodeState: int = ...",
                    "nds: int = ...",
                ],
                "Any",
            ),
        ]
    )
    return "".join(lines)


def generate_creation_overloads(
    command: str, history_type: str, flags_type: str
) -> str:
    lines = []
    for object_flag, alias in (("object", "o"), ("o", "object")):
        lines.append(
            render_overload(
                command,
                "str",
                flags_type,
                [
                    f"{object_flag}: Literal[False]",
                    f"{alias}: bool = ...",
                    "constructionHistory: bool = ...",
                    "ch: bool = ...",
                ],
                f"tuple[{history_type}]",
            )
        )
    for history_flag, alias in (
        ("constructionHistory", "ch"),
        ("ch", "constructionHistory"),
    ):
        lines.append(
            render_overload(
                command,
                "str",
                flags_type,
                [
                    f"{history_flag}: Literal[False]",
                    f"{alias}: bool = ...",
                    "object: Literal[True] = True",
                    "o: Literal[True] = True",
                ],
                "tuple[Transform]",
            )
        )
    lines.append(
        render_overload(
            command,
            "str",
            flags_type,
            [
                f"{flag}: Literal[True] = True"
                for flag in ("constructionHistory", "ch", "object", "o")
            ],
            f"tuple[Transform, {history_type}]",
        )
    )
    lines.append(
        render_overload(
            command,
            "str",
            flags_type,
            [
                f"{flag}: bool = ..."
                for flag in ("constructionHistory", "ch", "object", "o")
            ],
            f"tuple[Transform, {history_type}] | tuple[Transform] | tuple[{history_type}]",
        )
    )
    return "".join(lines)


def generate_query_overloads(command: str, history_type: str, flags_type: str) -> str:
    lines = []
    for selector in mode_selectors("query"):
        for state, state_alias in (("nodeState", "nds"), ("nds", "nodeState")):
            lines.append(
                render_overload(
                    command,
                    f"str | {history_type} | Transform",
                    flags_type,
                    [
                        selector[0],
                        f"{state}: Literal[True]",
                        *selector[1:],
                        f"{state_alias}: int = ...",
                    ],
                    "NodeState",
                )
            )
    return "".join(lines)


def generate_edit_overloads(command: str, history_type: str, flags_type: str) -> str:
    return "".join(
        render_overload(
            command,
            f"str | {history_type} | Transform",
            flags_type,
            [
                *selector,
                "nodeState: int = ...",
                "nds: int = ...",
            ],
            'Literal["Values edited."]',
        )
        for selector in mode_selectors("edit")
    )
