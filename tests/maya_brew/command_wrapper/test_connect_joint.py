import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.command_wrapper import connectJoint, extensions
from maya_brew.exceptions import NodeException


@pytest.fixture
def chains():
    root = cmds.joint(n="root")
    middle = cmds.joint(n="middle", p=(0, 4, 0))
    tip = cmds.joint(n="tip", p=(1, 8, 0))
    maya_cmds.select(clear=True)
    other = cmds.joint(n="other", p=(5, 4, 0))
    child = cmds.joint(n="other_child", p=(5, 8, 0))
    return root, middle, tip, other, child


@pytest.mark.parametrize("mode", [None, "parentMode", "pm", "connectMode", "cm"])
@pytest.mark.parametrize(
    "targets", ["wrapped", "strings", "list", "tuple", "mixed", "selection"]
)
def test_connect_joint_preserves_maya_parenting(chains, mode, targets):
    _, middle, tip, other, child = chains
    flags = {} if mode is None else {mode: True}
    arguments = {
        "wrapped": (other, tip),
        "strings": (str(other), str(tip)),
        "list": ([other, tip],),
        "tuple": ((other, tip),),
        "mixed": ([other], str(tip)),
    }
    offset = maya_cmds.getAttr(f"{child}.translate")
    if targets == "selection":
        maya_cmds.select(str(other), str(tip))
        result = cmds.connectJoint(**flags)
    else:
        result = cmds.connectJoint(*arguments[targets], **flags)
    assert result is None
    parent = tip if mode in ("parentMode", "pm") else middle
    assert maya_cmds.listRelatives("other", parent=True, fullPath=True) == [str(parent)]
    assert maya_cmds.getAttr("other_child.translate") == offset


def test_connect_joint_runtime_errors_are_chained():
    with pytest.raises(NodeException, match="connectJoint failed") as error:
        cmds.connectJoint()
    assert isinstance(error.value.__cause__, RuntimeError)


def test_connect_joint_omitted_flags_are_not_forwarded(monkeypatch):
    calls = []

    def record_call(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(extensions, "connectJoint", record_call)
    connectJoint(parentMode=False)
    assert calls == [((), {"parentMode": False})]
