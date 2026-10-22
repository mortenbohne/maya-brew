from collections.abc import Sequence
from typing import Literal, TypedDict, Unpack, overload

from maya_brew.nodes._foundation.node_extensions import Node

class _LsFilterFlags(TypedDict, total=False):
    absoluteName: bool
    an: bool
    allPaths: bool
    ap: bool
    assemblies: bool
    cameras: bool
    ca: bool
    containers: bool
    con: bool
    containerType: str | list[str] | tuple[str, ...]
    ct: str | list[str] | tuple[str, ...]
    dagObjects: bool
    dag: bool
    dependencyNodes: bool
    dep: bool
    defaultNodes: bool
    dn: bool
    exactType: str | type[Node] | Sequence[str | type[Node]]
    et: str | type[Node] | Sequence[str | type[Node]]
    excludeType: str | type[Node] | Sequence[str | type[Node]]
    ext: str | type[Node] | Sequence[str | type[Node]]
    flatten: bool
    fl: bool
    geometry: bool
    g: bool
    ghost: bool
    gh: bool
    head: int
    hd: int
    hilite: bool
    hl: bool
    intermediateObjects: bool
    io: bool
    invisible: bool
    iv: bool
    long: bool
    l: bool
    leaf: bool
    lf: bool
    lockedNodes: bool
    ln: bool
    lights: bool
    lt: bool
    live: bool
    lv: bool
    materials: bool
    mat: bool
    modified: bool
    mod: bool
    noIntermediate: bool
    ni: bool
    orderedComponentSelection: bool
    ocs: bool
    orderedSelection: bool
    os: bool
    planes: bool
    pl: bool
    persistentNodes: bool
    pn: bool
    partitions: bool
    pr: bool
    preSelectHilite: bool
    psh: bool
    recursive: bool
    r: bool
    references: bool
    rf: bool
    renderGlobals: bool
    rg: bool
    referencedNodes: bool
    rn: bool
    readOnly: bool
    ro: bool
    renderQualities: bool
    rq: bool
    renderResolutions: bool
    rr: bool
    renderSetups: bool
    rs: bool
    shapes: bool
    s: bool
    sets: bool
    set: bool
    selection: bool
    sl: bool
    shortNames: bool
    sn: bool
    textures: bool
    tex: bool
    tail: int
    tl: int
    templated: bool
    tm: bool
    transforms: bool
    tr: bool
    type: str | type[Node] | Sequence[str | type[Node]]
    typ: str | type[Node] | Sequence[str | type[Node]]
    undeletable: bool
    ud: bool
    untemplated: bool
    ut: bool
    visible: bool
    v: bool

class _LsMetadataFlags(_LsFilterFlags, total=False):
    objectsOnly: bool
    o: bool
    showType: bool
    st: bool
    showNamespace: bool
    sns: bool
    ufeObjects: bool
    ufe: bool

class _LsNodeFlags(_LsFilterFlags, total=False):
    uuid: Literal[False]
    uid: Literal[False]
    nodeTypes: Literal[False]
    nt: Literal[False]
    showType: Literal[False]
    st: Literal[False]
    showNamespace: Literal[False]
    sns: Literal[False]
    ufeObjects: Literal[False]
    ufe: Literal[False]

class _LsFlags(_LsMetadataFlags, total=False):
    uuid: bool
    uid: bool
    nodeTypes: bool
    nt: bool

@overload
def ls(
    *args: str | Node | Sequence[str | Node],
    uuid: Literal[True],
    uid: bool = ...,
    nodeTypes: bool = ...,
    nt: bool = ...,
    **kwargs: Unpack[_LsMetadataFlags],
) -> list[str]: ...
@overload
def ls(
    *args: str | Node | Sequence[str | Node],
    uid: Literal[True],
    uuid: bool = ...,
    nodeTypes: bool = ...,
    nt: bool = ...,
    **kwargs: Unpack[_LsMetadataFlags],
) -> list[str]: ...
@overload
def ls(
    *args: str | Node | Sequence[str | Node],
    nodeTypes: Literal[True],
    nt: bool = ...,
    uuid: bool = ...,
    uid: bool = ...,
    **kwargs: Unpack[_LsMetadataFlags],
) -> list[str]: ...
@overload
def ls(
    *args: str | Node | Sequence[str | Node],
    nt: Literal[True],
    nodeTypes: bool = ...,
    uuid: bool = ...,
    uid: bool = ...,
    **kwargs: Unpack[_LsMetadataFlags],
) -> list[str]: ...
@overload
def ls(
    *args: str | Node | Sequence[str | Node],
    objectsOnly: Literal[True],
    o: bool = ...,
    **kwargs: Unpack[_LsNodeFlags],
) -> list[Node]: ...
@overload
def ls(
    *args: str | Node | Sequence[str | Node],
    o: Literal[True],
    objectsOnly: bool = ...,
    **kwargs: Unpack[_LsNodeFlags],
) -> list[Node]: ...
@overload
def ls(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_LsFlags],
) -> list[Node | str]: ...
