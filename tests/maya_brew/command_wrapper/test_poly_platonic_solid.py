import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def platonic_solid():
    return cmds.polyPlatonicSolid(radius=2.0, solidType=1)


@pytest.mark.parametrize(
    "flag",
    [
        "radius",
        "r",
        "sideLength",
        "l",
        "solidType",
        "st",
        "createUVs",
        "cuv",
        "texture",
        "tx",
    ],
)
@pytest.mark.parametrize("target", [0, 1])
def test_poly_platonic_solid_queries_match_maya(platonic_solid, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyPlatonicSolid(
        platonic_solid[target], **flags
    ) == maya_cmds.polyPlatonicSolid(str(platonic_solid[target]), **flags)


@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize(
    "flag, value",
    [
        ("radius", 3.0),
        ("r", 3.0),
        ("sideLength", 2.0),
        ("l", 2.0),
        ("solidType", 2),
        ("st", 2),
        ("createUVs", 0),
        ("cuv", 0),
        ("texture", 0),
        ("tx", 0),
    ],
)
def test_poly_platonic_solid_edits_wrapped_target(platonic_solid, edit, flag, value):
    assert (
        cmds.polyPlatonicSolid(platonic_solid[1], **{edit: True, flag: value})
        == "Values edited."
    )
    assert cmds.polyPlatonicSolid(
        platonic_solid[1], **{"q": True, flag: True}
    ) == pytest.approx(float(value))


@pytest.fixture(
    params=[(flag, value) for flag in ("solidType", "st") for value in range(4)]
)
def selected_solid_type(request):
    flag, value = request.param
    return cmds.polyPlatonicSolid(**{flag: value}), value


def test_poly_platonic_solid_creates_selected_type(selected_solid_type):
    nodes, expected = selected_solid_type
    assert cmds.polyPlatonicSolid(nodes[1], q=True, solidType=True) == expected
