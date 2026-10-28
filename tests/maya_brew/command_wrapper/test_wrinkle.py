import pytest
from maya_brew import cmds
from maya_brew.command_wrapper.extensions.wrinkle import WrinkleStyle
from maya_brew.exceptions import NodeException
from maya_brew.nodes._foundation.node_extensions import Node


def test_wrinkle_returns_wrapped_nodes() -> None:
    mesh = cmds.polySphere()[0]
    created = cmds.wrinkle(mesh)
    assert isinstance(created, tuple)
    assert created
    assert all(isinstance(node, Node) for node in created)


def test_wrinkle_accepts_style_constants() -> None:
    mesh = cmds.polySphere()[0]
    for style in (WrinkleStyle.RADIAL, WrinkleStyle.LINES):
        created = cmds.wrinkle(mesh, style=style)
        assert isinstance(created, tuple)
        assert created


def test_wrinkle_rejects_unsupported_tangential_style() -> None:
    mesh = cmds.polySphere()[0]
    with pytest.raises(NodeException, match="Invalid style specified"):
        cmds.wrinkle(mesh, style="tangential")
