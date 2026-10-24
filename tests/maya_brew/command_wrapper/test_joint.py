import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds
from maya_brew.command_wrapper import joint
from maya_brew.exceptions import NodeException
from maya_brew.nodes.casting import cast
from maya_brew.nodes.node_types import Joint


@pytest.fixture
def created_joint():
    return cmds.joint()


def test_joint_creation_returns_joint_and_preserves_selection(created_joint):
    assert type(created_joint) is Joint
    assert maya_cmds.nodeType(str(created_joint)) == "joint"
    assert maya_cmds.ls(selection=True, long=True) == [str(created_joint)]
    assert maya_cmds.listRelatives(str(created_joint), parent=True) is None


@pytest.fixture(params=["transform", "joint"])
def selected_parent_joint(request):
    parent = cmds.createNode(request.param, name="selected_parent")
    return parent, cmds.joint(name="selected_child", position=(1, 2, 3))


def test_joint_creation_preserves_selected_parent(selected_parent_joint):
    parent, child = selected_parent_joint
    assert maya_cmds.listRelatives(str(child), parent=True, fullPath=True) == [
        str(parent)
    ]
    assert maya_cmds.joint(str(child), q=True, position=True) == [1, 2, 3]


@pytest.fixture(params=["string", "wrapped", "sequence"])
def explicit_parent_joint(request):
    parent = cmds.createNode("transform", name="explicit_parent")
    maya_cmds.select(clear=True)
    target = {
        "string": str(parent),
        "wrapped": parent,
        "sequence": [parent],
    }[request.param]
    return parent, cmds.joint(target, name="explicit_child")


def test_joint_accepts_explicit_parent(explicit_parent_joint):
    parent, child = explicit_parent_joint
    assert maya_cmds.listRelatives(str(child), parent=True, fullPath=True) == [
        str(parent)
    ]


@pytest.fixture(params=["relative", "r"])
def relative_joint(request):
    parent = cmds.createNode("transform", name="relative_parent")
    maya_cmds.xform(str(parent), translation=(5, 0, 0))
    return cmds.joint(p=(1, 2, 3), **{request.param: True})


def test_joint_relative_creation(relative_joint):
    assert maya_cmds.joint(str(relative_joint), q=True, p=True, a=True) == [6, 2, 3]


@pytest.fixture(params=["long", "short"])
def configured_joint(request):
    if request.param == "long":
        flags = {
            "name": "configured",
            "position": (1, 2, 3),
            "orientation": (10, 20, 30),
            "scale": (1, 2, 3),
            "limitZ": ("-90deg", "90deg"),
            "limitSwitchZ": False,
            "scaleCompensate": False,
            "rotationOrder": "zyx",
        }
    else:
        flags = {
            "n": "configured",
            "p": (1, 2, 3),
            "o": (10, 20, 30),
            "s": (1, 2, 3),
            "lz": ("-90deg", "90deg"),
            "lsz": False,
            "sc": False,
            "roo": "zyx",
        }
    return joint(**flags)


def test_joint_creation_forwards_flags_and_units(configured_joint):
    name = str(configured_joint)
    assert maya_cmds.joint(name, q=True, name=True) == "configured"
    assert maya_cmds.joint(name, q=True, position=True) == [1, 2, 3]
    assert maya_cmds.joint(name, q=True, orientation=True) == pytest.approx(
        [10, 20, 30]
    )
    assert maya_cmds.joint(name, q=True, scale=True) == [1, 2, 3]
    assert maya_cmds.joint(name, q=True, limitZ=True) == [-90, 90]
    assert maya_cmds.joint(name, q=True, limitSwitchZ=True) == [False, False]
    assert not maya_cmds.joint(name, q=True, scaleCompensate=True)
    assert maya_cmds.joint(name, q=True, rotationOrder=True) == "zyx"


@pytest.fixture
def joint_chain():
    root = cmds.joint(name="root", p=(1, 0, 0))
    middle = cmds.joint(name="middle", p=(1, 4, 0))
    tip = cmds.joint(name="tip", p=(1, 8, 1))
    return root, middle, tip


@pytest.mark.parametrize("mode", ["query", "q"])
@pytest.mark.parametrize(
    "flag",
    [
        "angleX",
        "ax",
        "angleY",
        "ay",
        "angleZ",
        "az",
        "degreeOfFreedom",
        "dof",
        "limitSwitchX",
        "lsx",
        "limitSwitchY",
        "lsy",
        "limitSwitchZ",
        "lsz",
        "limitX",
        "lx",
        "limitY",
        "ly",
        "limitZ",
        "lz",
        "name",
        "n",
        "orientation",
        "o",
        "position",
        "p",
        "radius",
        "rad",
        "rotationOrder",
        "roo",
        "scale",
        "s",
        "scaleCompensate",
        "sc",
        "scaleOrientation",
        "so",
        "stiffnessX",
        "stx",
        "stiffnessY",
        "sty",
        "stiffnessZ",
        "stz",
    ],
)
def test_joint_queries_match_maya(joint_chain, mode, flag):
    target = joint_chain[1]
    flags = {mode: True, flag: True}
    assert cmds.joint(target, **flags) == maya_cmds.joint(str(target), **flags)


@pytest.mark.parametrize("space", ["absolute", "a", "relative", "r"])
def test_joint_position_space_queries_match_maya(joint_chain, space):
    target = joint_chain[1]
    flags = {"q": True, "position": True, space: True}
    assert cmds.joint(target, **flags) == maya_cmds.joint(str(target), **flags)


@pytest.mark.parametrize("mode", ["edit", "e"])
@pytest.mark.parametrize("targets", ["strings", "wrapped", "list", "tuple", "mixed"])
def test_joint_edits_multiple_targets(joint_chain, mode, targets):
    root, middle, _ = joint_chain
    arguments = {
        "strings": (str(root), str(middle)),
        "wrapped": (root, middle),
        "list": ([root, middle],),
        "tuple": ((root, middle),),
        "mixed": ([root], str(middle)),
    }[targets]
    assert cmds.joint(*arguments, **{mode: True, "stx": 25}) is None
    for target in (root, middle):
        assert maya_cmds.joint(str(target), q=True, stx=True) == [25]


def test_joint_multi_target_radius_edit_matches_maya(joint_chain):
    names = [str(target) for target in joint_chain]
    maya_cmds.joint(*names, e=True, radius=2.5)
    expected = [maya_cmds.getAttr(f"{name}.radius") for name in names]
    for name in names:
        maya_cmds.setAttr(f"{name}.radius", 1)
    assert cmds.joint(joint_chain, e=True, radius=2.5) is None
    assert [maya_cmds.getAttr(f"{name}.radius") for name in names] == expected


@pytest.fixture
def selected_joint(joint_chain):
    target = joint_chain[1]
    maya_cmds.select(str(target))
    return target


def test_joint_edits_and_queries_implicit_selection(selected_joint):
    assert cmds.joint(e=True, radius=3) is None
    assert cmds.joint(q=True, radius=True) == [3]
    assert cmds.joint(q=True, name=True) == maya_cmds.joint(
        str(selected_joint), q=True, name=True
    )
    assert maya_cmds.ls(selection=True, long=True) == [str(selected_joint)]


@pytest.mark.parametrize("children", ["children", "ch"])
def test_joint_edits_descendants(joint_chain, children):
    assert cmds.joint(joint_chain[0], e=True, **{children: True, "stx": 40}) is None
    for target in joint_chain:
        assert maya_cmds.joint(str(target), q=True, stx=True) == [40]


@pytest.mark.parametrize("relative", ["relative", "r"])
def test_joint_relative_position_edit(joint_chain, relative):
    middle = joint_chain[1]
    assert cmds.joint(middle, e=True, p=(2, 3, 4), **{relative: True}) is None
    assert maya_cmds.joint(str(middle), q=True, p=True, r=True) == [2, 3, 4]


def test_joint_component_edit_preserves_child_world_position(joint_chain):
    middle, tip = joint_chain[1:]
    position = maya_cmds.joint(str(tip), q=True, p=True, a=True)
    assert cmds.joint(middle, e=True, co=True, p=(2, 3, 4)) is None
    assert maya_cmds.joint(str(tip), q=True, p=True, a=True) == position


def test_joint_orientation_and_preferred_angles(joint_chain):
    root = joint_chain[0]
    assert cmds.joint(root, e=True, oj="xyz", sao="yup", zso=True) is None
    assert maya_cmds.joint(str(root), q=True, o=True) != [0, 0, 0]
    cmds.joint(root, e=True, ax=20, ay=10, az=5)
    assert cmds.joint(root, e=True, spa=True) is None
    cmds.joint(root, e=True, ax=0, ay=0, az=0)
    assert cmds.joint(root, e=True, apa=True) is None
    assert maya_cmds.joint(str(root), q=True, ax=True) == pytest.approx([20])
    assert maya_cmds.joint(str(root), q=True, ay=True) == pytest.approx([10])
    assert maya_cmds.joint(str(root), q=True, az=True) == pytest.approx([5])


@pytest.fixture
def native_joint_chain():
    root = maya_cmds.joint(name="native_root", p=(1, 0, 0))
    middle = maya_cmds.joint(name="native_middle", p=(1, 4, 0))
    tip = maya_cmds.joint(name="native_tip", p=(1, 8, 1))
    maya_cmds.select(clear=True)
    return root, middle, tip


@pytest.mark.parametrize(
    "flags",
    [
        {"automaticLimits": True},
        {"al": True},
        {
            "orientJoint": "xyz",
            "secondaryAxisOrient": "yup",
            "autoOrientSecondaryAxis": True,
        },
        {"oj": "xyz", "sao": "yup", "aos": True},
    ],
)
def test_joint_automatic_orientation_and_limits_match_maya(
    native_joint_chain, joint_chain, flags
):
    assert cmds.joint(joint_chain[1], e=True, **flags) == maya_cmds.joint(
        native_joint_chain[1], e=True, **flags
    )
    for wrapped, native in zip(joint_chain, native_joint_chain):
        for attribute in (
            "jointOrient",
            "rotateAxis",
            "translate",
            "rotate",
            "minRotLimit",
            "maxRotLimit",
            "minRotLimitEnable",
            "maxRotLimitEnable",
        ):
            assert maya_cmds.getAttr(f"{wrapped}.{attribute}") == maya_cmds.getAttr(
                f"{native}.{attribute}"
            )


@pytest.fixture
def ik_handle(joint_chain):
    root, _, tip = joint_chain
    name, _ = maya_cmds.ikHandle(startJoint=str(root), endEffector=str(tip))
    return cast(name), joint_chain


def test_joint_edits_ik_handle_targets(ik_handle):
    handle, chain = ik_handle
    assert cmds.joint(handle, e=True, stx=50) is None
    for target in chain[:-1]:
        assert maya_cmds.joint(str(target), q=True, stx=True) == [50]


@pytest.mark.parametrize("flag", ["exists", "ex"])
@pytest.mark.parametrize("mode", [{}, {"q": True}, {"e": True}])
@pytest.mark.parametrize("value", ["root", "missing_joint", True, False, ""])
def test_joint_existence_matches_maya(joint_chain, flag, mode, value):
    flags = {**mode, flag: value}
    if mode.get("q") and isinstance(value, str):
        with pytest.raises(TypeError):
            maya_cmds.joint(**flags)
        with pytest.raises(TypeError):
            cmds.joint(**flags)
        return
    result = cmds.joint(**flags)
    assert type(result) is bool
    assert result == maya_cmds.joint(**flags)


@pytest.fixture
def symmetric_joint():
    return cmds.joint(p=(2, 0, 0), symmetry=True, symmetryAxis="x")


def test_joint_symmetry_creation_returns_joint(symmetric_joint):
    assert type(symmetric_joint) is Joint
    assert maya_cmds.objExists(str(symmetric_joint))


def test_joint_runtime_errors_are_chained(joint_chain):
    with pytest.raises(NodeException, match="joint failed") as error:
        cmds.joint(joint_chain[0], e=True, orientJoint="invalid")
    assert isinstance(error.value.__cause__, RuntimeError)


def test_joint_missing_target_preserves_native_value_error():
    with pytest.raises(ValueError, match="No object matches name"):
        cmds.joint("missing_joint", e=True, radius=1)
