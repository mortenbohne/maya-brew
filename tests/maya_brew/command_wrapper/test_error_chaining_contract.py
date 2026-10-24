from unittest.mock import Mock

import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.exceptions import NodeException


@pytest.mark.parametrize(
    "name",
    [
        "ikHandleDisplayScale",
        "ikSystemInfo",
        "jointDisplayScale",
        "ambientLight",
        "directionalLight",
        "pointLight",
        "spotLight",
        "spaceLocator",
    ],
)
def test_runtime_errors_are_chained(monkeypatch, name):
    error = RuntimeError("invalid target")
    monkeypatch.setattr(maya_cmds, name, Mock(side_effect=error))
    with pytest.raises(NodeException, match=f"{name} failed") as caught:
        getattr(cmds, name)(q=True)
    assert caught.value.__cause__ is error
