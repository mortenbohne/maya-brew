import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def pipe():
    return cmds.polyPipe(radius=3.0, height=4.0, thickness=0.5, sa=8, sc=2, sh=3)


@pytest.mark.parametrize(
    "flag",
    [
        "radius",
        "r",
        "height",
        "h",
        "thickness",
        "t",
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
        "createUVs",
        "cuv",
        "texture",
        "tx",
    ],
)
@pytest.mark.parametrize("target", [0, 1])
def test_poly_pipe_queries_match_maya(pipe, flag, target):
    flags = {"query": True, flag: True}
    assert cmds.polyPipe(pipe[target], **flags) == maya_cmds.polyPipe(
        str(pipe[target]), **flags
    )


@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize(
    "flag, value",
    [
        ("radius", 4.0),
        ("r", 4.0),
        ("height", 5.0),
        ("h", 5.0),
        ("thickness", 0.75),
        ("t", 0.75),
        ("roundCap", True),
        ("rcp", True),
        ("roundCapHeightCompensation", True),
        ("rch", True),
        ("subdivisionsAxis", 10),
        ("sa", 10),
        ("subdivisionsCaps", 3),
        ("sc", 3),
        ("subdivisionsHeight", 4),
        ("sh", 4),
        ("createUVs", False),
        ("cuv", False),
        ("texture", False),
        ("tx", False),
    ],
)
def test_poly_pipe_edits_wrapped_target(pipe, edit, flag, value):
    assert cmds.polyPipe(pipe[1], **{edit: True, flag: value}) == "Values edited."
    assert cmds.polyPipe(pipe[1], **{"q": True, flag: True}) == pytest.approx(
        float(value)
    )
