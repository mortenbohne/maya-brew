from dataclasses import dataclass
from unittest.mock import Mock

import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.exceptions import NodeException


@dataclass(frozen=True)
class ErrorCase:
    command: str


CASES = (
    ErrorCase("ikHandleDisplayScale"),
    ErrorCase("ikSystemInfo"),
    ErrorCase("jointDisplayScale"),
    ErrorCase("ambientLight"),
    ErrorCase("blendShape"),
    ErrorCase("deltaMush"),
    ErrorCase("directionalLight"),
    ErrorCase("lattice"),
    ErrorCase("pointLight"),
    ErrorCase("proximityWrap"),
    ErrorCase("sculpt"),
    ErrorCase("skinCluster"),
    ErrorCase("softMod"),
    ErrorCase("spotLight"),
    ErrorCase("spaceLocator"),
    ErrorCase("wire"),
)


@pytest.mark.parametrize(
    "case", [pytest.param(case, id=case.command) for case in CASES]
)
def test_runtime_errors_are_chained(monkeypatch, case):
    error = RuntimeError("invalid target")
    monkeypatch.setattr(maya_cmds, case.command, Mock(side_effect=error))
    with pytest.raises(NodeException, match=f"{case.command} failed") as caught:
        getattr(cmds, case.command)(q=True)
    assert caught.value.__cause__ is error
