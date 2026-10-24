import maya.cmds as maya_cmds
import pytest

from maya_brew import cmds
from maya_brew.command_wrapper import extensions, removeJoint
from maya_brew.exceptions import NodeException


@pytest.fixture
def chain():
    root = cmds.joint(n="root")
    middle = cmds.joint(n="middle", p=(0, 4, 0))
    next_joint = cmds.joint(n="next_joint", p=(1, 8, 0))
    tip = cmds.joint(n="tip", p=(2, 12, 0))
    return root, middle, next_joint, tip


@pytest.mark.parametrize(
    "target_kind", ["wrapped", "string", "list", "tuple", "selection"]
)
def test_remove_joint_reparents_children(chain, target_kind):
    root, middle, next_joint, tip = chain
    position = maya_cmds.xform(str(tip), q=True, worldSpace=True, translation=True)
    target = {
        "wrapped": middle,
        "string": str(middle),
        "list": [middle],
        "tuple": (middle,),
    }.get(target_kind)
    if target_kind == "selection":
        maya_cmds.select(str(middle))
        result = cmds.removeJoint()
    else:
        result = cmds.removeJoint(target)
    assert result is None
    assert not maya_cmds.objExists("middle")
    assert maya_cmds.listRelatives("next_joint", parent=True, fullPath=True) == [
        str(root)
    ]
    assert maya_cmds.xform("tip", q=True, worldSpace=True, translation=True) == position


@pytest.mark.parametrize("targets", ["arguments", "list", "mixed"])
def test_remove_joint_multiple_targets(chain, targets):
    root, middle, next_joint, _ = chain
    arguments = {
        "arguments": (middle, next_joint),
        "list": ([middle, next_joint],),
        "mixed": ([middle], str(next_joint)),
    }[targets]
    assert cmds.removeJoint(*arguments) is None
    assert not maya_cmds.objExists("middle")
    assert not maya_cmds.objExists("next_joint")
    assert maya_cmds.listRelatives("tip", parent=True, fullPath=True) == [str(root)]


def test_remove_joint_runtime_errors_are_chained():
    with pytest.raises(NodeException, match="removeJoint failed") as error:
        cmds.removeJoint()
    assert isinstance(error.value.__cause__, RuntimeError)


def test_remove_joint_forwards_no_flags(monkeypatch):
    calls = []

    def record_call(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(extensions, "removeJoint", record_call)
    removeJoint("middle")
    assert calls == [(("middle",), {})]
