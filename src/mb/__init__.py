import os
import logging

PACKAGE_NAME = "MAYA_BREW"


def get_bool_env_variable(name: str, default=True):
    value = os.getenv(name)
    if value is None:
        return default
    return value.lower() in ("true", "1", "t", "yes", "y")


MAYA_BREW_AUTOINIT = get_bool_env_variable(f"{PACKAGE_NAME}_AUTOINIT", True)


def init():
    old_handlers = logging.root.handlers[:]
    old_log_level = logging.getLogger().level
    from mb.maya_initializer.shared import is_interactive_maya
    interactive = is_interactive_maya()
    import mb.log
    if interactive:
        mb.log.configure(use_colors=False)
    else:
        mb.log.configure(use_colors=get_bool_env_variable(f"{PACKAGE_NAME}_USE_LOG_COLORS", True))
    logger = mb.log.get_logger(__name__)
    logger.info("Initializing maya...")
    import maya.api._OpenMaya_py2 as OpenMaya2  # noqa
    os.environ["MAYA_NO_WARNING_FOR_MISSING_DEFAULT_RENDERER"] = "1"
    if is_interactive_maya():
        from mb.maya_initializer import interactive_init
        interactive_init.initialize_maya()
    else:
        from mb.maya_initializer import standalone_init
        standalone_init.initialize_maya()
    logging.root.handlers = old_handlers
    logging.getLogger().setLevel(old_log_level)
    logging.debug("maya initialized")


if MAYA_BREW_AUTOINIT:
    init()
