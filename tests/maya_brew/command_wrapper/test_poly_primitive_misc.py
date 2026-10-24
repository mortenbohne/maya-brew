import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture(params=["polyType", "pt"])
def soccer_ball(request):
    return cmds.polyPrimitive(radius=2.0, **{request.param: 0})


def test_poly_primitive_creates_soccer_ball(soccer_ball):
    assert maya_cmds.polyEvaluate(str(soccer_ball[0]), face=True) == 32
