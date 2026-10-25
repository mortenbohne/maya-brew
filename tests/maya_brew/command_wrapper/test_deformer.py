import maya.cmds as maya_cmds
import pytest

from maya_brew import cmds
from maya_brew.command_wrapper.extensions.deformer import DeformerType
from maya_brew.nodes import node_types


def test_deformer_creation_returns_wrapped_deformer_node() -> None:
    mesh = cmds.polySphere()[0]
    node = cmds.deformer(mesh, type=DeformerType.CLUSTER)
    assert type(node) is node_types.Cluster


@pytest.mark.parametrize("target_kind", ["wrapped", "string", "list", "tuple"])
def test_deformer_geometry_query_matches_maya(target_kind: str) -> None:
    mesh = cmds.polySphere()[0]
    node = cmds.deformer(mesh, type=DeformerType.CLUSTER)
    target = {
        "wrapped": node,
        "string": str(node),
        "list": [node],
        "tuple": (node,),
    }[target_kind]
    assert cmds.deformer(target, q=True, geometry=True) == maya_cmds.deformer(
        str(node), q=True, geometry=True
    )




