import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def cone():
    return cmds.polyCone(radius=2.0, height=3.0, sx=8, sy=2, sz=1)


@pytest.mark.parametrize(
    "flag",
    [
        "radius",
        "r",
        "height",
        "h",
        "roundCap",
        "rcp",
        "subdivisionsAxis",
        "sa",
        "subdivisionsCap",
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
def test_poly_cone_queries_match_maya(cone, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyCone(cone[target], **flags) == maya_cmds.polyCone(
        str(cone[target]), **flags
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
        ("subdivisionsAxis", 10),
        ("sa", 10),
        ("subdivisionsCap", 2),
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
        ("texture", False),
        ("tx", False),
    ],
)
def test_poly_cone_edits_wrapped_target(cone, edit, flag, value):
    assert cmds.polyCone(cone[1], **{edit: True, flag: value}) == "Values edited."
    assert cmds.polyCone(cone[1], **{"q": True, flag: True}) == value
