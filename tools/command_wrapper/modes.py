"""Shared signature rendering and Maya query/edit mode selectors."""

from typing import Literal


def mode_selectors(mode: Literal["query", "edit"]) -> list[list[str]]:
    if mode == "query":
        return [
            [
                f"{query}: Literal[True]",
                "edit: bool = False",
                "e: bool = False",
                f"{alias}: bool = ...",
            ]
            for query, alias in (("query", "q"), ("q", "query"))
        ]
    return [
        [
            f"{edit}: Literal[True]",
            f"{alias}: bool = False",
            "query: Literal[False] = False",
            "q: Literal[False] = False",
        ]
        for edit, alias in (("edit", "e"), ("e", "edit"))
    ]


def render_overload(
    command: str,
    argument_type: str,
    flags_type: str,
    parameters: list[str],
    return_type: str,
) -> str:
    return "".join(
        [
            f"\n@overload\ndef {command}(\n",
            f"    *args: {argument_type},\n",
            *(f"    {parameter},\n" for parameter in parameters),
            f"    **kwargs: Unpack[{flags_type}],\n",
            f") -> {return_type}: ...\n",
        ]
    )
