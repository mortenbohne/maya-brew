import pytest
import mb
import mb.scene
import mb.nodes.node_types


@pytest.fixture()
def test_namespace():
    return "my_namespace"


@pytest.fixture()
def test_cube_short_name():
    return "test_cube"


@pytest.fixture()
def test_cube(test_namespace, test_cube_short_name):
    cube, history = mb.cmds.polyCube(name=f"{test_namespace}:{test_cube_short_name}")
    yield cube


@pytest.fixture()
def empty_transform():
    """
    Fixture to return the node object of the test cube.
    """
    yield mb.nodes.node_types.Transform.create("test_transform")


@pytest.fixture(autouse=True)
def new_scene():
    return mb.scene.new_file()
