from maya_brew.nodes._foundation.native_node_hierarchy import NodeType
from tools.command_wrapper import generate


def test_command_stub_is_deterministic():
    hierarchy = {
        "node": NodeType("node", ("node",), abstract=True),
        "transform": NodeType("transform", ("node", "transform")),
        "joint": NodeType("joint", ("node", "transform", "joint")),
    }
    artifacts = generate.generate_command_files(hierarchy, "2027")
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


def test_help_flags_and_aliases():
    assert generate.command_flags(
        "createNode", "  -n -name String\n  -s -shared\n", {}
    ) == {"name": "str", "n": "str", "shared": "bool", "s": "bool"}


def test_flag_overrides_complete_help():
    assert generate.command_flags(
        "example",
        "  -v -value Unsupported\n",
        {"value": "tuple[float, float]", "extra": "str"},
    ) == {
        "value": "tuple[float, float]",
        "v": "tuple[float, float]",
        "extra": "str",
    }


def test_unsupported_help_type_requires_override():
    with pytest.raises(ValueError, match="flag_types"):
        generate.command_flags("example", "  -v -value Unsupported\n", {})


import pytest
