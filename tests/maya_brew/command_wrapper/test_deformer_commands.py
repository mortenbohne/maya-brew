from dataclasses import dataclass
from typing import Any

import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.command_wrapper.extensions.non_linear import NonLinearType
from maya_brew.exceptions import (
    NodeCastingException,
    NodeException,
)
from maya_brew.nodes import node_types


@dataclass(frozen=True)
class DeformerCase:
    command: str
    wrapper_type: type
    query_flag: str
    edit_flag: str
    edit_value: Any


CASES = (
    DeformerCase("blendShape", node_types.BlendShape, "envelope", "envelope", 0.75),
    DeformerCase("cluster", node_types.Cluster, "envelope", "envelope", 0.5),
    DeformerCase("deltaMush", node_types.DeltaMush, "envelope", "envelope", 0.4),
    DeformerCase("lattice", node_types.Ffd, "divisions", "divisions", (2, 3, 4)),
    DeformerCase("nonLinear", node_types.NonLinear, "geometry", "geometry", "pSphereShape1"),
    DeformerCase(
        "proximityWrap",
        node_types.ProximityWrap,
        "freeDriverIndex",
        "applyUserDefaults",
        True,
    ),
    DeformerCase("sculpt", node_types.Sculpt, "mode", "mode", "flip"),
    DeformerCase("skinCluster", node_types.SkinCluster, "skinMethod", "skinMethod", 1),
    DeformerCase("softMod", node_types.SoftMod, "envelope", "envelope", 0.5),
    DeformerCase("wire", node_types.Wire, "envelope", "envelope", 0.7),
)


@pytest.fixture(params=[pytest.param(case, id=case.command) for case in CASES])
def case(request):
    return request.param


@pytest.fixture
def created_node(case):
    mesh = cmds.polySphere()[0]
    if case.command == "blendShape":
        return cmds.blendShape(mesh, mesh), case.wrapper_type
    if case.command == "cluster":
        return cmds.cluster(mesh), case.wrapper_type
    if case.command == "deltaMush":
        return cmds.deltaMush(mesh), case.wrapper_type
    if case.command == "lattice":
        return cmds.lattice(mesh), case.wrapper_type
    if case.command == "nonLinear":
        return cmds.nonLinear(mesh, type="bend"), case.wrapper_type
    if case.command == "proximityWrap":
        driver = cmds.polyCube(name="driver_mesh")[0]
        cmds.polyCube(name="driver_extra")
        return cmds.proximityWrap(driver, mesh), case.wrapper_type
    if case.command == "sculpt":
        return cmds.sculpt(mesh), case.wrapper_type
    if case.command == "skinCluster":
        root = cmds.joint(name="joint_root")
        maya_cmds.select(clear=True)
        tip = cmds.joint(name="joint_tip", p=(0, 2, 0))
        maya_cmds.select(clear=True)
        return cmds.skinCluster([root, tip], mesh, skinMethod=0), case.wrapper_type
    if case.command == "softMod":
        return cmds.softMod(mesh), case.wrapper_type
    curve = maya_cmds.curve(degree=1, point=[(0.0, 0.0, 0.0), (0.0, 2.0, 0.0)])
    return cmds.wire(mesh, wire=curve), case.wrapper_type


def creation_args(command: str) -> tuple[Any, ...]:
    if command == "blendShape":
        return ("source", "target")
    if command == "cluster":
        return ("target",)
    if command == "nonLinear":
        return ("target",)
    if command == "skinCluster":
        return ("joint1", "target")
    if command == "proximityWrap":
        return ("driver", "target")
    return ("target",)


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
    actual = command(node, q=True, **{case.query_flag: True})
    expected_query = native(str(node), q=True, **{case.query_flag: True})
    if case.command == "wire":
        assert actual == pytest.approx(expected_query)
        return
    assert actual == expected_query


@pytest.mark.parametrize(
    "command, expected",
    [
        ("blendShape", "Expected BlendShape"),
        ("cluster", "Expected Cluster"),
        ("deltaMush", "Expected DeltaMush"),
        ("lattice", "Expected Ffd"),
        ("nonLinear", "Expected NonLinear"),
        ("proximityWrap", "Expected ProximityWrap"),
        ("sculpt", "Expected Sculpt"),
        ("skinCluster", "Expected SkinCluster"),
        ("softMod", "Expected SoftMod"),
        ("wire", "Expected Wire"),
    ],
)
def test_deformers_reject_wrong_node_types(monkeypatch, command, expected):
    wrong_result = str(cmds.createNode("transform"))
    monkeypatch.setattr(maya_cmds, command, lambda *args, **kwargs: [wrong_result])
    with pytest.raises(NodeCastingException, match=expected):
        getattr(cmds, command)(*creation_args(command))


def test_cluster_weighted_node_requires_related_transforms() -> None:
    mesh = cmds.polySphere()[0]
    cluster_node = cmds.cluster(mesh)
    first = cmds.createNode("transform", n="cluster_weighted_a")
    second = cmds.createNode("transform", n="cluster_weighted_b")
    assert first is not None
    assert second is not None

    with pytest.raises(
        NodeException,
        match="cluster weightedNode expects related parent/child transforms",
    ) as error:
        cmds.cluster(cluster_node, e=True, weightedNode=(first, second))

    assert isinstance(error.value.__cause__, NodeException)
    assert isinstance(error.value.__cause__.__cause__, RuntimeError)
    assert "Transforms not related in hierarchy." in str(error.value.__cause__)


def test_non_linear_type_accepts_enum_and_single_item_sequences() -> None:
    mesh = cmds.polySphere()[0]
    assert type(cmds.nonLinear(mesh, type=NonLinearType.BEND)) is node_types.NonLinear
    assert type(cmds.nonLinear(mesh, typ=[NonLinearType.FLARE])) is node_types.NonLinear
    assert type(cmds.nonLinear(mesh, type=["sine"])) is node_types.NonLinear


def test_non_linear_type_rejects_multi_value_sequences() -> None:
    mesh = cmds.polySphere()[0]
    with pytest.raises(NodeException, match="expects exactly one type value"):
        cmds.nonLinear(mesh, type=["bend", "twist"])


