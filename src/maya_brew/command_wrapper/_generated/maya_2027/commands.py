# AUTO-GENERATED; DO NOT EDIT.
# @generated
from maya_brew.command_wrapper.extensions import UNSET, Unset
from maya_brew.command_wrapper import extensions as extensions
from maya_brew.nodes._foundation.node_extensions import Node


def createNode(
    node_type: str | type[Node],
    *,
    name: str | Unset = UNSET,
    n: str | Unset = UNSET,
    parent: str | Node | Unset = UNSET,
    p: str | Node | Unset = UNSET,
    shared: bool | Unset = UNSET,
    s: bool | Unset = UNSET,
    skipSelect: bool | Unset = UNSET,
    ss: bool | Unset = UNSET,
) -> Node | None:
    kwargs = {
        "name": name,
        "n": n,
        "parent": parent,
        "p": p,
        "shared": shared,
        "s": s,
        "skipSelect": skipSelect,
        "ss": ss,
    }
    return extensions.createNode(
        node_type,
        **{flag: value for flag, value in kwargs.items() if value is not UNSET},
    )


__all__ = ["createNode"]
