import pytest
from tools.command_wrapper.help import command_flags


@pytest.mark.parametrize(
    "maya_type, annotation",
    [
        ("", "bool"),
        ("String", "str"),
        ("Int", "int"),
        ("Float", "float"),
        ("Angle", "float"),
        ("Boolean", "bool"),
        ("Length", "float"),
        ("on|off", "bool"),
    ],
)
def test_help_flags_and_aliases(maya_type, annotation):
    assert command_flags("example", f"  -v -value {maya_type}\n", {}) == {
        "value": annotation,
        "v": annotation,
    }


def test_flag_overrides_complete_help():
    assert command_flags(
        "example",
        "  -v -value Unsupported\n",
        {"value": "tuple[float, float]", "extra": "str"},
    ) == {
        "value": "tuple[float, float]",
        "v": "tuple[float, float]",
        "extra": "str",
    }


@pytest.mark.parametrize(
    "maya_type, annotation",
    [
        ("Length Length", "tuple[float, float]"),
        ("Length Length Length", "tuple[float, float, float]"),
        ("Int Int", "tuple[int, int]"),
    ],
)
def test_multi_value_help_types_are_inferred(maya_type, annotation):
    assert command_flags("example", f"  -v -value {maya_type}\n", {}) == {
        "value": annotation,
        "v": annotation,
    }


@pytest.mark.parametrize(
    "help_text, message",
    [
        ("  -v -value Unsupported\n", "unsupported help type"),
        ("  -value\n", "unsupported flag help line"),
        ("Synopsis: example\nFlags:\n", "no flags found"),
    ],
)
def test_invalid_help_requires_explicit_handling(help_text, message):
    with pytest.raises(ValueError, match=message):
        command_flags("example", help_text, {})


def test_overrides_supply_flags_missing_from_help():
    assert command_flags("example", "", {"value": "str"}) == {"value": "str"}


def test_explicitly_flagless_command():
    assert (
        command_flags(
            "removeJoint", "Synopsis: removeJoint [String...]\nNo Flags.\n", {}
        )
        == {}
    )
