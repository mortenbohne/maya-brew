import pytest
import mb
import mb.scene


@pytest.fixture()
def test_namespace():
    return "my_namespace"


@pytest.fixture()
def test_cube_name():
    return "test_cube"


@pytest.fixture()
def test_cube(test_namespace, test_cube_name):
    cube, history = mb.cmds.polyCube(name=f"{test_namespace}:{test_cube_name}")
    yield cube


@pytest.fixture(autouse=True)
def new_scene():
    return mb.scene.new_file()
