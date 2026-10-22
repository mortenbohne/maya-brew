import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def cube():
    return cmds.polyCube(width=2.0, height=3.0, depth=4.0, sx=2, sy=3, sz=4)


@pytest.mark.parametrize(
    "flag",
    [
        "width",
        "w",
        "height",
        "h",
        "depth",
        "d",
        "subdivisionsWidth",
        "sw",
        "subdivisionsHeight",
        "sh",
        "subdivisionsDepth",
        "sd",
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
def test_poly_cube_queries_match_maya(cube, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyCube(cube[target], **flags) == maya_cmds.polyCube(
        str(cube[target]), **flags
    )


@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize("flag", ["width", "w", "height", "h", "depth", "d"])
def test_poly_cube_edits_wrapped_target(cube, edit, flag):
    assert cmds.polyCube(cube[1], **{edit: True, flag: 5.0}) == "Values edited."
    assert cmds.polyCube(cube[1], **{"q": True, flag: True}) == 5.0
