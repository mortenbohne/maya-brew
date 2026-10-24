import maya.cmds as maya_cmds
from maya_brew import cmds


def _create_wrap_selection() -> None:
    target = cmds.polySphere(name="wrap_target")[0]
    driver = cmds.polyCube(name="wrap_driver")[0]
    maya_cmds.select(str(target), str(driver), replace=True)


def test_create_jiggle_deformer_matches_maya():
    target = cmds.polySphere(name="jiggle_target")[0]
    maya_cmds.select(str(target), replace=True)
    expected = getattr(maya_cmds, "CreateJiggleDeformer")()
    expected_count = len(maya_cmds.ls(type="jiggle"))

    maya_cmds.file(new=True, force=True)
    target = cmds.polySphere(name="jiggle_target")[0]
    maya_cmds.select(str(target), replace=True)
    actual = cmds.CreateJiggleDeformer()
    actual_count = len(maya_cmds.ls(type="jiggle"))

    assert actual is expected is None
    assert actual_count == expected_count


def test_create_wrap_matches_maya():
    _create_wrap_selection()
    expected = getattr(maya_cmds, "CreateWrap")()
    expected_count = len(maya_cmds.ls(type="wrap"))

    maya_cmds.file(new=True, force=True)
    _create_wrap_selection()
    actual = cmds.CreateWrap()
    actual_count = len(maya_cmds.ls(type="wrap"))

    assert actual is expected is None
    assert actual_count == expected_count
