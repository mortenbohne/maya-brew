import pytest
import mb
import mb.scene


def test_new_scene():
    cube, history = mb.cmds.polyCube()
    with pytest.raises(mb.scene.UnsavedChanges):
        mb.scene.new_file(force=False)
    mb.scene.new_file(force=True)
    assert mb.cmds.objExists(cube) is False


def test_UnsavedChanges_is_RuntimeError():
    try:
        raise mb.scene.UnsavedChanges("some test error")
    except RuntimeError as e:
        assert isinstance(e, mb.scene.UnsavedChanges)
