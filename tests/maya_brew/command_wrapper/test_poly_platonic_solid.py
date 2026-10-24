import pytest
from maya_brew import cmds


@pytest.fixture(
    params=[(flag, value) for flag in ("solidType", "st") for value in range(4)]
)
def selected_solid_type(request):
    flag, value = request.param
    return cmds.polyPlatonicSolid(**{flag: value}), value


def test_poly_platonic_solid_creates_selected_type(selected_solid_type):
    nodes, expected = selected_solid_type
    assert cmds.polyPlatonicSolid(nodes[1], q=True, solidType=True) == expected
