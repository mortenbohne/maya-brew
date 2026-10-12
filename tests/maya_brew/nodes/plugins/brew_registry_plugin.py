import maya.api.OpenMaya as om


# Maya checks for this name to pass API 2.0 objects to the plug-in.
def maya_useNewAPI():
    pass


class BrewRegistryNode(om.MPxNode):
    type_name = "brewRegistryTestNode"
    type_id = om.MTypeId(0x0007F7F0)


def initializePlugin(plugin):
    fn = om.MFnPlugin(plugin, "maya-brew", "1.0", "Any")
    fn.registerNode(
        BrewRegistryNode.type_name,
        BrewRegistryNode.type_id,
        BrewRegistryNode,
        lambda: None,
    )


def uninitializePlugin(plugin):
    om.MFnPlugin(plugin).deregisterNode(BrewRegistryNode.type_id)
