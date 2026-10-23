import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def helix():
    return cmds.polyHelix(coils=2.5, height=4.0, width=3.0, radius=0.25, sa=8, sco=12)


@pytest.mark.parametrize(
    "flag",
    [
        "coils",
        "c",
        "direction",
        "d",
        "height",
        "h",
        "width",
        "w",
        "radius",
        "r",
        "roundCap",
        "rcp",
        "subdivisionsAxis",
        "sa",
        "subdivisionsCaps",
        "sc",
        "subdivisionsCoil",
        "sco",
        "createUVs",
        "cuv",
        "texture",
        "tx",
        "useOldInitBehaviour",
        "oib",
    ],
)
@pytest.mark.parametrize("target", [0, 1])
def test_poly_helix_queries_match_maya(helix, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyHelix(helix[target], **flags) == maya_cmds.polyHelix(
        str(helix[target]), **flags
    )


@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize(
    "flag, value",
    [
        ("coils", 3.5),
        ("c", 3.5),
        ("direction", 0),
        ("d", 0),
        ("height", 5.0),
        ("h", 5.0),
        ("width", 4.0),
        ("w", 4.0),
        ("radius", 0.5),
        ("r", 0.5),
        ("roundCap", True),
        ("rcp", True),
        ("subdivisionsAxis", 10),
        ("sa", 10),
        ("subdivisionsCaps", 2),
        ("sc", 2),
        ("subdivisionsCoil", 16),
        ("sco", 16),
        ("createUVs", 0),
        ("cuv", 0),
        ("texture", 0),
        ("tx", 0),
        ("useOldInitBehaviour", True),
        ("oib", True),
    ],
)
def test_poly_helix_edits_wrapped_target(helix, edit, flag, value):
    assert cmds.polyHelix(helix[1], **{edit: True, flag: value}) == "Values edited."
    assert cmds.polyHelix(helix[1], **{"q": True, flag: True}) == pytest.approx(
        float(value)
    )
