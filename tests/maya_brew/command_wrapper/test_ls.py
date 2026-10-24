import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.exceptions import NodeException
from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.casting import cast
from maya_brew.nodes.node_types import (
    DagNode,
    Joint,
    Mesh,
    MultiplyDivide,
    Shape,
    Transform,
)

TYPE_FILTER_FLAGS = ("type", "typ", "exactType", "et", "excludeType", "ext")


@pytest.fixture
def listed_nodes():
    transform, _ = maya_cmds.polyCube(name="listed_cube")
    shape = maya_cmds.listRelatives(transform, shapes=True, fullPath=True)[0]
    utility = maya_cmds.createNode("multiplyDivide", name="listed_utility")
    return cast(transform), cast(shape), cast(utility)


def test_ls_returns_native_wrappers(listed_nodes):
    transform, shape, utility = listed_nodes
    result = cmds.ls(transform, shape, utility)
    assert [type(node) for node in result] == [Transform, Mesh, MultiplyDivide]
    assert [str(node) for node in result] == [str(node) for node in listed_nodes]


@pytest.mark.parametrize("container", [list, tuple])
def test_ls_accepts_sequences_of_nodes_and_strings(listed_nodes, container):
    transform, _, utility = listed_nodes
    result = cmds.ls(container([transform, str(utility)]))
    assert [str(node) for node in result] == [str(transform), str(utility)]


def test_ls_without_arguments_wraps_scene_nodes(listed_nodes):
    result = cmds.ls(long=True)
    assert all(isinstance(node, Node) for node in result)
    assert [str(node) for node in result] == maya_cmds.ls(long=True)


def test_ls_class_filter_without_objects_only_returns_nodes(listed_nodes):
    result = cmds.ls(type=Transform)
    assert result
    assert all(isinstance(node, Transform) for node in result)
    assert [str(node) for node in result] == [
        str(cast(name)) for name in maya_cmds.ls(type="transform")
    ]


def test_ls_no_matches_returns_empty_list():
    assert cmds.ls("missing_listed_node") == []


@pytest.mark.parametrize(
    "flags",
    [
        {"type": ["transform", "mesh"]},
        {"typ": ("transform", "mesh")},
        {"exactType": "mesh"},
        {"et": ["mesh"]},
        {"excludeType": "mesh"},
        {"ext": ("mesh",)},
        {"head": 1},
        {"tl": 1},
        {"dag": True, "shapes": True},
        {"assemblies": True},
    ],
)
def test_ls_preserves_filtering_and_order(listed_nodes, flags):
    expected = maya_cmds.ls("listed_*", long=True, **flags)
    result = cmds.ls("listed_*", long=True, **flags)
    assert all(isinstance(node, Node) for node in result)
    assert [str(node) for node in result] == expected


class CustomTransform(Transform):
    pass


@pytest.mark.parametrize("flag", TYPE_FILTER_FLAGS)
@pytest.mark.parametrize(
    "value, native",
    [
        (Transform, "transform"),
        (CustomTransform, "transform"),
        (DagNode, "dagNode"),
        ([Transform, "mesh"], ["transform", "mesh"]),
        ((Transform, Mesh), ["transform", "mesh"]),
    ],
)
def test_ls_accepts_wrapper_class_filters(listed_nodes, flag, value, native):
    result = cmds.ls("listed_*", long=True, **{flag: value})
    expected = maya_cmds.ls("listed_*", long=True, **{flag: native})
    assert [str(node) for node in result] == expected


@pytest.mark.parametrize("flag", ["type", "typ", "exactType", "et"])
@pytest.mark.parametrize("objects_only", [False, True])
def test_ls_class_filters_preserve_requested_wrapper(listed_nodes, flag, objects_only):
    result = cmds.ls("listed_*", objectsOnly=objects_only, **{flag: CustomTransform})
    assert result
    assert all(isinstance(node, CustomTransform) for node in result)


@pytest.fixture
def listed_joint():
    return maya_cmds.createNode("joint", name="listed_joint")


def test_ls_retains_native_subclasses(listed_joint):
    result = cmds.ls(listed_joint, type=Transform, objectsOnly=True)
    assert len(result) == 1
    assert isinstance(result[0], Joint)


def test_ls_custom_filter_accepts_native_descendants(listed_joint):
    result = cmds.ls(listed_joint, type=CustomTransform, objectsOnly=True)
    assert len(result) == 1
    assert isinstance(result[0], CustomTransform)
    assert str(result[0]) == maya_cmds.ls(listed_joint, long=True)[0]


def test_ls_custom_filter_keeps_metadata_strings(listed_nodes):
    result = cmds.ls("listed_*", type=CustomTransform, showType=True)
    assert len(result) == 2
    assert isinstance(result[0], CustomTransform)
    assert result[1] == "transform"


def test_ls_mixed_filters_preserve_custom_and_native_wrappers(listed_nodes):
    result = cmds.ls("listed_*", type=[CustomTransform, "mesh"], objectsOnly=True)
    assert {type(node) for node in result} == {CustomTransform, Mesh}


@pytest.mark.parametrize("flag", ["type", "typ", "exactType", "et"])
@pytest.mark.parametrize(
    "node_types",
    [
        (Shape, Transform),
        (CustomTransform,),
        (CustomTransform, Mesh),
        (CustomTransform, Mesh, MultiplyDivide),
    ],
)
def test_ls_tuple_filters_preserve_requested_wrappers(listed_nodes, flag, node_types):
    result = cmds.ls("listed_*", long=True, **{flag: node_types})
    expected = maya_cmds.ls(
        "listed_*",
        long=True,
        **{flag: [node_type._maya_type for node_type in node_types]},
    )
    assert result
    assert [str(node) for node in result] == expected
    assert all(isinstance(node, node_types) for node in result)


@pytest.mark.parametrize("flag", ["showType", "st", "showNamespace", "sns"])
def test_ls_tuple_filters_keep_metadata_strings(listed_nodes, flag):
    result = cmds.ls("listed_*", type=(CustomTransform, Mesh), **{flag: True})
    expected = maya_cmds.ls("listed_*", type=("transform", "mesh"), **{flag: True})
    assert {type(node) for node in result[::2]} == {CustomTransform, Mesh}
    assert result[1::2] == expected[1::2]


def test_ls_additive_selectors_can_return_other_node_types(listed_nodes):
    result = cmds.ls("listed_*", type=CustomTransform, shapes=True, objectsOnly=True)
    assert {type(node) for node in result} == {CustomTransform, Mesh}


@pytest.mark.parametrize("flag", ["type", "typ", "exactType", "et"])
@pytest.mark.parametrize("container", [list, tuple])
def test_ls_empty_type_sequence_does_not_filter(listed_nodes, flag, container):
    result = cmds.ls("listed_*", objectsOnly=True, **{flag: container()})
    assert {type(node) for node in result} == {Transform, Mesh, MultiplyDivide}


@pytest.mark.parametrize("flag", TYPE_FILTER_FLAGS)
def test_ls_rejects_wrappers_without_native_type(flag):
    with pytest.raises(NodeException, match="no native Maya type"):
        cmds.ls(**{flag: Node})


@pytest.mark.parametrize("flag", ["uuid", "uid", "nodeTypes", "nt"])
def test_ls_returns_strings(listed_nodes, flag):
    assert cmds.ls(**{flag: True}) == maya_cmds.ls(**{flag: True})


def test_ls_finds_nodes_by_uuid(listed_nodes):
    transform, _, _ = listed_nodes
    uuid = maya_cmds.ls(str(transform), uuid=True)[0]
    result = cmds.ls(uuid)
    assert isinstance(result[0], Transform)
    assert str(result[0]) == str(transform)


@pytest.mark.parametrize("flag", ["showType", "st", "showNamespace", "sns"])
def test_ls_preserves_flat_metadata_pairs(listed_nodes, flag):
    expected = maya_cmds.ls("listed_*", long=True, **{flag: True})
    result = cmds.ls("listed_*", long=True, **{flag: True})
    assert all(isinstance(node, Node) for node in result[::2])
    assert result[1::2] == expected[1::2]
    assert [str(node) for node in result] == expected


@pytest.fixture
def namespaced_node():
    maya_cmds.namespace(add="listed_namespace")
    return maya_cmds.createNode("transform", name="listed_namespace:transform")


def test_ls_preserves_absolute_namespace_metadata(namespaced_node):
    result = cmds.ls(namespaced_node, showNamespace=True, absoluteName=True)
    assert isinstance(result[0], Transform)
    assert result[1] == ":listed_namespace"


@pytest.fixture
def relative_namespace(namespaced_node):
    maya_cmds.namespace(set=":listed_namespace")
    maya_cmds.namespace(relativeNames=True)
    yield
    maya_cmds.namespace(relativeNames=False)
    maya_cmds.namespace(set=":")


def test_ls_resolves_relative_namespace_names(relative_namespace):
    result = cmds.ls("transform", showNamespace=True)
    assert isinstance(result[0], Transform)
    assert str(result[0]) == maya_cmds.ls("transform", long=True)[0]
    assert result[1] == ""


@pytest.fixture
def selected_items(listed_nodes):
    transform, _, utility = listed_nodes
    items = [str(utility), f"{transform}.vtx[0:2]", f"{transform}.translateX"]
    maya_cmds.select(items, replace=True)
    return items


def test_ls_preserves_component_and_attribute_strings(selected_items):
    result = cmds.ls(selection=True, long=True)
    assert isinstance(result[0], MultiplyDivide)
    assert [str(item) for item in result] == maya_cmds.ls(selection=True, long=True)
    assert all(isinstance(item, str) for item in result[1:])


@pytest.mark.parametrize("flag", ["type", "typ", "exactType", "et"])
@pytest.mark.parametrize(
    "node_type", [Transform, Mesh, MultiplyDivide, CustomTransform]
)
@pytest.mark.parametrize("selection", [False, True])
@pytest.mark.parametrize("objects_only", [False, True])
def test_ls_positive_type_filters_exclude_non_nodes(
    selected_items, flag, node_type, selection, objects_only
):
    targets = () if selection else tuple(selected_items)
    flags = {"selection": selection, "objectsOnly": objects_only, "long": True}
    result = cmds.ls(*targets, **flags, **{flag: node_type})
    expected = maya_cmds.ls(*targets, **flags, **{flag: node_type._maya_type})
    assert [str(node) for node in result] == expected
    assert all(isinstance(node, node_type) for node in result)
    if node_type is MultiplyDivide:
        assert result


@pytest.mark.parametrize("flag", ["type", "typ", "exactType", "et"])
@pytest.mark.parametrize("selection", [False, True])
def test_ls_tuple_filters_exclude_non_nodes(selected_items, flag, selection):
    node_types = (Shape, Transform, MultiplyDivide)
    targets = () if selection else tuple(selected_items)
    result = cmds.ls(*targets, selection=selection, **{flag: node_types})
    expected = maya_cmds.ls(
        *targets,
        selection=selection,
        **{flag: [node_type._maya_type for node_type in node_types]},
    )
    assert result
    assert [str(node) for node in result] == [str(cast(name)) for name in expected]
    assert all(isinstance(node, node_types) for node in result)


@pytest.mark.parametrize("flags", [{}, {"flatten": True}, {"showType": True}])
def test_ls_preserves_component_strings(listed_nodes, flags):
    transform, _, _ = listed_nodes
    component = f"{transform}.vtx[0:2]"
    assert cmds.ls(component, **flags) == maya_cmds.ls(component, **flags)


@pytest.mark.parametrize("flag", ["objectsOnly", "o"])
def test_ls_objects_only_omits_non_nodes(selected_items, flag):
    result = cmds.ls(selection=True, **{flag: True})
    assert all(isinstance(item, Node) for item in result)
    assert [str(item) for item in result] == [
        str(cast(name)) for name in maya_cmds.ls(selection=True, **{flag: True})
    ]


@pytest.fixture
def instanced_node(listed_nodes):
    transform, _, _ = listed_nodes
    maya_cmds.instance(str(transform), name="listed_instance")
    return str(transform)


def test_ls_preserves_all_instance_paths(instanced_node):
    expected = maya_cmds.ls(instanced_node, dag=True, allPaths=True, long=True)
    result = cmds.ls(instanced_node, dag=True, allPaths=True, long=True)
    assert [str(node) for node in result] == expected


@pytest.fixture
def selected_ufe_path():
    maya_usd = pytest.importorskip("mayaUsd.lib")
    ufe = pytest.importorskip("ufe")
    if not maya_cmds.pluginInfo("mayaUsdPlugin", query=True, loaded=True):
        # Maya USD creates persistent nodes, preventing a clean plug-in unload.
        maya_cmds.loadPlugin("mayaUsdPlugin", quiet=True)
    proxy = maya_cmds.createNode("mayaUsdProxyShape", name="listed_proxyShape")
    proxy_path = maya_cmds.ls(proxy, long=True)[0]
    stage = maya_usd.GetPrim(proxy_path).GetStage()
    stage.DefinePrim("/World", "Xform")
    stage.DefinePrim("/World/mesh", "Mesh")
    path = f"{proxy_path},/World/mesh"
    selection = ufe.GlobalSelection.get()
    selection.clear()
    selection.append(ufe.Hierarchy.createItem(ufe.PathString.path(path)))
    yield path
    selection.clear()


@pytest.mark.parametrize("flag", ["ufeObjects", "ufe"])
def test_ls_keeps_ufe_paths_as_strings(selected_ufe_path, flag):
    result = cmds.ls(selection=True, **{flag: True})
    assert selected_ufe_path in result
    assert [str(item) for item in result] == [
        str(item) if "," in item else str(cast(item))
        for item in maya_cmds.ls(selection=True, **{flag: True})
    ]


@pytest.fixture
def selected_transform(listed_nodes):
    transform, _, _ = listed_nodes
    maya_cmds.select(str(transform), replace=True)
    return transform


@pytest.mark.parametrize("selection", [None, False, True])
def test_ls_preserves_selection_flag_behavior(selected_transform, selection):
    flags = {} if selection is None else {"selection": selection}
    result = cmds.ls("listed_*", long=True, **flags)
    assert [str(node) for node in result] == maya_cmds.ls(
        "listed_*", long=True, **flags
    )
    if selection:
        assert [str(node) for node in result] == [str(selected_transform)]
    else:
        assert len(result) == 3


def test_ls_invalid_flag_combination_is_chained():
    with pytest.raises(NodeException, match="ls failed") as caught:
        cmds.ls(showType=True, showNamespace=True)
    assert isinstance(caught.value.__cause__, RuntimeError)
