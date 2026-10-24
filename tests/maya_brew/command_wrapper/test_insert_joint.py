import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.command_wrapper import insertJoint
from maya_brew.exceptions import NodeCastingException, NodeException
from maya_brew.nodes.node_types import Joint


@pytest.fixture
def chain():
    root = cmds.joint(n="root", p=(1, 0, 0))
    middle = cmds.joint(n="middle", p=(1, 4, 0))
    tip = cmds.joint(n="tip", p=(2, 8, 0))
    return root, middle, tip


@pytest.mark.parametrize(
    "target_kind", ["wrapped", "string", "list", "tuple", "selection"]
)
def test_insert_joint_wraps_result_and_preserves_hierarchy(chain, target_kind):
    root, middle, tip = chain
    position = maya_cmds.xform(str(tip), q=True, ws=True, t=True)
    target = {
        "wrapped": root,
        "string": str(root),
        "list": [root],
        "tuple": (root,),
    }.get(target_kind)
    if target_kind == "selection":
        maya_cmds.select(str(root))
        result = cmds.insertJoint()
    else:
        result = cmds.insertJoint(target)
    assert type(result) is Joint
    assert maya_cmds.listRelatives(str(result), parent=True, fullPath=True) == [
        str(root)
    ]
    assert maya_cmds.listRelatives(str(result), children=True) == ["middle"]
    assert maya_cmds.listRelatives("middle", parent=True, fullPath=True) == [
        str(result)
    ]
    assert maya_cmds.xform("tip", q=True, ws=True, t=True) == position
    assert maya_cmds.ls(selection=True, long=True) == [str(result)]


def test_insert_joint_at_leaf(chain):
    result = insertJoint(chain[-1])
    assert type(result) is Joint
    assert maya_cmds.listRelatives(str(result), parent=True, fullPath=True) == [
        str(chain[-1])
    ]
    assert maya_cmds.listRelatives(str(result), children=True) is None


def test_insert_joint_runtime_errors_are_chained():
    with pytest.raises(NodeException, match="insertJoint failed") as error:
        cmds.insertJoint()
    assert isinstance(error.value.__cause__, RuntimeError)


@pytest.fixture
def transform():
    return cmds.createNode("transform")


def test_insert_joint_rejects_wrong_node_type(monkeypatch, transform):
    monkeypatch.setattr(
        maya_cmds, "insertJoint", lambda *args, **kwargs: str(transform)
    )
    with pytest.raises(NodeCastingException, match="Expected Joint"):
        cmds.insertJoint()
