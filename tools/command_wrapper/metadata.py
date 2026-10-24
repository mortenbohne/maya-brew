from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, TypeAlias

from maya_brew.command_wrapper import extensions


@dataclass(frozen=True)
class CommandSignature:
    argument_type: str = "str"
    flag_type_overrides: dict[str, str] = field(default_factory=dict)


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
    extensions.createNode: NodeCreationSignature(
        type_argument="node_type",
        nullable_return_flags=("shared", "s"),
        node_flags=("parent", "p"),
    ),
    extensions.ikHandle: CommandSignature(
        argument_type="str | Node | Sequence[str | Node]",
        flag_type_overrides={
            **{
                flag: "str | Node | bool"
                for flag in ("startJoint", "endEffector", "curve", "solver")
            },
            **{
                flag: "str | bool" for flag in ("exists", "name", "sticky", "twistType")
            },
        },
    ),
    extensions.ikSolver: CommandSignature(
        argument_type="str | Node | Sequence[str | Node]",
        flag_type_overrides={"name": "str | bool", "solverType": "str | bool"},
    ),
    extensions.joint: CommandSignature(
        argument_type="str | Node | Sequence[str | Node]",
        flag_type_overrides={
            **{flag: "float | str | bool" for flag in ("angleX", "angleY", "angleZ")},
            **{
                flag: "tuple[float | str, float | str] | bool"
                for flag in ("limitX", "limitY", "limitZ")
            },
            **{
                flag: "tuple[float | str, float | str, float | str] | bool"
                for flag in ("orientation", "position", "scaleOrientation")
            },
            "scale": "tuple[float, float, float] | bool",
            **{
                flag: "str | bool"
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
    extensions.polyPipe: PrimitiveSignature(history_type="PolyPipe"),
    extensions.polyPyramid: PrimitiveSignature(history_type="PolyPyramid"),
    extensions.polyPrism: PrimitiveSignature(history_type="PolyPrism"),
    extensions.polyHelix: PrimitiveSignature(history_type="PolyHelix"),
    extensions.polyPlatonicSolid: PrimitiveSignature(history_type="PolyPlatonicSolid"),
    extensions.polyPrimitive: PrimitiveSignature(history_type="PolyPrimitiveMisc"),
    extensions.ls: CommandSignature(
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
