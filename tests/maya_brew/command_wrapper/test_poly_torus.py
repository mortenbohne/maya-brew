import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def torus():
    return cmds.polyTorus(radius=3.0, sectionRadius=0.5, sx=8, sy=6, twist=30.0)


@pytest.mark.parametrize(
    "flag",
    [
        "radius",
        "r",
        "sectionRadius",
        "sr",
        "twist",
        "tw",
        "subdivisionsAxis",
        "sa",
        "subdivisionsHeight",
        "sh",
        "subdivisionsX",
        "sx",
        "subdivisionsY",
        "sy",
        "createUVs",
        "cuv",
        "texture",
        "tx",
    ],
)
@pytest.mark.parametrize("target", [0, 1])
def test_poly_torus_queries_match_maya(torus, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyTorus(torus[target], **flags) == maya_cmds.polyTorus(
        str(torus[target]), **flags
    )


@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize(
    "flag, value",
    [
        ("radius", 4.0),
        ("r", 4.0),
        ("sectionRadius", 0.75),
        ("sr", 0.75),
        ("twist", 45.0),
        ("tw", 45.0),
        ("subdivisionsAxis", 10),
        ("sa", 10),
        ("subdivisionsHeight", 8),
        ("sh", 8),
        ("subdivisionsX", 10),
        ("sx", 10),
        ("subdivisionsY", 8),
        ("sy", 8),
        ("createUVs", False),
        ("cuv", False),
        ("texture", False),
        ("tx", False),
    ],
)
def test_poly_torus_edits_wrapped_target(torus, edit, flag, value):
    assert cmds.polyTorus(torus[1], **{edit: True, flag: value}) == "Values edited."
    assert cmds.polyTorus(torus[1], **{"q": True, flag: True}) == pytest.approx(
        float(value)
    )
