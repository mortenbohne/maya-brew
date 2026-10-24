import maya.cmds as maya_cmds
import pytest

from maya_brew import cmds
from maya_brew.command_wrapper import extensions, mirrorJoint
from maya_brew.exceptions import NodeException
from maya_brew.nodes.node_types import Joint, Transform


@pytest.fixture
def chain():
    root = cmds.joint(n="left_root", p=(2, 1, 3))
    middle = cmds.joint(n="left_middle", p=(2, 5, 4))
    tip = cmds.joint(n="left_tip", p=(3, 9, 5))
    cmds.joint(root, e=True, oj="xyz", sao="yup", ch=True)
    return root, middle, tip


@pytest.mark.parametrize(
    "target_kind", ["wrapped", "string", "list", "tuple", "selection"]
)
@pytest.mark.parametrize(
    "plane", ["mirrorXY", "mxy", "mirrorXZ", "mxz", "mirrorYZ", "myz"]
)
@pytest.mark.parametrize("behavior", ["mirrorBehavior", "mb"])
def test_mirror_joint_matches_maya(chain, target_kind, plane, behavior):
    root = chain[0]
    flags = {plane: True, behavior: True}
    expected = maya_cmds.mirrorJoint(str(root), **flags)
    attributes = ("translate", "rotate", "jointOrient")
    values = [
        [maya_cmds.getAttr(f"{name}.{attribute}") for attribute in attributes]
        for name in expected
    ]
    maya_cmds.delete(expected[0])
    target = {
        "wrapped": root,
        "string": str(root),
        "list": [root],
        "tuple": (root,),
    }.get(target_kind)
    if target_kind == "selection":
        maya_cmds.select(str(root))
        result = cmds.mirrorJoint(**flags)
    else:
        result = cmds.mirrorJoint(target, **flags)
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert all(type(node) is Joint for node in result)
    assert [
        [maya_cmds.getAttr(f"{node}.{attribute}") for attribute in attributes]
        for node in result
    ] == values
    assert maya_cmds.listRelatives(str(result[1]), parent=True, fullPath=True) == [
        str(result[0])
    ]


@pytest.mark.parametrize("flag", ["searchReplace", "sr"])
def test_mirror_joint_search_replace(chain, flag):
    result = mirrorJoint(chain[0], myz=True, **{flag: ("left_", "right_")})
    assert [maya_cmds.ls(str(node), shortNames=True)[0] for node in result] == [
        "right_root",
        "right_middle",
        "right_tip",
    ]


@pytest.fixture
def chain_with_attachment(chain):
    cmds.createNode("transform", parent=chain[1], name="attachment")
    return chain


def test_mirror_joint_wraps_non_joint_descendants(chain_with_attachment):
    result = cmds.mirrorJoint(chain_with_attachment[0], myz=True)
    assert len(result) == 4
    assert sum(type(node) is Joint for node in result) == 3
    assert sum(type(node) is Transform for node in result) == 1


def test_mirror_joint_runtime_errors_are_chained():
    with pytest.raises(NodeException, match="mirrorJoint failed") as error:
        cmds.mirrorJoint()
    assert isinstance(error.value.__cause__, RuntimeError)


@pytest.mark.parametrize("result", [None, "joint", [1], 1])
def test_mirror_joint_rejects_unexpected_results(monkeypatch, result):
    monkeypatch.setattr(maya_cmds, "mirrorJoint", lambda *args, **kwargs: result)
    with pytest.raises(NodeException, match="Unexpected result from mirrorJoint"):
        cmds.mirrorJoint()


def test_mirror_joint_omitted_flags_are_not_forwarded(monkeypatch):
    calls = []

    def record_call(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(extensions, "mirrorJoint", record_call)
    mirrorJoint(mirrorBehavior=False, sr=("left", "right"))
    assert calls == [((), {"mirrorBehavior": False, "sr": ("left", "right")})]
