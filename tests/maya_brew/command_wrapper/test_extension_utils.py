import pytest
from maya_brew.command_wrapper import extension_utils
from maya_brew.exceptions import NodeException
from maya_brew.nodes._foundation.node_extensions import Node


def test_command_forwards_arguments_and_preserves_result():
    expected = object()
    supplied = {"query": False, "name": None}

    def command(*args, **kwargs):
        assert args == ("first", "second")
        assert kwargs == supplied
        return expected

    assert (
        extension_utils._call_command("example", command, ["first", "second"], supplied)
        is expected
    )
    assert supplied == {"query": False, "name": None}


def test_command_runtime_errors_are_chained():
    error = RuntimeError("invalid target")

    def command():
        raise error

    with pytest.raises(NodeException, match="example failed: invalid target") as caught:
        extension_utils._call_command("example", command, [], {})
    assert caught.value.__cause__ is error


def test_command_does_not_translate_programming_errors():
    error = TypeError("invalid argument")

    def command():
        raise error

    with pytest.raises(TypeError) as caught:
        extension_utils._call_command("example", command, [], {})
    assert caught.value is error


@pytest.mark.parametrize("result", [None, 1, True, [], ["joint1"], ("joint1",)])
def test_node_result_rejects_non_string_results(result):
    with pytest.raises(NodeException, match="Unexpected result from example"):
        extension_utils._node_result("example", result, Node)


def test_node_result_passes_expected_type_to_cast(monkeypatch):
    expected = object()

    def cast(name, expected_type):
        assert name == "joint1"
        assert expected_type is Node
        return expected

    monkeypatch.setitem(vars(extension_utils), "cast", cast)
    assert extension_utils._node_result("example", "joint1", Node) is expected
