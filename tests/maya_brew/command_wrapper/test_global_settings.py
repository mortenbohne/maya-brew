import inspect
from unittest.mock import Mock

import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.exceptions import NodeException

COMMAND_FLAGS = {
    "ikHandleDisplayScale": {"query", "q"},
    "ikSystemInfo": {"query", "q", "globalSnapHandle", "gsh"},
    "jointDisplayScale": {"query", "q", "absolute", "a", "ikfk", "ik"},
}


@pytest.fixture(
    params=[
        ("ikHandleDisplayScale", {}),
        ("jointDisplayScale", {}),
        ("jointDisplayScale", {"absolute": True}),
        ("jointDisplayScale", {"a": True}),
        ("jointDisplayScale", {"ikfk": True}),
        ("jointDisplayScale", {"ik": True}),
        ("ikSystemInfo", {"globalSnapHandle": True}),
        ("ikSystemInfo", {"gsh": True}),
    ],
    ids=["handle", "joint", "absolute", "a", "ikfk", "ik", "snap", "gsh"],
)
def setting(request):
    name, flags = request.param
    native = getattr(maya_cmds, name)
    original = native(query=True, **flags)
    try:
        yield name, flags, native, getattr(cmds, name)
    finally:
        # Global display/IK settings can outlive the fresh scene fixture.
        if original is not None:
            if name == "ikSystemInfo":
                native(globalSnapHandle=original)
            else:
                native(original, **flags)


@pytest.mark.parametrize("query", ["query", "q"])
def test_queries_match_maya(setting, query):
    _, flags, native, wrapped = setting
    assert wrapped(**{query: True}, **flags) == native(**{query: True}, **flags)


@pytest.mark.parametrize("scale, snap", [(0.5, False), (2.0, True)])
def test_settings_match_maya(setting, scale, snap):
    name, flags, native, wrapped = setting
    if name == "ikSystemInfo":
        args, set_flags = (), {flag: snap for flag in flags}
    else:
        args, set_flags = (scale,), flags
    result = wrapped(*args, **set_flags)
    actual = native(q=True, **flags)
    assert wrapped(q=True, **flags) == actual
    assert result == native(*args, **set_flags)
    assert actual == native(q=True, **flags)


@pytest.fixture(params=[False, True])
def joint_scale(request):
    ikfk = request.param
    original = maya_cmds.jointDisplayScale(q=True, ikfk=ikfk)
    try:
        yield ikfk
    finally:
        maya_cmds.jointDisplayScale(original, ikfk=ikfk)


def test_joint_scale_changes_the_requested_display(joint_scale):
    cmds.jointDisplayScale(1.75, ikfk=joint_scale)
    assert maya_cmds.jointDisplayScale(q=True, ikfk=joint_scale) == pytest.approx(1.75)


@pytest.mark.parametrize(
    "name, args, flags, result",
    [
        ("ikHandleDisplayScale", (0.5,), {"q": False}, None),
        ("ikHandleDisplayScale", (), {"query": True}, 1.25),
        ("ikSystemInfo", (False,), {"globalSnapHandle": False}, None),
        ("ikSystemInfo", (True,), {"gsh": True, "q": False}, None),
        ("ikSystemInfo", (), {"query": True, "globalSnapHandle": True}, False),
        ("ikSystemInfo", (), {"q": True, "gsh": True}, True),
        ("jointDisplayScale", (2.0,), {"absolute": False, "ikfk": 0.5}, None),
        ("jointDisplayScale", (1,), {"a": True, "ik": False}, None),
        ("jointDisplayScale", (), {"q": True, "ik": True}, 1.25),
    ],
)
def test_supplied_arguments_and_results_are_preserved(
    monkeypatch, name, args, flags, result
):
    native = Mock(return_value=result)
    monkeypatch.setattr(maya_cmds, name, native)
    assert getattr(cmds, name)(*args, **flags) is result
    native.assert_called_once_with(*args, **flags)


def test_missing_joint_scale_raises_node_exception():
    with pytest.raises(NodeException, match="jointDisplayScale failed") as caught:
        cmds.jointDisplayScale()
    assert isinstance(caught.value.__cause__, RuntimeError)


@pytest.mark.parametrize("name", COMMAND_FLAGS)
def test_generated_signatures_expose_expected_flags(name):
    parameters = inspect.signature(getattr(cmds, name)).parameters.values()
    assert {
        parameter.name
        for parameter in parameters
        if parameter.kind == inspect.Parameter.KEYWORD_ONLY
    } == COMMAND_FLAGS[name]
