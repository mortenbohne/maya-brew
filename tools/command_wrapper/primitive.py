"""Generate the shared typing contract for polygon primitive commands."""


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
        lines.append(f"\nclass {name}(TypedDict, total=False):\n")
        lines.extend(
            f"    {flag}: {annotation}\n" for flag, annotation in fields.items()
        )

    def overload(parameters: list[str], result: str, *, creation: bool = False) -> None:
        target = "str" if creation else f"str | {history_type} | Transform"
        kwargs = create_flags if creation else mode_flags
        lines.extend(
            [
                f"\n@overload\ndef {command}(\n",
                f"    *args: {target},\n",
                *(f"    {parameter},\n" for parameter in parameters),
                f"    **kwargs: Unpack[{kwargs}],\n",
                f") -> {result}: ...\n",
            ]
        )

    for object_flag, alias in (("object", "o"), ("o", "object")):
        overload(
            [
                f"{object_flag}: Literal[False]",
                f"{alias}: bool = ...",
                "constructionHistory: bool = ...",
                "ch: bool = ...",
            ],
            f"tuple[{history_type}]",
            creation=True,
        )
    for history_flag, alias in (
        ("constructionHistory", "ch"),
        ("ch", "constructionHistory"),
    ):
        overload(
            [
                f"{history_flag}: Literal[False]",
                f"{alias}: bool = ...",
                "object: Literal[True] = True",
                "o: Literal[True] = True",
            ],
            "tuple[Transform]",
            creation=True,
        )
    overload(
        [
            f"{flag}: Literal[True] = True"
            for flag in ("constructionHistory", "ch", "object", "o")
        ],
        f"tuple[Transform, {history_type}]",
        creation=True,
    )
    overload(
        [
            f"{flag}: bool = ..."
            for flag in ("constructionHistory", "ch", "object", "o")
        ],
        f"tuple[Transform, {history_type}] | tuple[Transform] | tuple[{history_type}]",
        creation=True,
    )
    for query, query_alias in (("query", "q"), ("q", "query")):
        for state, state_alias in (("nodeState", "nds"), ("nds", "nodeState")):
            overload(
                [
                    f"{query}: Literal[True]",
                    f"{state}: Literal[True]",
                    "edit: bool = False",
                    "e: bool = False",
                    f"{query_alias}: bool = ...",
                    f"{state_alias}: int = ...",
                ],
                "NodeState",
            )
    for edit, alias in (("edit", "e"), ("e", "edit")):
        overload(
            [
                f"{edit}: Literal[True]",
                f"{alias}: bool = False",
                "query: Literal[False] = False",
                "q: Literal[False] = False",
                "nodeState: int = ...",
                "nds: int = ...",
            ],
            'Literal["Values edited."]',
        )
    overload(
        [
            "edit: bool = False",
            "e: bool = False",
            "query: bool = False",
            "q: bool = False",
            "nodeState: int = ...",
            "nds: int = ...",
        ],
        "Any",
    )
    return "".join(lines)
