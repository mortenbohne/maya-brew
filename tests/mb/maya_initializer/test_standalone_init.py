from mb.maya_initializer import standalone_init


def test_init_standalone():
    standalone_init.init_standalone()

    import maya.cmds as cmds
    cube, = cmds.polyCube(constructionHistory=False)
    assert isinstance(cube, str)
