# AUTO-GENERATED; DO NOT EDIT.
# @generated
from .concrete_nodes import ConcreteNode
from collections.abc import Sequence
from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import PolyCone, PolyCube, PolyCylinder, PolyPlane, PolyPyramid, PolySphere, Transform
from typing import Any, Literal, TypeAlias, TypeVar, TypedDict, Unpack, overload

T = TypeVar("T", bound=ConcreteNode)


@overload
def createNode(node_type: type[T], *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: Literal[False] = False, s: Literal[False] = False, skipSelect: bool = ..., ss: bool = ...) -> T: ...


@overload
def createNode(node_type: type[T], *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: bool = False, s: bool = False, skipSelect: bool = ..., ss: bool = ...) -> T | None: ...


@overload
def createNode(node_type: str, *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: bool = False, s: bool = False, skipSelect: bool = ..., ss: bool = ...) -> Node | None: ...




_LsTypeFilter: TypeAlias = str | type[Node] | Sequence[str | type[Node]]

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
    exactType: _LsTypeFilter
    et: _LsTypeFilter
    excludeType: _LsTypeFilter
    ext: _LsTypeFilter
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
    type: _LsTypeFilter
    typ: _LsTypeFilter
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




class _PolyConeModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    height: float
    h: float
    heightBaseline: float
    hbl: float
    name: str
    n: str
    object: bool
    o: bool
    radius: float
    r: float
    roundCap: bool
    rcp: bool
    subdivisionsAxis: int
    sa: int
    subdivisionsCap: int
    sc: int
    subdivisionsHeight: int
    sh: int
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    subdivisionsZ: int
    sz: int
    texture: bool
    tx: bool

class _PolyConeCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    height: float
    h: float
    heightBaseline: float
    hbl: float
    name: str
    n: str
    nodeState: int
    nds: int
    radius: float
    r: float
    roundCap: bool
    rcp: bool
    subdivisionsAxis: int
    sa: int
    subdivisionsCap: int
    sc: int
    subdivisionsHeight: int
    sh: int
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    subdivisionsZ: int
    sz: int
    texture: bool
    tx: bool

@overload
def polyCone(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyConeCreateFlags],
) -> tuple[PolyCone]: ...
@overload
def polyCone(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyConeCreateFlags],
) -> tuple[PolyCone]: ...
@overload
def polyCone(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyConeCreateFlags],
) -> tuple[Transform]: ...
@overload
def polyCone(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyConeCreateFlags],
) -> tuple[Transform]: ...
@overload
def polyCone(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyConeCreateFlags],
) -> tuple[Transform, PolyCone]: ...
@overload
def polyCone(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyConeCreateFlags],
) -> tuple[Transform, PolyCone] | tuple[Transform] | tuple[PolyCone]: ...
@overload
def polyCone(
    *args: str | PolyCone | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyConeModeFlags],
) -> NodeState: ...
@overload
def polyCone(
    *args: str | PolyCone | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyConeModeFlags],
) -> NodeState: ...
@overload
def polyCone(
    *args: str | PolyCone | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyConeModeFlags],
) -> NodeState: ...
@overload
def polyCone(
    *args: str | PolyCone | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyConeModeFlags],
) -> NodeState: ...
@overload
def polyCone(
    *args: str | PolyCone | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyConeModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polyCone(
    *args: str | PolyCone | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyConeModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polyCone(
    *args: str | PolyCone | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyConeModeFlags],
) -> Any: ...




class _PolyCubeModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    heightBaseline: float
    hbl: float
    name: str
    n: str
    object: bool
    o: bool
    depth: float
    d: float
    height: float
    h: float
    width: float
    w: float
    subdivisionsDepth: int
    sd: int
    subdivisionsHeight: int
    sh: int
    subdivisionsWidth: int
    sw: int
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    subdivisionsZ: int
    sz: int
    texture: int
    tx: int

class _PolyCubeCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    heightBaseline: float
    hbl: float
    name: str
    n: str
    nodeState: int
    nds: int
    depth: float
    d: float
    height: float
    h: float
    width: float
    w: float
    subdivisionsDepth: int
    sd: int
    subdivisionsHeight: int
    sh: int
    subdivisionsWidth: int
    sw: int
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    subdivisionsZ: int
    sz: int
    texture: int
    tx: int

@overload
def polyCube(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyCubeCreateFlags],
) -> tuple[PolyCube]: ...
@overload
def polyCube(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyCubeCreateFlags],
) -> tuple[PolyCube]: ...
@overload
def polyCube(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyCubeCreateFlags],
) -> tuple[Transform]: ...
@overload
def polyCube(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyCubeCreateFlags],
) -> tuple[Transform]: ...
@overload
def polyCube(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyCubeCreateFlags],
) -> tuple[Transform, PolyCube]: ...
@overload
def polyCube(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyCubeCreateFlags],
) -> tuple[Transform, PolyCube] | tuple[Transform] | tuple[PolyCube]: ...
@overload
def polyCube(
    *args: str | PolyCube | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyCubeModeFlags],
) -> NodeState: ...
@overload
def polyCube(
    *args: str | PolyCube | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyCubeModeFlags],
) -> NodeState: ...
@overload
def polyCube(
    *args: str | PolyCube | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyCubeModeFlags],
) -> NodeState: ...
@overload
def polyCube(
    *args: str | PolyCube | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyCubeModeFlags],
) -> NodeState: ...
@overload
def polyCube(
    *args: str | PolyCube | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyCubeModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polyCube(
    *args: str | PolyCube | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyCubeModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polyCube(
    *args: str | PolyCube | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyCubeModeFlags],
) -> Any: ...




class _PolyCylinderModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    height: float
    h: float
    heightBaseline: float
    hbl: float
    name: str
    n: str
    object: bool
    o: bool
    radius: float
    r: float
    roundCapHeightCompensation: bool
    rch: bool
    roundCap: bool
    rcp: bool
    subdivisionsAxis: int
    sa: int
    subdivisionsCaps: int
    sc: int
    subdivisionsHeight: int
    sh: int
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    subdivisionsZ: int
    sz: int
    texture: int
    tx: int

class _PolyCylinderCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    height: float
    h: float
    heightBaseline: float
    hbl: float
    name: str
    n: str
    nodeState: int
    nds: int
    radius: float
    r: float
    roundCapHeightCompensation: bool
    rch: bool
    roundCap: bool
    rcp: bool
    subdivisionsAxis: int
    sa: int
    subdivisionsCaps: int
    sc: int
    subdivisionsHeight: int
    sh: int
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    subdivisionsZ: int
    sz: int
    texture: int
    tx: int

@overload
def polyCylinder(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyCylinderCreateFlags],
) -> tuple[PolyCylinder]: ...
@overload
def polyCylinder(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyCylinderCreateFlags],
) -> tuple[PolyCylinder]: ...
@overload
def polyCylinder(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyCylinderCreateFlags],
) -> tuple[Transform]: ...
@overload
def polyCylinder(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyCylinderCreateFlags],
) -> tuple[Transform]: ...
@overload
def polyCylinder(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyCylinderCreateFlags],
) -> tuple[Transform, PolyCylinder]: ...
@overload
def polyCylinder(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyCylinderCreateFlags],
) -> tuple[Transform, PolyCylinder] | tuple[Transform] | tuple[PolyCylinder]: ...
@overload
def polyCylinder(
    *args: str | PolyCylinder | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyCylinderModeFlags],
) -> NodeState: ...
@overload
def polyCylinder(
    *args: str | PolyCylinder | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyCylinderModeFlags],
) -> NodeState: ...
@overload
def polyCylinder(
    *args: str | PolyCylinder | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyCylinderModeFlags],
) -> NodeState: ...
@overload
def polyCylinder(
    *args: str | PolyCylinder | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyCylinderModeFlags],
) -> NodeState: ...
@overload
def polyCylinder(
    *args: str | PolyCylinder | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyCylinderModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polyCylinder(
    *args: str | PolyCylinder | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyCylinderModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polyCylinder(
    *args: str | PolyCylinder | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyCylinderModeFlags],
) -> Any: ...




class _PolyPlaneModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    height: float
    h: float
    heightBaseline: float
    hbl: float
    name: str
    n: str
    object: bool
    o: bool
    subdivisionsHeight: int
    sh: int
    subdivisionsWidth: int
    sw: int
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    texture: int
    tx: int
    width: float
    w: float

class _PolyPlaneCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    height: float
    h: float
    heightBaseline: float
    hbl: float
    name: str
    n: str
    nodeState: int
    nds: int
    subdivisionsHeight: int
    sh: int
    subdivisionsWidth: int
    sw: int
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    texture: int
    tx: int
    width: float
    w: float

@overload
def polyPlane(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPlaneCreateFlags],
) -> tuple[PolyPlane]: ...
@overload
def polyPlane(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPlaneCreateFlags],
) -> tuple[PolyPlane]: ...
@overload
def polyPlane(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPlaneCreateFlags],
) -> tuple[Transform]: ...
@overload
def polyPlane(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPlaneCreateFlags],
) -> tuple[Transform]: ...
@overload
def polyPlane(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPlaneCreateFlags],
) -> tuple[Transform, PolyPlane]: ...
@overload
def polyPlane(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyPlaneCreateFlags],
) -> tuple[Transform, PolyPlane] | tuple[Transform] | tuple[PolyPlane]: ...
@overload
def polyPlane(
    *args: str | PolyPlane | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPlaneModeFlags],
) -> NodeState: ...
@overload
def polyPlane(
    *args: str | PolyPlane | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPlaneModeFlags],
) -> NodeState: ...
@overload
def polyPlane(
    *args: str | PolyPlane | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPlaneModeFlags],
) -> NodeState: ...
@overload
def polyPlane(
    *args: str | PolyPlane | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPlaneModeFlags],
) -> NodeState: ...
@overload
def polyPlane(
    *args: str | PolyPlane | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPlaneModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polyPlane(
    *args: str | PolyPlane | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPlaneModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polyPlane(
    *args: str | PolyPlane | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPlaneModeFlags],
) -> Any: ...




class _PolyPyramidModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    heightBaseline: float
    hbl: float
    name: str
    n: str
    object: bool
    o: bool
    numberOfSides: int
    ns: int
    numderOfSides: int
    nsi: int
    sideLength: float
    w: float
    subdivisionsCaps: int
    sc: int
    subdivisionsHeight: int
    sh: int
    texture: bool
    tx: bool

class _PolyPyramidCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    heightBaseline: float
    hbl: float
    name: str
    n: str
    nodeState: int
    nds: int
    numberOfSides: int
    ns: int
    numderOfSides: int
    nsi: int
    sideLength: float
    w: float
    subdivisionsCaps: int
    sc: int
    subdivisionsHeight: int
    sh: int
    texture: bool
    tx: bool

@overload
def polyPyramid(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPyramidCreateFlags],
) -> tuple[PolyPyramid]: ...
@overload
def polyPyramid(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPyramidCreateFlags],
) -> tuple[PolyPyramid]: ...
@overload
def polyPyramid(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPyramidCreateFlags],
) -> tuple[Transform]: ...
@overload
def polyPyramid(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPyramidCreateFlags],
) -> tuple[Transform]: ...
@overload
def polyPyramid(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPyramidCreateFlags],
) -> tuple[Transform, PolyPyramid]: ...
@overload
def polyPyramid(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyPyramidCreateFlags],
) -> tuple[Transform, PolyPyramid] | tuple[Transform] | tuple[PolyPyramid]: ...
@overload
def polyPyramid(
    *args: str | PolyPyramid | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPyramidModeFlags],
) -> NodeState: ...
@overload
def polyPyramid(
    *args: str | PolyPyramid | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPyramidModeFlags],
) -> NodeState: ...
@overload
def polyPyramid(
    *args: str | PolyPyramid | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPyramidModeFlags],
) -> NodeState: ...
@overload
def polyPyramid(
    *args: str | PolyPyramid | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPyramidModeFlags],
) -> NodeState: ...
@overload
def polyPyramid(
    *args: str | PolyPyramid | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPyramidModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polyPyramid(
    *args: str | PolyPyramid | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPyramidModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polyPyramid(
    *args: str | PolyPyramid | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPyramidModeFlags],
) -> Any: ...




class _PolySphereModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    heightBaseline: float
    hbl: float
    name: str
    n: str
    object: bool
    o: bool
    radius: float
    r: float
    subdivisionsAxis: int
    sa: int
    subdivisionsHeight: int
    sh: int
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    texture: int
    tx: int

class _PolySphereCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    frozen: bool
    fzn: bool
    heightBaseline: float
    hbl: float
    name: str
    n: str
    nodeState: int
    nds: int
    radius: float
    r: float
    subdivisionsAxis: int
    sa: int
    subdivisionsHeight: int
    sh: int
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    texture: int
    tx: int

@overload
def polySphere(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolySphereCreateFlags],
) -> tuple[PolySphere]: ...
@overload
def polySphere(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolySphereCreateFlags],
) -> tuple[PolySphere]: ...
@overload
def polySphere(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolySphereCreateFlags],
) -> tuple[Transform]: ...
@overload
def polySphere(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolySphereCreateFlags],
) -> tuple[Transform]: ...
@overload
def polySphere(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolySphereCreateFlags],
) -> tuple[Transform, PolySphere]: ...
@overload
def polySphere(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolySphereCreateFlags],
) -> tuple[Transform, PolySphere] | tuple[Transform] | tuple[PolySphere]: ...
@overload
def polySphere(
    *args: str | PolySphere | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolySphereModeFlags],
) -> NodeState: ...
@overload
def polySphere(
    *args: str | PolySphere | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolySphereModeFlags],
) -> NodeState: ...
@overload
def polySphere(
    *args: str | PolySphere | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolySphereModeFlags],
) -> NodeState: ...
@overload
def polySphere(
    *args: str | PolySphere | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolySphereModeFlags],
) -> NodeState: ...
@overload
def polySphere(
    *args: str | PolySphere | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolySphereModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polySphere(
    *args: str | PolySphere | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolySphereModeFlags],
) -> Literal["Values edited."]: ...
@overload
def polySphere(
    *args: str | PolySphere | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolySphereModeFlags],
) -> Any: ...


__all__ = ["createNode", "ls", "polyCone", "polyCube", "polyCylinder", "polyPlane", "polyPyramid", "polySphere"]
