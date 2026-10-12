from maya_brew import cmds
from maya_brew.nodes._foundation import node_registry
from maya_brew.nodes._foundation.node_registry import NodeRegistry


def test_classes_are_cached():
    local = NodeRegistry(use_generated=False)
    assert local.get_or_create_class("joint") is local.get_or_create_class("joint")


def test_fallback_preserves_inheritance():
    local = NodeRegistry(use_generated=False)
    joint = local.get_or_create_class("joint")
    transform = local.get_or_create_class("transform")
    dag_node = local.get_or_create_class("dagNode")

    assert issubclass(joint, transform)
    assert issubclass(transform, dag_node)
    assert joint._maya_type == "joint"


def test_late_loaded_plugin_fallback(plugin_type):
    local = NodeRegistry()
    wrapper = local.get_or_create_class(plugin_type)
    assert wrapper._maya_type == plugin_type
    assert wrapper.__module__ == node_registry.__name__


def test_missing_version_snapshot_warns_and_falls_back(monkeypatch, caplog):
    # noinspection PyUnresolvedReferences
    monkeypatch.setattr(cmds, "about", lambda **kwargs: "9999")
    local = NodeRegistry()
    wrapper = local.get_or_create_class("transform")

    assert wrapper.__module__ == node_registry.__name__
    assert caplog.text.count("No generated node snapshot for Maya 9999") == 1
