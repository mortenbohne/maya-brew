import pytest

from maya_brew import cmds
from tests.maya_brew.nodes.plugins import brew_registry_plugin


@pytest.fixture
def plugin_type():
    plugin = cmds.loadPlugin(brew_registry_plugin.__file__, quiet=True)[0]
    yield brew_registry_plugin.BrewRegistryNode.type_name
    cmds.unloadPlugin(plugin)
