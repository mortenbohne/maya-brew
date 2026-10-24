from dataclasses import dataclass
from typing import Any

import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.exceptions import NodeException


@dataclass(frozen=True)
class CreationCase:
    command: str
    invalid_results: tuple[Any, ...]
    kwargs: dict[str, Any]


CASES = (
    CreationCase("joint", (None, [], ["joint1"], 1), {}),
    CreationCase("ikHandle", (None, [], ["a", "b", "c", "d"], [1, 2], "h"), {}),
    CreationCase("ikSolver", (None, [], ["solver"], 1, False), {"st": "ikSCsolver"}),
    CreationCase("insertJoint", (None, [], ["joint"], 1, False), {}),
    CreationCase("mirrorJoint", (None, "joint", [1], 1), {}),
    CreationCase("ambientLight", (None, [], ["node1", "node2"], 1, False), {}),
    CreationCase("directionalLight", (None, [], ["node1", "node2"], 1, False), {}),
    CreationCase("pointLight", (None, [], ["node1", "node2"], 1, False), {}),
    CreationCase("spotLight", (None, [], ["node1", "node2"], 1, False), {}),
    CreationCase("spaceLocator", (None, "locator1", ["a", "b"], [1], 1, False), {}),
)


CASE_RESULTS = [
    pytest.param(case, result, id=f"{case.command}:{result!r}")
    for case in CASES
    for result in case.invalid_results
]


@pytest.mark.parametrize(("case", "result"), CASE_RESULTS)
def test_creation_commands_reject_unexpected_results(monkeypatch, case, result):
    monkeypatch.setattr(maya_cmds, case.command, lambda *args, **kwargs: result)
    with pytest.raises(NodeException, match=f"Unexpected result from {case.command}"):
        getattr(cmds, case.command)(**case.kwargs)
