import ast

import pytest
from tools.command_wrapper.commands import ls as ls_generator
from tools.command_wrapper.commands.ls import (
    MAX_PRECISE_TUPLE_TYPES,
    generate_ls_overloads,
)


@pytest.fixture
def flags():
    return {
        **dict.fromkeys(
            ("type", "typ", "exactType", "et", "excludeType", "ext"),
            "str | type[Node] | Sequence[str | type[Node]]",
        ),
        **dict.fromkeys(
            (
                "uuid",
                "uid",
                "nodeTypes",
                "nt",
                "objectsOnly",
                "o",
                "showType",
                "st",
                "showNamespace",
                "sns",
                "ufeObjects",
                "ufe",
                "shapes",
                "s",
            ),
            "bool",
        ),
        "containerType": "str",
        "head": "int",
        "futureFlag": "float",
    }


@pytest.fixture
def signature(flags):
    return generate_ls_overloads("str | Node | Sequence[str | Node]", flags)


def test_generation_is_deterministic_and_valid(flags, signature):
    assert (
        generate_ls_overloads("str | Node | Sequence[str | Node]", flags) == signature
    )
    compile(signature, "ls.pyi", "exec")


def test_all_overloads_cover_resolved_flags(flags, signature):
    for statement in ast.parse(signature).body:
        if not isinstance(statement, ast.FunctionDef):
            continue
        assert statement.args.kwarg is None
        fields = {}
        for arg in statement.args.kwonlyargs:
            assert arg.annotation is not None
            fields[arg.arg] = ast.unparse(arg.annotation)
        assert fields.keys() == flags.keys()
        assert fields["futureFlag"] == "float"
        assert statement.returns is not None
        result = ast.unparse(statement.returns)
        if "_LsNodeT" in result:
            assert fields["shapes"] == "Literal[False]"
            assert fields["containerType"] == "Never"
        else:
            assert fields["shapes"] == "bool"
        if result == "list[Node]" or ("_LsNodeT" in result and "str" not in result):
            for flag in (
                "uuid",
                "uid",
                "nodeTypes",
                "nt",
                "showType",
                "st",
                "showNamespace",
                "sns",
                "ufeObjects",
                "ufe",
            ):
                assert fields[flag] == "Literal[False]"


def test_each_class_filter_alias_preserves_the_node_type(signature):
    selectors = []
    for statement in ast.parse(signature).body:
        if not isinstance(statement, ast.FunctionDef):
            continue
        assert statement.returns is not None
        result = ast.unparse(statement.returns)
        if "_LsNodeT" not in result:
            continue
        required = {
            arg.arg
            for arg, default in zip(
                statement.args.kwonlyargs, statement.args.kw_defaults
            )
            if default is None
        }
        selectors.append((required, result))
    for flag in ("type", "typ", "exactType", "et"):
        assert ({flag}, "list[_LsNodeT | str]") in selectors
        assert ({flag}, "list[_LsNodeT]") in selectors
        for size in range(1, MAX_PRECISE_TUPLE_TYPES + 1):
            node_types = " | ".join(f"_LsNodeT{i}" for i in range(1, size + 1))
            assert ({flag}, f"list[{node_types}]") in selectors
            assert ({flag}, f"list[{node_types} | str]") in selectors
    assert len(selectors) == 8 * (MAX_PRECISE_TUPLE_TYPES + 1)


def test_generic_filters_use_qualified_classes_and_nonempty_tuples(signature):
    assert "import builtins\n" in signature
    expected_filters = {
        "builtins.type[_LsNodeT] | "
        "tuple[builtins.type[_LsNodeT], *tuple[builtins.type[_LsNodeT], ...]]":
        "_LsNodeT",
    }
    for size in range(1, MAX_PRECISE_TUPLE_TYPES + 1):
        variables = [f"_LsNodeT{i}" for i in range(1, size + 1)]
        classes = ", ".join(f"builtins.type[{name}]" for name in variables)
        expected_filters[f"tuple[{classes}]"] = " | ".join(variables)
    for statement in ast.parse(signature).body:
        if not isinstance(statement, ast.FunctionDef):
            continue
        assert statement.returns is not None
        if "_LsNodeT" not in ast.unparse(statement.returns):
            continue
        fields = {}
        for arg in statement.args.kwonlyargs:
            assert arg.annotation is not None
            fields[arg.arg] = ast.unparse(arg.annotation)
        for flag in ("type", "typ", "exactType", "et"):
            assert fields[flag] in expected_filters
            assert fields[flag] == fields["type"]
        node_types = expected_filters[fields["type"]]
        assert ast.unparse(statement.returns) in (
            f"list[{node_types}]",
            f"list[{node_types} | str]",
        )


def test_precise_overloads_precede_the_generic_fallback(signature):
    precise_lines = []
    fallback_lines = []
    for statement in ast.parse(signature).body:
        if not isinstance(statement, ast.FunctionDef):
            continue
        assert statement.returns is not None
        result = ast.unparse(statement.returns)
        if "_LsNodeT1" in result:
            precise_lines.append(statement.lineno)
        if result in ("list[_LsNodeT]", "list[_LsNodeT | str]"):
            fallback_lines.append(statement.lineno)
    assert max(precise_lines) < min(fallback_lines)


def test_each_tuple_position_has_a_node_bound_type_variable(signature):
    for name in ["_LsNodeT"] + [
        f"_LsNodeT{i}" for i in range(1, MAX_PRECISE_TUPLE_TYPES + 1)
    ]:
        assert f'{name} = TypeVar("{name}", bound=Node)' in signature


def test_tuple_precision_limit_is_configurable(flags, monkeypatch):
    monkeypatch.setattr(ls_generator, "MAX_PRECISE_TUPLE_TYPES", 3)
    signature = generate_ls_overloads("str", flags)
    assert '_LsNodeT3 = TypeVar("_LsNodeT3", bound=Node)' in signature
    assert "_LsNodeT4" not in signature
    overloads = [
        statement
        for statement in ast.parse(signature).body
        if isinstance(statement, ast.FunctionDef)
    ]
    assert len(overloads) == 8 * (3 + 1) + 7


def test_optional_version_flags_are_not_invented(flags):
    del flags["ufeObjects"]
    del flags["ufe"]
    signature = generate_ls_overloads("str", flags)
    assert "ufe" not in signature


