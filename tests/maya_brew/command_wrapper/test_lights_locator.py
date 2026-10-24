from dataclasses import dataclass
from typing import Any

import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.exceptions import NodeCastingException, NodeException
from maya_brew.nodes import node_types


@dataclass(frozen=True)
class ModeCase:
    command: str
    wrapper_type: type
    query_flag: str
    edit_flag: str
    edit_value: Any


CASES = (
    ModeCase("ambientLight", node_types.AmbientLight, "intensity", "intensity", 0.8),
    ModeCase(
        "directionalLight", node_types.DirectionalLight, "intensity", "intensity", 0.7
    ),
    ModeCase("pointLight", node_types.PointLight, "intensity", "intensity", 0.6),
    ModeCase("spotLight", node_types.SpotLight, "coneAngle", "coneAngle", 35.0),
    ModeCase(
        "spaceLocator",
        node_types.Transform,
        "position",
        "position",
        (1.0, 2.0, 3.0),
    ),
)


@pytest.fixture(params=[pytest.param(case, id=case.command) for case in CASES])
def case(request):
    return request.param


@pytest.fixture
def created_node(case):
    return getattr(cmds, case.command)(), case.wrapper_type


def test_creation_returns_native_wrapper(created_node):
    node, wrapper = created_node
    assert type(node) is wrapper


@pytest.mark.parametrize("target_kind", ["wrapped", "string", "list", "tuple"])
def test_queries_match_maya(case, created_node, target_kind):
    node, _ = created_node
    command = getattr(cmds, case.command)
    native = getattr(maya_cmds, case.command)
    target = {
        "wrapped": node,
        "string": str(node),
        "list": [node],
        "tuple": (node,),
    }[target_kind]
    flags = {"q": True, case.query_flag: True}
    assert command(target, **flags) == native(str(node), **flags)


@pytest.mark.parametrize("mode", ["edit", "e"])
def test_edits_match_maya(case, created_node, mode):
    node, _ = created_node
    command = getattr(cmds, case.command)
    native = getattr(maya_cmds, case.command)
    expected = native(str(node), **{mode: True, case.edit_flag: case.edit_value})
    assert command(node, **{mode: True, case.edit_flag: case.edit_value}) == expected
    if case.command == "spaceLocator":
        return
    queried = native(str(node), q=True, **{case.query_flag: True})
    if isinstance(case.edit_value, tuple):
        assert queried == list(case.edit_value)
    else:
        assert queried == pytest.approx(case.edit_value)




def test_lights_reject_wrong_node_types(monkeypatch):
    wrong_result = str(cmds.createNode("transform"))
    monkeypatch.setattr(maya_cmds, "ambientLight", lambda *args, **kwargs: wrong_result)
    with pytest.raises(NodeCastingException, match="Expected AmbientLight"):
        cmds.ambientLight()
