import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture(params=["polyType", "pt"])
def soccer_ball(request):
    return cmds.polyPrimitive(radius=2.0, **{request.param: 0})


@pytest.mark.parametrize(
    "flag",
    [
        "radius",
        "r",
        "sideLength",
        "l",
        "polyType",
        "pt",
        "createUVs",
        "cuv",
        "texture",
        "tx",
    ],
)
@pytest.mark.parametrize("target", [0, 1])
def test_poly_primitive_queries_match_maya(soccer_ball, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyPrimitive(soccer_ball[target], **flags) == maya_cmds.polyPrimitive(
        str(soccer_ball[target]), **flags
    )


@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize(
    "flag, value",
    [
        ("radius", 3.0),
        ("r", 3.0),
        ("sideLength", 0.8),
        ("l", 0.8),
        ("createUVs", 0),
        ("cuv", 0),
        ("texture", 0),
        ("tx", 0),
    ],
)
def test_poly_primitive_edits_wrapped_target(soccer_ball, edit, flag, value):
    assert (
        cmds.polyPrimitive(soccer_ball[1], **{edit: True, flag: value})
        == "Values edited."
    )
    assert cmds.polyPrimitive(
        soccer_ball[1], **{"q": True, flag: True}
    ) == pytest.approx(float(value))


def test_poly_primitive_creates_soccer_ball(soccer_ball):
    assert maya_cmds.polyEvaluate(str(soccer_ball[0]), face=True) == 32
