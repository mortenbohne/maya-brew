import maya_brew

from .exceptions import SceneException, UnsavedChanges


def new_file(force=True):
    try:
        return maya_brew.cmds.file(newFile=True, force=force)
    except RuntimeError as e:
        message = str(e).strip()
        if message == "Unsaved changes.":
            raise UnsavedChanges(message) from e
        raise SceneException(message) from e
