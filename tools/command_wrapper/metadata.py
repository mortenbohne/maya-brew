from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, TypeAlias

from maya_brew.command_wrapper import extensions


@dataclass(frozen=True)
class CommandSignature:
    argument_type: str = "str"
    flag_type_overrides: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class LsSignature(CommandSignature):
    pass


@dataclass(frozen=True)
class ModeSignature(CommandSignature):
    creation_return_type: str = "Node"
    node_imports: tuple[str, ...] = ()
    queryable_flag_types: dict[str, str] = field(default_factory=dict)
    presence_flags: tuple[str, ...] = ()
    presence_return_type: str = "Any"


@dataclass(frozen=True)
class NodeCreationSignature:
    type_argument: str
    nullable_return_flags: tuple[str, ...] = ()
    node_flags: tuple[str, ...] = ()
    flag_type_overrides: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class PrimitiveSignature:
    history_type: str
    flag_type_overrides: dict[str, str] = field(default_factory=dict)


Signature: TypeAlias = CommandSignature | NodeCreationSignature | PrimitiveSignature


COMMANDS: dict[Callable[..., Any], Signature] = {
    extensions.ikHandleDisplayScale: CommandSignature(
        argument_type="float",
        # Maya standalone does not provide quick help for this command.
        flag_type_overrides={"query": "bool", "q": "bool"},
    ),
    extensions.ikSystemInfo: CommandSignature(argument_type="bool"),
    extensions.jointDisplayScale: CommandSignature(
        argument_type="float",
        flag_type_overrides={"ikfk": "float | bool"},
    ),
    extensions.insertJoint: CommandSignature(
        argument_type="str | Node | Sequence[str | Node]",
    ),
    extensions.lattice: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="Ffd",
        node_imports=("Ffd",),
        queryable_flag_types={"divisions": "list[int]"},
    ),
    extensions.nonLinear: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="NonLinear",
        node_imports=("NonLinear",),
        queryable_flag_types={"geometry": "str | Node | Sequence[str | Node]"},
        flag_type_overrides={flag: "str | Sequence[str]" for flag in ("type", "typ")},
    ),
    extensions.connectJoint: CommandSignature(
        argument_type="str | Node | Sequence[str | Node]",
    ),
    extensions.CreateJiggleDeformer: CommandSignature(
        argument_type="str | Node | Sequence[str | Node]",
    ),
    extensions.CreateWrap: CommandSignature(
        argument_type="str | Node | Sequence[str | Node]",
    ),
    extensions.mirrorJoint: CommandSignature(
        argument_type="str | Node | Sequence[str | Node]",
        flag_type_overrides={"searchReplace": "tuple[str, str]"},
    ),
    extensions.removeJoint: CommandSignature(
        argument_type="str | Node | Sequence[str | Node]",
    ),
    extensions.createNode: NodeCreationSignature(
        type_argument="node_type",
        nullable_return_flags=("shared", "s"),
        node_flags=("parent", "p"),
    ),
    extensions.ikHandle: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type=(
            "tuple[IkHandle] | tuple[IkHandle, IkEffector]"
            " | tuple[IkHandle, IkEffector, Transform]"
        ),
        node_imports=("IkHandle", "IkEffector", "Transform"),
        presence_flags=("exists", "ex"),
        queryable_flag_types={
            **{
                flag: "str | Node"
                for flag in ("startJoint", "endEffector", "curve", "solver")
            },
            **{flag: "str" for flag in ("exists", "name", "sticky", "twistType")},
        },
    ),
    extensions.ikSolver: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="IkSolver",
        node_imports=("IkSolver",),
        queryable_flag_types={"name": "str", "solverType": "str"},
    ),
    extensions.ambientLight: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="AmbientLight",
        node_imports=("AmbientLight",),
        queryable_flag_types={
            "name": "str",
            "intensity": "float",
            "position": "tuple[float, float, float]",
            "rotation": "tuple[float, float, float]",
        },
    ),
    extensions.blendShape: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="BlendShape",
        node_imports=("BlendShape",),
        queryable_flag_types={"envelope": "float"},
    ),
    extensions.cluster: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="Cluster",
        node_imports=("Cluster",),
        queryable_flag_types={"envelope": "float"},
    ),
    extensions.deltaMush: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="DeltaMush",
        node_imports=("DeltaMush",),
        queryable_flag_types={"envelope": "float"},
    ),
    extensions.directionalLight: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="DirectionalLight",
        node_imports=("DirectionalLight",),
        queryable_flag_types={
            "name": "str",
            "intensity": "float",
            "position": "tuple[float, float, float]",
            "rotation": "tuple[float, float, float]",
            "decayRate": "int",
        },
    ),
    extensions.pointLight: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="PointLight",
        node_imports=("PointLight",),
        queryable_flag_types={
            "name": "str",
            "intensity": "float",
            "position": "tuple[float, float, float]",
            "rotation": "tuple[float, float, float]",
            "decayRate": "int",
        },
    ),
    extensions.spotLight: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="SpotLight",
        node_imports=("SpotLight",),
        queryable_flag_types={
            "name": "str",
            "intensity": "float",
            "position": "tuple[float, float, float]",
            "rotation": "tuple[float, float, float]",
            "decayRate": "int",
            "coneAngle": "float",
            "penumbra": "float",
        },
    ),
    extensions.spaceLocator: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="Transform",
        node_imports=("Transform",),
        queryable_flag_types={
            "name": "str",
            "position": "tuple[float, float, float]",
        },
    ),
    extensions.skinCluster: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="SkinCluster",
        node_imports=("SkinCluster",),
        queryable_flag_types={
            "skinMethod": "int",
            "normalizeWeights": "int",
            "maximumInfluences": "int",
        },
    ),
    extensions.joint: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="Joint",
        node_imports=("Joint",),
        presence_flags=("exists", "ex"),
        presence_return_type="bool",
        queryable_flag_types={
            **{flag: "float | str" for flag in ("angleX", "angleY", "angleZ")},
            **{
                flag: "tuple[float | str, float | str]"
                for flag in ("limitX", "limitY", "limitZ")
            },
            **{
                flag: "tuple[float | str, float | str, float | str]"
                for flag in ("orientation", "position", "scaleOrientation")
            },
            "scale": "tuple[float, float, float]",
            **{
                flag: "str"
                for flag in ("degreeOfFreedom", "exists", "name", "rotationOrder")
            },
        },
    ),
    extensions.polyPlane: PrimitiveSignature(history_type="PolyPlane"),
    extensions.polyCone: PrimitiveSignature(history_type="PolyCone"),
    extensions.polyCylinder: PrimitiveSignature(history_type="PolyCylinder"),
    extensions.polyCube: PrimitiveSignature(history_type="PolyCube"),
    extensions.polySphere: PrimitiveSignature(history_type="PolySphere"),
    extensions.polyTorus: PrimitiveSignature(
        history_type="PolyTorus",
        flag_type_overrides={"twist": "float"},
    ),
    extensions.proximityWrap: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="ProximityWrap",
        node_imports=("ProximityWrap",),
        queryable_flag_types={"freeDriverIndex": "int"},
    ),
    extensions.sculpt: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="Sculpt",
        node_imports=("Sculpt",),
        queryable_flag_types={
            "mode": "list[str]",
            "insideMode": "list[str]",
            "maxDisplacement": "list[float]",
        },
    ),
    extensions.softMod: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="SoftMod",
        node_imports=("SoftMod",),
        queryable_flag_types={"envelope": "float"},
    ),
    extensions.wire: ModeSignature(
        argument_type="str | Node | Sequence[str | Node]",
        creation_return_type="Wire",
        node_imports=("Wire",),
        queryable_flag_types={"envelope": "float"},
    ),
    extensions.polyPipe: PrimitiveSignature(history_type="PolyPipe"),
    extensions.polyPyramid: PrimitiveSignature(history_type="PolyPyramid"),
    extensions.polyPrism: PrimitiveSignature(history_type="PolyPrism"),
    extensions.polyHelix: PrimitiveSignature(history_type="PolyHelix"),
    extensions.polyPlatonicSolid: PrimitiveSignature(history_type="PolyPlatonicSolid"),
    extensions.polyPrimitive: PrimitiveSignature(history_type="PolyPrimitiveMisc"),
    extensions.circle: PrimitiveSignature(history_type="MakeNurbCircle"),
    extensions.cone: PrimitiveSignature(history_type="MakeNurbCone"),
    extensions.cylinder: PrimitiveSignature(history_type="MakeNurbCylinder"),
    extensions.sphere: PrimitiveSignature(history_type="MakeNurbSphere"),
    extensions.torus: PrimitiveSignature(history_type="MakeNurbTorus"),
    extensions.nurbsPlane: PrimitiveSignature(history_type="MakeNurbPlane"),
    extensions.nurbsCube: PrimitiveSignature(history_type="MakeNurbCube"),
    extensions.nurbsSquare: PrimitiveSignature(history_type="MakeNurbsSquare"),
    extensions.ls: LsSignature(
        flag_type_overrides={
            "containerType": "str | list[str] | tuple[str, ...]",
            **{
                flag: "str | type[Node] | Sequence[str | type[Node]]"
                for flag in ("exactType", "excludeType", "type")
            },
        },
        argument_type="str | Node | Sequence[str | Node]",
    ),
}
