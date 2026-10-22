import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def pyramid():
    return cmds.polyPyramid(sideLength=2.0, numberOfSides=5, sc=2, sh=3)


@pytest.mark.parametrize(
    "flag",
    [
        "sideLength",
        "w",
        "numberOfSides",
        "ns",
        "numderOfSides",
        "nsi",
        "subdivisionsCaps",
        "sc",
        "subdivisionsHeight",
        "sh",
        "createUVs",
        "cuv",
        "texture",
        "tx",
    ],
)
@pytest.mark.parametrize("target", [0, 1])
def test_poly_pyramid_queries_match_maya(pyramid, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyPyramid(pyramid[target], **flags) == maya_cmds.polyPyramid(
        str(pyramid[target]), **flags
    )


@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize(
    "flag, value",
    [
        ("sideLength", 4.0),
        ("w", 4.0),
        ("numberOfSides", 6),
        ("ns", 6),
        ("numderOfSides", 6),
        ("nsi", 6),
        ("subdivisionsCaps", 3),
        ("sc", 3),
        ("subdivisionsHeight", 4),
        ("sh", 4),
        ("createUVs", 0),
        ("cuv", 0),
        ("texture", False),
        ("tx", False),
    ],
)
def test_poly_pyramid_edits_wrapped_target(pyramid, edit, flag, value):
    assert cmds.polyPyramid(pyramid[1], **{edit: True, flag: value}) == "Values edited."
    assert cmds.polyPyramid(pyramid[1], **{"q": True, flag: True}) == value
