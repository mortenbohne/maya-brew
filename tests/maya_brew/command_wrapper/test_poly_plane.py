import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def plane():
    return cmds.polyPlane(width=2.0, height=3.0, sx=2, sy=3)


@pytest.mark.parametrize("flag", ["width", "w", "height", "h", "sx", "sy"])
@pytest.mark.parametrize("target", [0, 1])
def test_poly_plane_queries_match_maya(plane, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyPlane(plane[target], **flags) == maya_cmds.polyPlane(
        str(plane[target]), **flags
    )


@pytest.mark.parametrize("edit", ["edit", "e"])
def test_poly_plane_edits_wrapped_target(plane, edit):
    assert cmds.polyPlane(plane[1], **{edit: True, "width": 5.0}) == "Values edited."
    assert cmds.polyPlane(plane[1], query=True, width=True) == 5.0
