import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@pytest.fixture
def sphere():
    return cmds.polySphere(radius=2.0, subdivisionsX=10, subdivisionsY=15)


@pytest.mark.parametrize(
    "flags",
    [
        {"query": True, "radius": True},
        {"q": True, "r": True},
        {"q": True, "sx": True},
        {"query": True, "subdivisionsY": True},
    ],
)
@pytest.mark.parametrize("target", [0, 1])
def test_poly_sphere_queries_match_maya(sphere, flags, target):
    assert cmds.polySphere(sphere[target], **flags) == maya_cmds.polySphere(
        str(sphere[target]), **flags
    )


@pytest.mark.parametrize("edit, radius", [("edit", "radius"), ("e", "r")])
def test_poly_sphere_edits_wrapped_target(sphere, edit, radius):
    result = cmds.polySphere(sphere[1], **{edit: True, radius: 3.0})
    assert result == "Values edited."
    assert cmds.polySphere(sphere[1], q=True, radius=True) == 3.0
