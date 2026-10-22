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


COMMANDS: dict[Callable[..., Any], CommandMetadata] = {
    extensions.createNode: CommandMetadata(
        type_argument="node_type",
        nullable_flags=("shared", "s"),
        node_arguments=("parent", "p"),
    ),
    extensions.polyPlane: CommandMetadata(
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyCone: CommandMetadata(
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyCylinder: CommandMetadata(
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyCube: CommandMetadata(
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polySphere: CommandMetadata(
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyTorus: CommandMetadata(
        flag_types={"axis": "tuple[float, float, float] | bool", "twist": "float"},
        node_targets=True,
    ),
    extensions.polyPipe: CommandMetadata(
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyPyramid: CommandMetadata(
        flag_types={"axis": "tuple[float, float, float] | bool"},
        node_targets=True,
    ),
    extensions.polyPrism: CommandMetadata(
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
