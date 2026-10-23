from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from maya_brew.command_wrapper import extensions


@dataclass(frozen=True)
class CommandMetadata:
    type_argument: str | None = None
    nullable_flags: tuple[str, ...] = ()
    node_arguments: tuple[str, ...] = ()
    flag_types: dict[str, str] = field(default_factory=dict)
    node_targets: bool = False
    target_type: str | None = None
    primitive_history_type: str | None = None


COMMANDS: dict[Callable[..., Any], CommandMetadata] = {
    extensions.createNode: CommandMetadata(
        type_argument="node_type",
        nullable_flags=("shared", "s"),
        node_arguments=("parent", "p"),
    ),
    extensions.polyPlane: CommandMetadata(
        primitive_history_type="PolyPlane",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyCone: CommandMetadata(
        primitive_history_type="PolyCone",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyCylinder: CommandMetadata(
        primitive_history_type="PolyCylinder",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyCube: CommandMetadata(
        primitive_history_type="PolyCube",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polySphere: CommandMetadata(
        primitive_history_type="PolySphere",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyTorus: CommandMetadata(
        primitive_history_type="PolyTorus",
        flag_types={"axis": "tuple[float, float, float] | bool", "twist": "float"},
        node_targets=True,
    ),
    extensions.polyPipe: CommandMetadata(
        primitive_history_type="PolyPipe",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyPyramid: CommandMetadata(
        primitive_history_type="PolyPyramid",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyPrism: CommandMetadata(
        primitive_history_type="PolyPrism",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyHelix: CommandMetadata(
        primitive_history_type="PolyHelix",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyPlatonicSolid: CommandMetadata(
        primitive_history_type="PolyPlatonicSolid",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyPrimitive: CommandMetadata(
        primitive_history_type="PolyPrimitiveMisc",
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.ls: CommandMetadata(
        flag_types={
            "containerType": "str | list[str] | tuple[str, ...]",
            **{
                flag: "str | type[Node] | Sequence[str | type[Node]]"
                for flag in ("exactType", "excludeType", "type")
            },
        },
        target_type="str | Node | Sequence[str | Node]",
    ),
}
