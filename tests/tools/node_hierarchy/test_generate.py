# @not-generated

import pytest
from maya_brew.nodes._foundation.native_node_hierarchy import NodeType
from tools.node_hierarchy import generate


@pytest.fixture()
def hierarchy():
    nodes = [
        NodeType("node", ("node",), abstract=True),
        NodeType("dagNode", ("node", "dagNode"), abstract=True),
        NodeType("transform", ("node", "dagNode", "transform")),
        NodeType("joint", ("node", "dagNode", "transform", "joint")),
    ]
    return {node.name: node for node in nodes}


@pytest.fixture()
def artifacts(hierarchy):
    return generate.generate_artifacts(hierarchy)


def test_generation_is_deterministic(hierarchy, artifacts):
    reversed_hierarchy = dict(reversed(list(hierarchy.items())))
    assert artifacts == generate.generate_artifacts(reversed_hierarchy)
    assert set(artifacts) == {"classes.py", "constants.py", "__init__.py"}
    assert all(content.startswith(generate.HEADER) for content in artifacts.values())
    assert artifacts["__init__.py"] == generate.HEADER


def test_generated_artifacts_compile(artifacts):
    for filename, content in artifacts.items():
        compile(content, filename, "exec")
