import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def prism():
    return cmds.polyPrism(sideLength=2.0, length=3.0, numberOfSides=5, sc=2, sh=3)


@pytest.mark.parametrize(
    "flag",
    [
        "sideLength",
        "w",
        "length",
        "l",
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
def test_poly_prism_queries_match_maya(prism, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyPrism(prism[target], **flags) == maya_cmds.polyPrism(
        str(prism[target]), **flags
    )


@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize(
    "flag, value",
    [
        ("sideLength", 4.0),
        ("w", 4.0),
        ("length", 5.0),
        ("l", 5.0),
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
        ("texture", 0),
        ("tx", 0),
    ],
)
def test_poly_prism_edits_wrapped_target(prism, edit, flag, value):
    assert cmds.polyPrism(prism[1], **{edit: True, flag: value}) == "Values edited."
    assert cmds.polyPrism(prism[1], **{"q": True, flag: True}) == value
