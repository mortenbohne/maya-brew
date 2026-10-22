import maya.cmds as cmds
import pytest
from maya_brew.command_wrapper import _snapshot
from maya_brew.command_wrapper._generated.maya_2027 import commands


def test_missing_command_snapshot_uses_latest(monkeypatch, caplog):
    # noinspection PyUnresolvedReferences
    monkeypatch.setattr(cmds, "about", lambda **kwargs: "9999")
    assert _snapshot.load_commands() is commands
    assert "using Maya 2027 command wrappers" in caplog.text


def test_command_snapshot_dependency_failure_is_raised(monkeypatch):
    failure = ModuleNotFoundError("Missing dependency", name="snapshot_dependency")

    def fail(name):
        raise failure

    monkeypatch.setattr(_snapshot.importlib, "import_module", fail)
    with pytest.raises(ModuleNotFoundError) as caught:
        _snapshot.load_commands()
    assert caught.value is failure
