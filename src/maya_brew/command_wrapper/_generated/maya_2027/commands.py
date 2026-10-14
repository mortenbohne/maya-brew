# AUTO-GENERATED; DO NOT EDIT.
# @generated
from typing import Any
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


def polyPlane(
    *args: str | Node,
    edit: bool | Unset = UNSET,
    e: bool | Unset = UNSET,
    query: bool | Unset = UNSET,
    q: bool | Unset = UNSET,
    axis: tuple[float, float, float] | bool | Unset = UNSET,
    ax: tuple[float, float, float] | bool | Unset = UNSET,
    caching: bool | Unset = UNSET,
    cch: bool | Unset = UNSET,
    constructionHistory: bool | Unset = UNSET,
    ch: bool | Unset = UNSET,
    componentTagCreate: bool | Unset = UNSET,
    ctc: bool | Unset = UNSET,
    createUVs: int | Unset = UNSET,
    cuv: int | Unset = UNSET,
    frozen: bool | Unset = UNSET,
    fzn: bool | Unset = UNSET,
    height: float | Unset = UNSET,
    h: float | Unset = UNSET,
    heightBaseline: float | Unset = UNSET,
    hbl: float | Unset = UNSET,
    name: str | Unset = UNSET,
    n: str | Unset = UNSET,
    nodeState: int | Unset = UNSET,
    nds: int | Unset = UNSET,
    object: bool | Unset = UNSET,
    o: bool | Unset = UNSET,
    subdivisionsHeight: int | Unset = UNSET,
    sh: int | Unset = UNSET,
    subdivisionsWidth: int | Unset = UNSET,
    sw: int | Unset = UNSET,
    subdivisionsX: int | Unset = UNSET,
    sx: int | Unset = UNSET,
    subdivisionsY: int | Unset = UNSET,
    sy: int | Unset = UNSET,
    texture: int | Unset = UNSET,
    tx: int | Unset = UNSET,
    width: float | Unset = UNSET,
    w: float | Unset = UNSET,
) -> Any:
    kwargs = {
        "edit": edit,
        "e": e,
        "query": query,
        "q": q,
        "axis": axis,
        "ax": ax,
        "caching": caching,
        "cch": cch,
        "constructionHistory": constructionHistory,
        "ch": ch,
        "componentTagCreate": componentTagCreate,
        "ctc": ctc,
        "createUVs": createUVs,
        "cuv": cuv,
        "frozen": frozen,
        "fzn": fzn,
        "height": height,
        "h": h,
        "heightBaseline": heightBaseline,
        "hbl": hbl,
        "name": name,
        "n": n,
        "nodeState": nodeState,
        "nds": nds,
        "object": object,
        "o": o,
        "subdivisionsHeight": subdivisionsHeight,
        "sh": sh,
        "subdivisionsWidth": subdivisionsWidth,
        "sw": sw,
        "subdivisionsX": subdivisionsX,
        "sx": sx,
        "subdivisionsY": subdivisionsY,
        "sy": sy,
        "texture": texture,
        "tx": tx,
        "width": width,
        "w": w,
    }
    return extensions.polyPlane(
        *args,
        **{flag: value for flag, value in kwargs.items() if value is not UNSET},
    )


__all__ = ["createNode", "polyPlane"]
