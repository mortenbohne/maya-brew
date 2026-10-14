import ast
from pathlib import Path
from typing import get_type_hints

import pytest
from maya_brew.command_wrapper import extensions
from maya_brew.nodes._foundation.native_node_hierarchy import NodeType
from tools.command_wrapper import generate
from tools.command_wrapper.metadata import COMMANDS


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


@pytest.fixture
def handwritten_signature():
    return (
        Path(generate.__file__).with_name("signatures")
        / f"{extensions.polyPlane.__name__}.pyi"
    ).read_text(encoding="utf-8")


def test_handwritten_signature_is_in_generated_stub(artifacts, handwritten_signature):
    assert handwritten_signature in artifacts["commands.pyi"]


def signature_flag_names(signature):
    statements = ast.parse(signature).body
    flag_groups = {
        node.name: {
            field.target.id
            for field in node.body
            if isinstance(field, ast.AnnAssign) and isinstance(field.target, ast.Name)
        }
        for node in statements
        if isinstance(node, ast.ClassDef)
    }
    for definition in statements:
        if not isinstance(definition, ast.FunctionDef):
            continue
        declared_flags = {argument.arg for argument in definition.args.kwonlyargs}
        if definition.args.kwarg is not None:
            annotation = definition.args.kwarg.annotation
            assert isinstance(annotation, ast.Subscript)
            assert isinstance(annotation.slice, ast.Name)
            declared_flags.update(flag_groups[annotation.slice.id])
        yield definition.name, declared_flags


def test_handwritten_signature_matches_help_flags(handwritten_signature):
    function = extensions.polyPlane
    flags = generate.resolve_command_flags(function.__name__, COMMANDS[function])
    signatures = list(signature_flag_names(handwritten_signature))
    assert signatures
    for name, declared_flags in signatures:
        assert name == function.__name__
        assert declared_flags == flags.keys()
