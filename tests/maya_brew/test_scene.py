import maya.cmds as cmds
import maya_brew
import maya_brew.scene
import pytest


def test_new_scene():
    cube, history = cmds.polyCube()
    with pytest.raises(maya_brew.scene.UnsavedChanges):
        maya_brew.scene.new_file(force=False)
    maya_brew.scene.new_file(force=True)
    assert cmds.objExists(cube) is False


def test_command_wrapper_is_exported_from_package():
    from maya_brew import command_wrapper

    assert maya_brew.cmds is command_wrapper


def test_UnsavedChanges_is_RuntimeError():
    try:
        raise maya_brew.scene.UnsavedChanges("some test error")
    except RuntimeError as e:
        assert isinstance(e, maya_brew.scene.UnsavedChanges)
