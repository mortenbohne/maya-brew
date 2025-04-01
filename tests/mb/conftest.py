import pytest
import mb.scene


@pytest.fixture(autouse=True)
def new_scene():
    return mb.scene.new_file()