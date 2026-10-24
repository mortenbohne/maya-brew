import ast
import inspect
from typing import get_type_hints

import pytest
from maya_brew.command_wrapper import extensions
from maya_brew.nodes._foundation.native_node_hierarchy import NodeType
from tools.command_wrapper import generate
from tools.command_wrapper.commands.ls import MAX_PRECISE_TUPLE_TYPES
from tools.command_wrapper.metadata import (
    COMMANDS,
    CommandSignature,
    ModeSignature,
    NodeCreationSignature,
    PrimitiveSignature,
)


def test_extensions_star_import_exports_only_commands():
    namespace = {}
    exec("from maya_brew.command_wrapper.extensions import *", namespace)
    exports = {
        name: value for name, value in namespace.items() if name != "__builtins__"
    }
    assert exports == {function.__name__: function for function in COMMANDS}


@pytest.fixture
def hierarchy():
    return {
        "node": NodeType("node", ("node",), abstract=True),
        "transform": NodeType("transform", ("node", "transform")),
        "joint": NodeType("joint", ("node", "transform", "joint")),
    }


@pytest.fixture
def artifacts(hierarchy):
    return generate.generate_command_files(hierarchy, "2027")


def test_command_stub_is_deterministic(hierarchy, artifacts):
    assert set(artifacts) == {
        "commands.py",
        "commands.pyi",
        "concrete_nodes.pyi",
        "__init__.py",
    }
    assert artifacts == generate.generate_command_files(
        dict(reversed(list(hierarchy.items()))), "2027"
    )
    for filename, content in artifacts.items():
        compile(content, filename, "exec")


def test_generated_return_annotations_match_implementations(artifacts):
    namespace = {}
    exec(artifacts["commands.py"], namespace)
    for function in COMMANDS:
        assert (
            get_type_hints(namespace[function.__name__])["return"]
            == get_type_hints(function)["return"]
        )


def test_generated_commands_preserve_wrapper_docstrings(artifacts):
    namespace = {}
    exec(artifacts["commands.py"], namespace)
    for function in COMMANDS:
        assert inspect.getdoc(namespace[function.__name__]) == inspect.getdoc(function)


@pytest.fixture
def ls_signature():
    policy = COMMANDS[extensions.ls]
    flags = generate.resolve_command_flags("ls", policy)
    return generate.generate_command_overloads("ls", policy, flags, "list[Node | str]")


def test_ls_signature_is_in_generated_stub(artifacts, ls_signature):
    generated_definitions = {
        ast.dump(statement)
        for statement in ast.parse(artifacts["commands.pyi"]).body
        if isinstance(statement, (ast.ClassDef, ast.FunctionDef))
    }
    for statement in ast.parse(ls_signature).body:
        if isinstance(statement, (ast.ClassDef, ast.FunctionDef)):
            assert ast.dump(statement) in generated_definitions


def test_generated_stub_imports_are_deduplicated(artifacts):
    bindings = []
    for statement in ast.parse(artifacts["commands.pyi"]).body:
        if isinstance(statement, (ast.Import, ast.ImportFrom)):
            bindings.extend(alias.asname or alias.name for alias in statement.names)
    assert len(bindings) == len(set(bindings))


def test_stub_imports_are_consolidated():
    source = (
        generate.HEADER
        + "from typing import (\n    Literal,\n    overload,\n)\n"
        + "import collections as col\n"
        + "from .types import Node\n"
        + "value: Node\n"
        + "from typing import Literal, TypedDict\n"
        + "from .types import Node\n"
        + "import collections as col\n"
    )
    result = generate.consolidate_stub_imports(source)
    assert result == (
        generate.HEADER
        + "from .types import Node\n"
        + "from typing import Literal, TypedDict, overload\n"
        + "import collections as col\n\n"
        + "value: Node\n"
    )
    assert generate.consolidate_stub_imports(result) == result


def typed_dict_flag_names(definition, inherited_flags):
    flags = set()
    for base in definition.bases:
        assert isinstance(base, ast.Name)
        if base.id != "TypedDict":
            flags.update(inherited_flags[base.id])
    for field in definition.body:
        if isinstance(field, ast.AnnAssign):
            assert isinstance(field.target, ast.Name)
            flags.add(field.target.id)
    return flags


def signature_flag_names(signature):
    typed_dicts = {}
    for definition in ast.parse(signature).body:
        if isinstance(definition, ast.ClassDef):
            typed_dicts[definition.name] = typed_dict_flag_names(
                definition, typed_dicts
            )
        elif isinstance(definition, ast.FunctionDef):
            flags = {argument.arg for argument in definition.args.kwonlyargs}
            kwargs = definition.args.kwarg
            if kwargs is not None:
                # **kwargs: Unpack[SomeFlags] contributes SomeFlags' fields.
                unpack = kwargs.annotation
                assert isinstance(unpack, ast.Subscript)
                assert isinstance(unpack.value, ast.Name)
                assert unpack.value.id == "Unpack"
                assert isinstance(unpack.slice, ast.Name)
                flags.update(typed_dicts[unpack.slice.id])
            yield definition.name, flags


def test_ls_signature_matches_help_flags(ls_signature):
    flags = generate.resolve_command_flags("ls", COMMANDS[extensions.ls])
    signatures = list(signature_flag_names(ls_signature))
    assert len(signatures) == 8 * (MAX_PRECISE_TUPLE_TYPES + 1) + 7
    for name, declared_flags in signatures:
        assert name == "ls"
        assert declared_flags == flags.keys()


@pytest.mark.parametrize(
    "function, count",
    [(extensions.joint, 4), (extensions.ikHandle, 2), (extensions.ikSolver, 2)],
    ids=["joint", "ikHandle", "ikSolver"],
)
def test_mode_signatures_match_help_flags(function, count):
    policy = COMMANDS[function]
    assert isinstance(policy, ModeSignature)
    name = function.__name__
    flags = generate.resolve_command_flags(name, policy)
    signature = generate.generate_command_overloads(
        name,
        policy,
        flags,
        "Any",
        generate.resolve_command_flags(name, policy, creation=True),
    )
    signatures = list(signature_flag_names(signature))
    assert len(signatures) == count
    for command, declared_flags in signatures:
        assert command == name
        assert declared_flags == flags.keys()


@pytest.mark.parametrize(
    "function, flag, alias, creation_type",
    [
        (
            extensions.joint,
            "position",
            "p",
            "tuple[float | str, float | str, float | str]",
        ),
        (extensions.joint, "angleX", "ax", "float | str"),
        (extensions.ikHandle, "startJoint", "sj", "str | Node"),
        (extensions.ikSolver, "solverType", "st", "str"),
    ],
)
def test_queryable_flag_aliases_have_explicit_creation_types(
    function, flag, alias, creation_type
):
    policy = COMMANDS[function]
    creation = generate.resolve_command_flags(function.__name__, policy, creation=True)
    modes = generate.resolve_command_flags(function.__name__, policy)
    assert creation[flag] == creation[alias] == creation_type
    assert modes[flag] == modes[alias] == f"{creation_type} | bool"


@pytest.fixture(
    params=[
        function
        for function, policy in COMMANDS.items()
        if isinstance(policy, PrimitiveSignature)
    ],
    ids=lambda function: function.__name__,
)
def primitive_signature(request):
    function = request.param
    policy = COMMANDS[function]
    flags = generate.resolve_command_flags(function.__name__, policy)
    return (
        generate.generate_command_overloads(function.__name__, policy, flags, "Any"),
        function,
        flags,
    )


def test_primitive_signatures_match_help_flags(primitive_signature):
    signature, function, flags = primitive_signature
    signatures = list(signature_flag_names(signature))
    assert len(signatures) == 13
    for name, declared_flags in signatures:
        assert name == function.__name__
        assert declared_flags == flags.keys()


def test_primitive_creation_axis_requires_vector(primitive_signature):
    signature, _, _ = primitive_signature
    definitions = {
        statement.name: statement
        for statement in ast.parse(signature).body
        if isinstance(statement, ast.ClassDef)
    }
    for name, definition in definitions.items():
        fields = {
            field.target.id: ast.unparse(field.annotation)
            for field in definition.body
            if isinstance(field, ast.AnnAssign)
        }
        expected = "tuple[float, float, float]"
        if name.endswith("ModeFlags"):
            expected += " | bool"
        if {"axis", "ax"} <= fields.keys():
            assert fields["axis"] == fields["ax"] == expected


def test_python_keyword_flag_aliases_are_omitted():
    flags = generate.resolve_command_flags("ls", COMMANDS[extensions.ls])
    assert "assemblies" in flags
    assert "as" not in flags


def test_regular_signature_uses_argument_type():
    signature = generate.generate_command_overloads(
        "example", CommandSignature(argument_type="str | Node"), {"name": "str"}, "Any"
    )
    assert "def example(*args: str | Node, name: str = ...) -> Any" in signature


def test_flagless_signature_has_no_trailing_parameter_separator():
    signature = generate.generate_command_overloads(
        "example", CommandSignature(argument_type="str | Node"), {}, "None"
    )
    assert "def example(*args: str | Node) -> None" in signature
    compile(signature, "example.pyi", "exec")


def test_primitive_defaults_preserve_custom_overrides():
    flags = generate.resolve_command_flags(
        "polyTorus",
        PrimitiveSignature(
            history_type="PolyTorus", flag_type_overrides={"twist": "float"}
        ),
    )
    assert flags["axis"] == flags["ax"] == "tuple[float, float, float] | bool"
    assert flags["twist"] == flags["tw"] == "float"


def test_node_creation_flags_accept_nodes():
    flags = generate.resolve_command_flags(
        "createNode", COMMANDS[extensions.createNode]
    )
    assert flags["parent"] == flags["p"] == "str | Node"


@pytest.mark.parametrize(
    "signature",
    [
        NodeCreationSignature(type_argument="node_type", node_flags=("missing",)),
        NodeCreationSignature(
            type_argument="node_type", nullable_return_flags=("missing",)
        ),
    ],
)
def test_unknown_node_creation_flags_are_rejected(signature):
    with pytest.raises(ValueError, match="unknown policy flags"):
        generate.resolve_command_flags("createNode", signature)
