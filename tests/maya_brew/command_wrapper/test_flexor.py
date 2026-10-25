import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.command_wrapper.extensions.flexor import (
    FlexorDeformerCommand,
    FlexorType,
)
from maya_brew.exceptions import NodeException
from maya_brew.nodes import node_types


def test_flexor_creation_returns_flexor_shape_wrapper() -> None:
    node = cmds.flexor(
        type=FlexorType.SCULPT, deformerCommand=FlexorDeformerCommand.SCULPT
    )
    assert type(node) is node_types.FlexorShape


def test_flexor_query_list_matches_maya() -> None:
    assert cmds.flexor(q=True, l=True) == maya_cmds.flexor(q=True, l=True)


def test_flexor_rejects_non_string_type_and_deformer_command_values() -> None:
    with pytest.raises(NodeException, match="Unsupported flexor type value"):
        cmds.flexor(type=1)
    with pytest.raises(NodeException, match="Unsupported flexor deformerCommand value"):
        cmds.flexor(type=FlexorType.SCULPT, deformerCommand=1)
