from dataclasses import dataclass
from typing import Any

import pytest
from maya_brew import command_wrapper
from maya_brew.command_wrapper import extensions


@dataclass(frozen=True)
class ForwardCase:
    command: str
    args: tuple[Any, ...]
    kwargs: dict[str, Any]


CASES = (
    ForwardCase("connectJoint", (), {"parentMode": False}),
    ForwardCase("CreateJiggleDeformer", (), {}),
    ForwardCase("CreateWrap", (), {}),
    ForwardCase("ikSolver", (), {"st": "ikSCsolver", "ep": 0.0, "query": False}),
    ForwardCase(
        "joint", (), {"name": "supplied", "scaleCompensate": False, "query": False}
    ),
    ForwardCase(
        "ikHandle", (), {"name": "supplied", "createCurve": False, "query": False}
    ),
    ForwardCase("mirrorJoint", (), {"mirrorBehavior": False, "sr": ("left", "right")}),
    ForwardCase("insertJoint", ("root",), {}),
    ForwardCase("lattice", ("target",), {"divisions": (2, 3, 4), "query": False}),
    ForwardCase("removeJoint", ("middle",), {}),
    ForwardCase("proximityWrap", ("driver", "target"), {"query": False}),
    ForwardCase("sculpt", ("target",), {"mode": "flip", "query": False}),
    ForwardCase("softMod", ("target",), {"envelope": 0.5, "query": False}),
    ForwardCase("wire", ("target",), {"envelope": 0.75, "query": False}),
)


@pytest.mark.parametrize(
    "case", [pytest.param(case, id=case.command) for case in CASES]
)
def test_wrapper_forwards_only_supplied_arguments(monkeypatch, case):
    calls: list[tuple[tuple[Any, ...], dict[str, Any]]] = []

    def record_call(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(extensions, case.command, record_call)
    getattr(command_wrapper, case.command)(*case.args, **case.kwargs)
    assert calls == [(case.args, case.kwargs)]
