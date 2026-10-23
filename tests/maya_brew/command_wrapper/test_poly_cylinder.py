import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def cylinder():
    return cmds.polyCylinder(radius=2.0, height=3.0, sx=8, sy=2, sz=1)


@pytest.mark.parametrize(
    "flag",
    [
        "radius",
        "r",
        "height",
        "h",
        "roundCap",
        "rcp",
        "roundCapHeightCompensation",
        "rch",
        "subdivisionsAxis",
        "sa",
        "subdivisionsCaps",
        "sc",
        "subdivisionsHeight",
        "sh",
        "subdivisionsX",
        "sx",
        "subdivisionsY",
        "sy",
        "subdivisionsZ",
        "sz",
        "createUVs",
        "cuv",
        "texture",
        "tx",
    ],
)
@pytest.mark.parametrize("target", [0, 1])
def test_poly_cylinder_queries_match_maya(cylinder, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyCylinder(cylinder[target], **flags) == maya_cmds.polyCylinder(
        str(cylinder[target]), **flags
    )


@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize(
    "flag, value",
    [
        ("radius", 4.0),
        ("r", 4.0),
        ("height", 5.0),
        ("h", 5.0),
        ("roundCap", True),
        ("rcp", True),
        ("roundCapHeightCompensation", False),
        ("rch", False),
        ("subdivisionsAxis", 10),
        ("sa", 10),
        ("subdivisionsCaps", 2),
        ("sc", 2),
        ("subdivisionsHeight", 3),
        ("sh", 3),
        ("subdivisionsX", 10),
        ("sx", 10),
        ("subdivisionsY", 3),
        ("sy", 3),
        ("subdivisionsZ", 2),
        ("sz", 2),
        ("createUVs", 0),
        ("cuv", 0),
        ("texture", 1),
        ("tx", 1),
    ],
)
def test_poly_cylinder_edits_wrapped_target(cylinder, edit, flag, value):
    assert (
        cmds.polyCylinder(cylinder[1], **{edit: True, flag: value}) == "Values edited."
    )
    assert cmds.polyCylinder(cylinder[1], **{"q": True, flag: True}) == value
