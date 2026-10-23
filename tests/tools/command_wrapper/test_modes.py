import ast

import pytest
from tools.command_wrapper.modes import mode_selectors, render_overload
from tools.command_wrapper.primitive import (
    generate_creation_overloads,
    generate_edit_overloads,
    generate_query_overloads,
)


@pytest.mark.parametrize(
    "mode, aliases", [("query", ("query", "q")), ("edit", ("edit", "e"))]
)
def test_mode_selectors_cover_both_aliases(mode, aliases):
    selectors = mode_selectors(mode)
    assert len(selectors) == 2
    for selector, alias in zip(selectors, aliases):
        assert selector[0] == f"{alias}: Literal[True]"
        assert len(selector) == 4


def test_edit_selectors_exclude_query_mode():
    for selector in mode_selectors("edit"):
        assert "query: Literal[False] = False" in selector
        assert "q: Literal[False] = False" in selector


def test_renderer_does_not_assume_primitive_targets_or_returns():
    source = render_overload(
        "example", "str", "ExampleFlags", mode_selectors("query")[0], "float"
    )
    function = ast.parse(source).body[0]
    assert ast.unparse(function.args.vararg.annotation) == "str"
    assert ast.unparse(function.returns) == "float"
    assert ast.unparse(function.args.kwarg.annotation) == "Unpack[ExampleFlags]"


@pytest.mark.parametrize(
    "generator, count, returns",
    [
        (
            generate_creation_overloads,
            6,
            {
                "tuple[PolyCube]",
                "tuple[Transform]",
                "tuple[Transform, PolyCube]",
                "tuple[Transform, PolyCube] | tuple[Transform] | tuple[PolyCube]",
            },
        ),
        (generate_query_overloads, 4, {"NodeState"}),
        (generate_edit_overloads, 2, {"Literal['Values edited.']"}),
    ],
)
def test_primitive_modes_keep_command_specific_returns(generator, count, returns):
    functions = ast.parse(generator("polyCube", "PolyCube", "Flags")).body
    assert len(functions) == count
    assert {ast.unparse(function.returns) for function in functions} == returns
