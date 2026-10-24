import ast

import pytest
from tools.command_wrapper.metadata import ModeSignature
from tools.command_wrapper.mode_command import generate_mode_overloads
from tools.command_wrapper.modes import render_typed_dict


@pytest.fixture
def signature():
    flags = {
        "edit": "bool",
        "e": "bool",
        "query": "bool",
        "q": "bool",
        "enabled": "bool",
        "en": "bool",
        "name": "str | bool",
        "n": "str | bool",
        "exists": "str | bool",
        "ex": "str | bool",
    }
    creation = {**flags, "name": "str", "n": "str"}
    return generate_mode_overloads(
        "example",
        ModeSignature(
            creation_return_type="Joint",
            node_imports=("Joint",),
            presence_flags=("exists", "ex"),
            presence_return_type="bool",
        ),
        flags,
        creation,
    )


def test_shared_fields_preserve_boolean_creation_flags(signature):
    definitions = {
        definition.name: definition
        for definition in ast.parse(signature).body
        if isinstance(definition, ast.ClassDef)
    }
    fields = {
        name: {
            field.target.id: ast.unparse(field.annotation)
            for field in definition.body
            if isinstance(field, ast.AnnAssign)
        }
        for name, definition in definitions.items()
    }
    assert fields["_ExampleFlags"] == {"enabled": "bool", "en": "bool"}
    assert fields["_ExampleCreateFlags"] == {
        "edit": "Literal[False]",
        "e": "Literal[False]",
        "query": "Literal[False]",
        "q": "Literal[False]",
        "name": "str",
        "n": "str",
    }
    assert fields["_ExampleModeFlags"] == {
        "edit": "bool",
        "e": "bool",
        "query": "bool",
        "q": "bool",
        "name": "str | bool",
        "n": "str | bool",
    }
    for name in ("_ExampleCreateFlags", "_ExampleModeFlags"):
        assert ast.unparse(definitions[name].bases[0]) == "_ExampleFlags"


def test_presence_aliases_each_get_a_required_boolean_overload(signature):
    overloads = [
        statement
        for statement in ast.parse(signature).body
        if isinstance(statement, ast.FunctionDef)
    ]
    returns = []
    for overload in overloads:
        assert isinstance(overload.returns, ast.Name)
        returns.append(overload.returns.id)
    assert returns == ["Joint", "bool", "bool", "Any"]
    for argument in overloads[0].args.kwonlyargs:
        assert isinstance(argument.annotation, ast.Name)
        assert argument.annotation.id == "Never"
    for overload, required in zip(overloads[1:3], ("exists", "ex")):
        parameters = dict(
            zip(
                (argument.arg for argument in overload.args.kwonlyargs),
                overload.args.kw_defaults,
            )
        )
        required_parameters = {
            name for name, default in parameters.items() if default is None
        }
        assert required_parameters == {required}


def test_empty_typed_dict_is_valid():
    source = render_typed_dict("Empty", {})
    compile(source, "empty.pyi", "exec")
    assert "pass" in source


def test_mismatched_flag_sets_are_rejected():
    with pytest.raises(ValueError, match="creation and mode flags must match"):
        generate_mode_overloads("example", ModeSignature(), {"name": "str"}, {})


def test_unknown_presence_flags_are_rejected():
    with pytest.raises(ValueError, match="unknown presence flags"):
        generate_mode_overloads(
            "example", ModeSignature(presence_flags=("missing",)), {}, {}
        )
