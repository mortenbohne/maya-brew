import ast
import inspect
from pathlib import Path
from typing import get_type_hints

import pytest
from maya_brew.command_wrapper import extensions
from maya_brew.nodes._foundation.native_node_hierarchy import NodeType
from tools.command_wrapper import generate
from tools.command_wrapper.metadata import COMMANDS


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


@pytest.fixture(
    params=[
        extensions.polyCube,
        extensions.polyCone,
        extensions.polyCylinder,
        extensions.polyHelix,
        extensions.polyPlane,
        extensions.polyPlatonicSolid,
        extensions.polyPrimitive,
        extensions.polyPrism,
        extensions.polyPyramid,
        extensions.polySphere,
        extensions.polyTorus,
        extensions.polyPipe,
        extensions.ls,
    ]
)
def handwritten_signature(request):
    function = request.param
    return (
        Path(generate.__file__).with_name("signatures") / f"{function.__name__}.pyi"
    ).read_text(encoding="utf-8"), function


def test_handwritten_signature_is_in_generated_stub(artifacts, handwritten_signature):
    signature, _ = handwritten_signature
    generated_definitions = {
        ast.dump(statement)
        for statement in ast.parse(artifacts["commands.pyi"]).body
        if isinstance(statement, (ast.ClassDef, ast.FunctionDef))
    }
    for statement in ast.parse(signature).body:
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


def test_handwritten_signature_matches_help_flags(handwritten_signature):
    signature, function = handwritten_signature
    flags = generate.resolve_command_flags(function.__name__, COMMANDS[function])
    signatures = list(signature_flag_names(signature))
    assert signatures
    for name, declared_flags in signatures:
        assert name == function.__name__
        assert declared_flags == flags.keys()


def test_python_keyword_flag_aliases_are_omitted():
    flags = generate.resolve_command_flags("ls", COMMANDS[extensions.ls])
    assert "assemblies" in flags
    assert "as" not in flags
