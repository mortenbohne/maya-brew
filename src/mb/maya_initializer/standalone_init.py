from mb.log import get_logger

logger = get_logger(__name__)


def init_standalone():
    if cmds_about_exists():
        return
    with logger.silence(["This plugin does not support createPlatformOpenGLContext!"]):
        import maya.standalone
        maya.standalone.initialize(name="initialized_by_maya_brew")

def cmds_about_exists():
    try:
        from maya.cmds import about
        return True
    except ImportError:
        return False

if __name__ == "__main__":
    init_standalone()