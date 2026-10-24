from dataclasses import dataclass
from typing import Any
from unittest.mock import Mock

import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.exceptions import NodeException


@dataclass(frozen=True)
class ErrorCase:
    command: str
    args: tuple[Any, ...] = ()
    kwargs: dict[str, Any] | None = None


CASES = (
    ErrorCase("ikHandleDisplayScale", kwargs={"q": True}),
    ErrorCase("ikSystemInfo", kwargs={"q": True}),
    ErrorCase("jointDisplayScale", kwargs={"q": True}),
    ErrorCase("ambientLight", kwargs={"q": True}),
    ErrorCase("blendShape", kwargs={"q": True}),
    ErrorCase("CreateJiggleDeformer"),
    ErrorCase("CreateWrap"),
    ErrorCase("deltaMush", kwargs={"q": True}),
    ErrorCase("directionalLight", kwargs={"q": True}),
    ErrorCase("lattice", kwargs={"q": True}),
    ErrorCase("pointLight", kwargs={"q": True}),
    ErrorCase("proximityWrap", kwargs={"q": True}),
    ErrorCase("sculpt", kwargs={"q": True}),
    ErrorCase("skinCluster", kwargs={"q": True}),
    ErrorCase("softMod", kwargs={"q": True}),
    ErrorCase("spotLight", kwargs={"q": True}),
    ErrorCase("spaceLocator", kwargs={"q": True}),
    ErrorCase("wire", kwargs={"q": True}),
)


@pytest.mark.parametrize(
    "case", [pytest.param(case, id=case.command) for case in CASES]
)
def test_runtime_errors_are_chained(monkeypatch, case):
    error = RuntimeError("invalid target")
    monkeypatch.setattr(maya_cmds, case.command, Mock(side_effect=error))
    with pytest.raises(NodeException, match=f"{case.command} failed") as caught:
        getattr(cmds, case.command)(*case.args, **(case.kwargs or {}))
    assert caught.value.__cause__ is error
