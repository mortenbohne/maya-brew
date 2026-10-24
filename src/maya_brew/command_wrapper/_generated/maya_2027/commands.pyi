# AUTO-GENERATED; DO NOT EDIT.
# @generated
from .concrete_nodes import ConcreteNode
from collections.abc import Sequence
from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import AmbientLight, DirectionalLight, IkEffector, IkHandle, IkSolver, Joint, MakeNurbCircle, MakeNurbCone, MakeNurbCube, MakeNurbCylinder, MakeNurbPlane, MakeNurbSphere, MakeNurbTorus, MakeNurbsSquare, PointLight, PolyCone, PolyCube, PolyCylinder, PolyHelix, PolyPipe, PolyPlane, PolyPlatonicSolid, PolyPrimitiveMisc, PolyPrism, PolyPyramid, PolySphere, PolyTorus, SpotLight, Transform
from typing import Any, Literal, Never, TypeAlias, TypeVar, TypedDict, Unpack, overload

T = TypeVar("T", bound=ConcreteNode)


class _AmbientLightFlags(TypedDict, total=False):
    ambientShade: float
    discRadius: float
    drs: float
    exclusive: bool
    exc: bool
    rgb: tuple[float, float, float]
    useRayTraceShadows: bool
    rs: bool
    shadowColor: tuple[float, float, float]
    sc: tuple[float, float, float]
    shadowDither: float
    sd: float
    shadowSamples: int
    sh: int
    softShadow: bool
    ss: bool

class _AmbientLightCreateFlags(_AmbientLightFlags, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    intensity: float
    i: float
    name: str
    n: str
    position: tuple[float, float, float]
    pos: tuple[float, float, float]
    rotation: tuple[float, float, float]
    rot: tuple[float, float, float]

class _AmbientLightModeFlags(_AmbientLightFlags, total=False):
    edit: bool
    e: bool
    query: bool
    q: bool
    intensity: float | bool
    i: float | bool
    name: str | bool
    n: str | bool
    position: tuple[float, float, float] | bool
    pos: tuple[float, float, float] | bool
    rotation: tuple[float, float, float] | bool
    rot: tuple[float, float, float] | bool

@overload
def ambientLight(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_AmbientLightCreateFlags],
) -> AmbientLight: ...

@overload
def ambientLight(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_AmbientLightModeFlags],
) -> Any: ...



class _CircleModeFlags(TypedDict, total=False):
    center: tuple[float, float, float]
    c: tuple[float, float, float]
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    centerX: float
    cx: float
    centerY: float
    cy: float
    centerZ: float
    cz: float
    degree: int
    d: int
    fixCenter: bool
    fc: bool
    first: tuple[float, float, float]
    fp: tuple[float, float, float]
    firstPointX: float
    fpx: float
    firstPointY: float
    fpy: float
    firstPointZ: float
    fpz: float
    frozen: bool
    fzn: bool
    name: str
    n: str
    normal: tuple[float, float, float]
    nr: tuple[float, float, float]
    normalX: float
    nrx: float
    normalY: float
    nry: float
    normalZ: float
    nrz: float
    object: bool
    o: bool
    radius: float
    r: float
    sections: int
    s: int
    sweep: float
    sw: float
    tolerance: float
    tol: float
    useTolerance: bool
    ut: bool

class _CircleCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    center: tuple[float, float, float]
    c: tuple[float, float, float]
    caching: bool
    cch: bool
    centerX: float
    cx: float
    centerY: float
    cy: float
    centerZ: float
    cz: float
    degree: int
    d: int
    fixCenter: bool
    fc: bool
    first: tuple[float, float, float]
    fp: tuple[float, float, float]
    firstPointX: float
    fpx: float
    firstPointY: float
    fpy: float
    firstPointZ: float
    fpz: float
    frozen: bool
    fzn: bool
    name: str
    n: str
    nodeState: int
    nds: int
    normal: tuple[float, float, float]
    nr: tuple[float, float, float]
    normalX: float
    nrx: float
    normalY: float
    nry: float
    normalZ: float
    nrz: float
    radius: float
    r: float
    sections: int
    s: int
    sweep: float
    sw: float
    tolerance: float
    tol: float
    useTolerance: bool
    ut: bool

@overload
def circle(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_CircleCreateFlags],
) -> tuple[MakeNurbCircle]: ...

@overload
def circle(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_CircleCreateFlags],
) -> tuple[MakeNurbCircle]: ...

@overload
def circle(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_CircleCreateFlags],
) -> tuple[Transform]: ...

@overload
def circle(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_CircleCreateFlags],
) -> tuple[Transform]: ...

@overload
def circle(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_CircleCreateFlags],
) -> tuple[Transform, MakeNurbCircle]: ...

@overload
def circle(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_CircleCreateFlags],
) -> tuple[Transform, MakeNurbCircle] | tuple[Transform] | tuple[MakeNurbCircle]: ...

@overload
def circle(
    *args: str | MakeNurbCircle | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_CircleModeFlags],
) -> NodeState: ...

@overload
def circle(
    *args: str | MakeNurbCircle | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_CircleModeFlags],
) -> NodeState: ...

@overload
def circle(
    *args: str | MakeNurbCircle | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_CircleModeFlags],
) -> NodeState: ...

@overload
def circle(
    *args: str | MakeNurbCircle | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_CircleModeFlags],
) -> NodeState: ...

@overload
def circle(
    *args: str | MakeNurbCircle | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_CircleModeFlags],
) -> Literal["Values edited."]: ...

@overload
def circle(
    *args: str | MakeNurbCircle | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_CircleModeFlags],
) -> Literal["Values edited."]: ...

@overload
def circle(
    *args: str | MakeNurbCircle | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_CircleModeFlags],
) -> Any: ...



class _ConeModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    degree: int
    d: int
    endSweep: float
    esw: float
    frozen: bool
    fzn: bool
    heightRatio: float
    hr: float
    name: str
    n: str
    spans: int
    nsp: int
    object: bool
    o: bool
    useOldInitBehaviour: bool
    oib: bool
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    radius: float
    r: float
    sections: int
    s: int
    startSweep: float
    ssw: float
    tolerance: float
    tol: float
    useTolerance: bool
    ut: bool

class _ConeCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    degree: int
    d: int
    endSweep: float
    esw: float
    frozen: bool
    fzn: bool
    heightRatio: float
    hr: float
    name: str
    n: str
    nodeState: int
    nds: int
    spans: int
    nsp: int
    useOldInitBehaviour: bool
    oib: bool
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    radius: float
    r: float
    sections: int
    s: int
    startSweep: float
    ssw: float
    tolerance: float
    tol: float
    useTolerance: bool
    ut: bool

@overload
def cone(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_ConeCreateFlags],
) -> tuple[MakeNurbCone]: ...

@overload
def cone(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_ConeCreateFlags],
) -> tuple[MakeNurbCone]: ...

@overload
def cone(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_ConeCreateFlags],
) -> tuple[Transform]: ...

@overload
def cone(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_ConeCreateFlags],
) -> tuple[Transform]: ...

@overload
def cone(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_ConeCreateFlags],
) -> tuple[Transform, MakeNurbCone]: ...

@overload
def cone(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_ConeCreateFlags],
) -> tuple[Transform, MakeNurbCone] | tuple[Transform] | tuple[MakeNurbCone]: ...

@overload
def cone(
    *args: str | MakeNurbCone | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_ConeModeFlags],
) -> NodeState: ...

@overload
def cone(
    *args: str | MakeNurbCone | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_ConeModeFlags],
) -> NodeState: ...

@overload
def cone(
    *args: str | MakeNurbCone | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_ConeModeFlags],
) -> NodeState: ...

@overload
def cone(
    *args: str | MakeNurbCone | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_ConeModeFlags],
) -> NodeState: ...

@overload
def cone(
    *args: str | MakeNurbCone | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_ConeModeFlags],
) -> Literal["Values edited."]: ...

@overload
def cone(
    *args: str | MakeNurbCone | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_ConeModeFlags],
) -> Literal["Values edited."]: ...

@overload
def cone(
    *args: str | MakeNurbCone | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_ConeModeFlags],
) -> Any: ...


def connectJoint(*args: str | Node | Sequence[str | Node], connectMode: bool = ..., cm: bool = ..., parentMode: bool = ..., pm: bool = ...) -> None: ...


@overload
def createNode(node_type: type[T], *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: Literal[False] = False, s: Literal[False] = False, skipSelect: bool = ..., ss: bool = ...) -> T: ...


@overload
def createNode(node_type: type[T], *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: bool = False, s: bool = False, skipSelect: bool = ..., ss: bool = ...) -> T | None: ...


@overload
def createNode(node_type: str, *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: bool = False, s: bool = False, skipSelect: bool = ..., ss: bool = ...) -> Node | None: ...



class _CylinderModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    degree: int
    d: int
    endSweep: float
    esw: float
    frozen: bool
    fzn: bool
    heightRatio: float
    hr: float
    name: str
    n: str
    spans: int
    nsp: int
    object: bool
    o: bool
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    radius: float
    r: float
    sections: int
    s: int
    startSweep: float
    ssw: float
    tolerance: float
    tol: float
    useTolerance: bool
    ut: bool

class _CylinderCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    degree: int
    d: int
    endSweep: float
    esw: float
    frozen: bool
    fzn: bool
    heightRatio: float
    hr: float
    name: str
    n: str
    nodeState: int
    nds: int
    spans: int
    nsp: int
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    radius: float
    r: float
    sections: int
    s: int
    startSweep: float
    ssw: float
    tolerance: float
    tol: float
    useTolerance: bool
    ut: bool

@overload
def cylinder(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_CylinderCreateFlags],
) -> tuple[MakeNurbCylinder]: ...

@overload
def cylinder(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_CylinderCreateFlags],
) -> tuple[MakeNurbCylinder]: ...

@overload
def cylinder(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_CylinderCreateFlags],
) -> tuple[Transform]: ...

@overload
def cylinder(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_CylinderCreateFlags],
) -> tuple[Transform]: ...

@overload
def cylinder(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_CylinderCreateFlags],
) -> tuple[Transform, MakeNurbCylinder]: ...

@overload
def cylinder(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_CylinderCreateFlags],
) -> tuple[Transform, MakeNurbCylinder] | tuple[Transform] | tuple[MakeNurbCylinder]: ...

@overload
def cylinder(
    *args: str | MakeNurbCylinder | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_CylinderModeFlags],
) -> NodeState: ...

@overload
def cylinder(
    *args: str | MakeNurbCylinder | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_CylinderModeFlags],
) -> NodeState: ...

@overload
def cylinder(
    *args: str | MakeNurbCylinder | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_CylinderModeFlags],
) -> NodeState: ...

@overload
def cylinder(
    *args: str | MakeNurbCylinder | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_CylinderModeFlags],
) -> NodeState: ...

@overload
def cylinder(
    *args: str | MakeNurbCylinder | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_CylinderModeFlags],
) -> Literal["Values edited."]: ...

@overload
def cylinder(
    *args: str | MakeNurbCylinder | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_CylinderModeFlags],
) -> Literal["Values edited."]: ...

@overload
def cylinder(
    *args: str | MakeNurbCylinder | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_CylinderModeFlags],
) -> Any: ...


class _DirectionalLightFlags(TypedDict, total=False):
    discRadius: float
    drs: float
    exclusive: bool
    exc: bool
    rgb: tuple[float, float, float]
    useRayTraceShadows: bool
    rs: bool
    shadowColor: tuple[float, float, float]
    sc: tuple[float, float, float]
    shadowDither: float
    sd: float
    shadowSamples: int
    sh: int
    softShadow: bool
    ss: bool

class _DirectionalLightCreateFlags(_DirectionalLightFlags, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    decayRate: int
    d: int
    intensity: float
    i: float
    name: str
    n: str
    position: tuple[float, float, float]
    pos: tuple[float, float, float]
    rotation: tuple[float, float, float]
    rot: tuple[float, float, float]

class _DirectionalLightModeFlags(_DirectionalLightFlags, total=False):
    edit: bool
    e: bool
    query: bool
    q: bool
    decayRate: int | bool
    d: int | bool
    intensity: float | bool
    i: float | bool
    name: str | bool
    n: str | bool
    position: tuple[float, float, float] | bool
    pos: tuple[float, float, float] | bool
    rotation: tuple[float, float, float] | bool
    rot: tuple[float, float, float] | bool

@overload
def directionalLight(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_DirectionalLightCreateFlags],
) -> DirectionalLight: ...

@overload
def directionalLight(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_DirectionalLightModeFlags],
) -> Any: ...


class _IkHandleFlags(TypedDict, total=False):
    autoPriority: bool
    ap: bool
    createCurve: bool
    ccv: bool
    connectEffector: bool
    ce: bool
    createRootAxis: bool
    cra: bool
    disableHandles: bool
    dh: bool
    enableHandles: bool
    eh: bool
    freezeJoints: bool
    fj: bool
    forceSolver: bool
    fs: bool
    jointList: bool
    jl: bool
    numSpans: int
    ns: int
    priority: int
    p: int
    parentCurve: bool
    pcv: bool
    positionWeight: float
    pw: float
    rootOnCurve: bool
    roc: bool
    rootTwistMode: bool
    rtm: bool
    simplifyCurve: bool
    scv: bool
    snapHandleToEffector: bool
    see: bool
    snapHandleFlagToggle: bool
    shf: bool
    snapCurve: bool
    snc: bool
    setupForRPsolver: bool
    srp: bool
    weight: float
    w: float

class _IkHandleCreateFlags(_IkHandleFlags, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    curve: str | Node
    c: str | Node
    endEffector: str | Node
    ee: str | Node
    name: str
    n: str
    sticky: str
    s: str
    startJoint: str | Node
    sj: str | Node
    solver: str | Node
    sol: str | Node
    twistType: str
    tws: str

class _IkHandleModeFlags(_IkHandleFlags, total=False):
    edit: bool
    e: bool
    query: bool
    q: bool
    curve: str | Node | bool
    c: str | Node | bool
    endEffector: str | Node | bool
    ee: str | Node | bool
    name: str | bool
    n: str | bool
    sticky: str | bool
    s: str | bool
    startJoint: str | Node | bool
    sj: str | Node | bool
    solver: str | Node | bool
    sol: str | Node | bool
    twistType: str | bool
    tws: str | bool

@overload
def ikHandle(
    *args: str | Node | Sequence[str | Node],
    exists: Never = ...,
    ex: Never = ...,
    **kwargs: Unpack[_IkHandleCreateFlags],
) -> tuple[IkHandle] | tuple[IkHandle, IkEffector] | tuple[IkHandle, IkEffector, Transform]: ...

@overload
def ikHandle(
    *args: str | Node | Sequence[str | Node],
    exists: str | bool = ...,
    ex: str | bool = ...,
    **kwargs: Unpack[_IkHandleModeFlags],
) -> Any: ...


def ikHandleDisplayScale(*args: float, query: bool = ..., q: bool = ...) -> float | None: ...


class _IkSolverFlags(TypedDict, total=False):
    epsilon: float
    ep: float
    maxIterations: int
    mxi: int

class _IkSolverCreateFlags(_IkSolverFlags, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    name: str
    n: str
    solverType: str
    st: str

class _IkSolverModeFlags(_IkSolverFlags, total=False):
    edit: bool
    e: bool
    query: bool
    q: bool
    name: str | bool
    n: str | bool
    solverType: str | bool
    st: str | bool

@overload
def ikSolver(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_IkSolverCreateFlags],
) -> IkSolver: ...

@overload
def ikSolver(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_IkSolverModeFlags],
) -> Any: ...


def ikSystemInfo(*args: bool, query: bool = ..., q: bool = ..., globalSnapHandle: bool = ..., gsh: bool = ...) -> bool | None: ...


def insertJoint(*args: str | Node | Sequence[str | Node]) -> Joint: ...


class _JointFlags(TypedDict, total=False):
    absolute: bool
    a: bool
    automaticLimits: bool
    al: bool
    autoOrientSecondaryAxis: bool
    aos: bool
    assumePreferredAngles: bool
    apa: bool
    children: bool
    ch: bool
    component: bool
    co: bool
    limitSwitchX: bool
    lsx: bool
    limitSwitchY: bool
    lsy: bool
    limitSwitchZ: bool
    lsz: bool
    orientJoint: str
    oj: str
    relative: bool
    r: bool
    radius: float
    rad: float
    symmetryAxis: str
    sa: str
    secondaryAxisOrient: str
    sao: str
    scaleCompensate: bool
    sc: bool
    setPreferredAngles: bool
    spa: bool
    stiffnessX: float
    stx: float
    stiffnessY: float
    sty: float
    stiffnessZ: float
    stz: float
    symmetry: bool
    sym: bool
    zeroScaleOrient: bool
    zso: bool

class _JointCreateFlags(_JointFlags, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    angleX: float | str
    ax: float | str
    angleY: float | str
    ay: float | str
    angleZ: float | str
    az: float | str
    degreeOfFreedom: str
    dof: str
    limitX: tuple[float | str, float | str]
    lx: tuple[float | str, float | str]
    limitY: tuple[float | str, float | str]
    ly: tuple[float | str, float | str]
    limitZ: tuple[float | str, float | str]
    lz: tuple[float | str, float | str]
    name: str
    n: str
    orientation: tuple[float | str, float | str, float | str]
    o: tuple[float | str, float | str, float | str]
    position: tuple[float | str, float | str, float | str]
    p: tuple[float | str, float | str, float | str]
    rotationOrder: str
    roo: str
    scale: tuple[float, float, float]
    s: tuple[float, float, float]
    scaleOrientation: tuple[float | str, float | str, float | str]
    so: tuple[float | str, float | str, float | str]

class _JointModeFlags(_JointFlags, total=False):
    edit: bool
    e: bool
    query: bool
    q: bool
    angleX: float | str | bool
    ax: float | str | bool
    angleY: float | str | bool
    ay: float | str | bool
    angleZ: float | str | bool
    az: float | str | bool
    degreeOfFreedom: str | bool
    dof: str | bool
    limitX: tuple[float | str, float | str] | bool
    lx: tuple[float | str, float | str] | bool
    limitY: tuple[float | str, float | str] | bool
    ly: tuple[float | str, float | str] | bool
    limitZ: tuple[float | str, float | str] | bool
    lz: tuple[float | str, float | str] | bool
    name: str | bool
    n: str | bool
    orientation: tuple[float | str, float | str, float | str] | bool
    o: tuple[float | str, float | str, float | str] | bool
    position: tuple[float | str, float | str, float | str] | bool
    p: tuple[float | str, float | str, float | str] | bool
    rotationOrder: str | bool
    roo: str | bool
    scale: tuple[float, float, float] | bool
    s: tuple[float, float, float] | bool
    scaleOrientation: tuple[float | str, float | str, float | str] | bool
    so: tuple[float | str, float | str, float | str] | bool

@overload
def joint(
    *args: str | Node | Sequence[str | Node],
    exists: Never = ...,
    ex: Never = ...,
    **kwargs: Unpack[_JointCreateFlags],
) -> Joint: ...

@overload
def joint(
    *args: str | Node | Sequence[str | Node],
    exists: str | bool,
    ex: str | bool = ...,
    **kwargs: Unpack[_JointModeFlags],
) -> bool: ...

@overload
def joint(
    *args: str | Node | Sequence[str | Node],
    exists: str | bool = ...,
    ex: str | bool,
    **kwargs: Unpack[_JointModeFlags],
) -> bool: ...

@overload
def joint(
    *args: str | Node | Sequence[str | Node],
    exists: str | bool = ...,
    ex: str | bool = ...,
    **kwargs: Unpack[_JointModeFlags],
) -> Any: ...


def jointDisplayScale(*args: float, query: bool = ..., q: bool = ..., absolute: bool = ..., a: bool = ..., ikfk: float | bool = ..., ik: float | bool = ...) -> float | None: ...




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


def mirrorJoint(*args: str | Node | Sequence[str | Node], mirrorBehavior: bool = ..., mb: bool = ..., mirrorXY: bool = ..., mxy: bool = ..., mirrorXZ: bool = ..., mxz: bool = ..., mirrorYZ: bool = ..., myz: bool = ..., searchReplace: tuple[str, str] = ..., sr: tuple[str, str] = ...) -> tuple[Node, ...]: ...



class _NurbsCubeModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    degree: int
    d: int
    frozen: bool
    fzn: bool
    heightRatio: float
    hr: float
    lengthRatio: float
    lr: float
    name: str
    n: str
    object: bool
    o: bool
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    patchesU: int
    u: int
    patchesV: int
    v: int
    width: float
    w: float

class _NurbsCubeCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    degree: int
    d: int
    frozen: bool
    fzn: bool
    heightRatio: float
    hr: float
    lengthRatio: float
    lr: float
    name: str
    n: str
    nodeState: int
    nds: int
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    patchesU: int
    u: int
    patchesV: int
    v: int
    width: float
    w: float

@overload
def nurbsCube(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_NurbsCubeCreateFlags],
) -> tuple[MakeNurbCube]: ...

@overload
def nurbsCube(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_NurbsCubeCreateFlags],
) -> tuple[MakeNurbCube]: ...

@overload
def nurbsCube(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_NurbsCubeCreateFlags],
) -> tuple[Transform]: ...

@overload
def nurbsCube(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_NurbsCubeCreateFlags],
) -> tuple[Transform]: ...

@overload
def nurbsCube(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_NurbsCubeCreateFlags],
) -> tuple[Transform, MakeNurbCube]: ...

@overload
def nurbsCube(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_NurbsCubeCreateFlags],
) -> tuple[Transform, MakeNurbCube] | tuple[Transform] | tuple[MakeNurbCube]: ...

@overload
def nurbsCube(
    *args: str | MakeNurbCube | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsCubeModeFlags],
) -> NodeState: ...

@overload
def nurbsCube(
    *args: str | MakeNurbCube | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_NurbsCubeModeFlags],
) -> NodeState: ...

@overload
def nurbsCube(
    *args: str | MakeNurbCube | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsCubeModeFlags],
) -> NodeState: ...

@overload
def nurbsCube(
    *args: str | MakeNurbCube | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_NurbsCubeModeFlags],
) -> NodeState: ...

@overload
def nurbsCube(
    *args: str | MakeNurbCube | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsCubeModeFlags],
) -> Literal["Values edited."]: ...

@overload
def nurbsCube(
    *args: str | MakeNurbCube | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsCubeModeFlags],
) -> Literal["Values edited."]: ...

@overload
def nurbsCube(
    *args: str | MakeNurbCube | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsCubeModeFlags],
) -> Any: ...



class _NurbsPlaneModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    degree: int
    d: int
    frozen: bool
    fzn: bool
    lengthRatio: float
    lr: float
    name: str
    n: str
    object: bool
    o: bool
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    patchesU: int
    u: int
    patchesV: int
    v: int
    width: float
    w: float

class _NurbsPlaneCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    degree: int
    d: int
    frozen: bool
    fzn: bool
    lengthRatio: float
    lr: float
    name: str
    n: str
    nodeState: int
    nds: int
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    patchesU: int
    u: int
    patchesV: int
    v: int
    width: float
    w: float

@overload
def nurbsPlane(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_NurbsPlaneCreateFlags],
) -> tuple[MakeNurbPlane]: ...

@overload
def nurbsPlane(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_NurbsPlaneCreateFlags],
) -> tuple[MakeNurbPlane]: ...

@overload
def nurbsPlane(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_NurbsPlaneCreateFlags],
) -> tuple[Transform]: ...

@overload
def nurbsPlane(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_NurbsPlaneCreateFlags],
) -> tuple[Transform]: ...

@overload
def nurbsPlane(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_NurbsPlaneCreateFlags],
) -> tuple[Transform, MakeNurbPlane]: ...

@overload
def nurbsPlane(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_NurbsPlaneCreateFlags],
) -> tuple[Transform, MakeNurbPlane] | tuple[Transform] | tuple[MakeNurbPlane]: ...

@overload
def nurbsPlane(
    *args: str | MakeNurbPlane | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsPlaneModeFlags],
) -> NodeState: ...

@overload
def nurbsPlane(
    *args: str | MakeNurbPlane | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_NurbsPlaneModeFlags],
) -> NodeState: ...

@overload
def nurbsPlane(
    *args: str | MakeNurbPlane | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsPlaneModeFlags],
) -> NodeState: ...

@overload
def nurbsPlane(
    *args: str | MakeNurbPlane | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_NurbsPlaneModeFlags],
) -> NodeState: ...

@overload
def nurbsPlane(
    *args: str | MakeNurbPlane | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsPlaneModeFlags],
) -> Literal["Values edited."]: ...

@overload
def nurbsPlane(
    *args: str | MakeNurbPlane | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsPlaneModeFlags],
) -> Literal["Values edited."]: ...

@overload
def nurbsPlane(
    *args: str | MakeNurbPlane | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsPlaneModeFlags],
) -> Any: ...



class _NurbsSquareModeFlags(TypedDict, total=False):
    center: tuple[float, float, float]
    c: tuple[float, float, float]
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    centerX: float
    cx: float
    centerY: float
    cy: float
    centerZ: float
    cz: float
    degree: int
    d: int
    frozen: bool
    fzn: bool
    name: str
    n: str
    normal: tuple[float, float, float]
    nr: tuple[float, float, float]
    normalX: float
    nrx: float
    normalY: float
    nry: float
    normalZ: float
    nrz: float
    object: bool
    o: bool
    sideLength1: float
    sl1: float
    sideLength2: float
    sl2: float
    spansPerSide: int
    sps: int

class _NurbsSquareCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    center: tuple[float, float, float]
    c: tuple[float, float, float]
    caching: bool
    cch: bool
    centerX: float
    cx: float
    centerY: float
    cy: float
    centerZ: float
    cz: float
    degree: int
    d: int
    frozen: bool
    fzn: bool
    name: str
    n: str
    nodeState: int
    nds: int
    normal: tuple[float, float, float]
    nr: tuple[float, float, float]
    normalX: float
    nrx: float
    normalY: float
    nry: float
    normalZ: float
    nrz: float
    sideLength1: float
    sl1: float
    sideLength2: float
    sl2: float
    spansPerSide: int
    sps: int

@overload
def nurbsSquare(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_NurbsSquareCreateFlags],
) -> tuple[MakeNurbsSquare]: ...

@overload
def nurbsSquare(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_NurbsSquareCreateFlags],
) -> tuple[MakeNurbsSquare]: ...

@overload
def nurbsSquare(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_NurbsSquareCreateFlags],
) -> tuple[Transform]: ...

@overload
def nurbsSquare(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_NurbsSquareCreateFlags],
) -> tuple[Transform]: ...

@overload
def nurbsSquare(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_NurbsSquareCreateFlags],
) -> tuple[Transform, MakeNurbsSquare]: ...

@overload
def nurbsSquare(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_NurbsSquareCreateFlags],
) -> tuple[Transform, MakeNurbsSquare] | tuple[Transform] | tuple[MakeNurbsSquare]: ...

@overload
def nurbsSquare(
    *args: str | MakeNurbsSquare | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsSquareModeFlags],
) -> NodeState: ...

@overload
def nurbsSquare(
    *args: str | MakeNurbsSquare | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_NurbsSquareModeFlags],
) -> NodeState: ...

@overload
def nurbsSquare(
    *args: str | MakeNurbsSquare | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsSquareModeFlags],
) -> NodeState: ...

@overload
def nurbsSquare(
    *args: str | MakeNurbsSquare | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_NurbsSquareModeFlags],
) -> NodeState: ...

@overload
def nurbsSquare(
    *args: str | MakeNurbsSquare | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsSquareModeFlags],
) -> Literal["Values edited."]: ...

@overload
def nurbsSquare(
    *args: str | MakeNurbsSquare | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsSquareModeFlags],
) -> Literal["Values edited."]: ...

@overload
def nurbsSquare(
    *args: str | MakeNurbsSquare | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_NurbsSquareModeFlags],
) -> Any: ...


class _PointLightFlags(TypedDict, total=False):
    discRadius: float
    drs: float
    exclusive: bool
    exc: bool
    rgb: tuple[float, float, float]
    useRayTraceShadows: bool
    rs: bool
    shadowColor: tuple[float, float, float]
    sc: tuple[float, float, float]
    shadowDither: float
    sd: float
    shadowSamples: int
    sh: int
    softShadow: bool
    ss: bool

class _PointLightCreateFlags(_PointLightFlags, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    decayRate: int
    d: int
    intensity: float
    i: float
    name: str
    n: str
    position: tuple[float, float, float]
    pos: tuple[float, float, float]
    rotation: tuple[float, float, float]
    rot: tuple[float, float, float]

class _PointLightModeFlags(_PointLightFlags, total=False):
    edit: bool
    e: bool
    query: bool
    q: bool
    decayRate: int | bool
    d: int | bool
    intensity: float | bool
    i: float | bool
    name: str | bool
    n: str | bool
    position: tuple[float, float, float] | bool
    pos: tuple[float, float, float] | bool
    rotation: tuple[float, float, float] | bool
    rot: tuple[float, float, float] | bool

@overload
def pointLight(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_PointLightCreateFlags],
) -> PointLight: ...

@overload
def pointLight(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_PointLightModeFlags],
) -> Any: ...



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
    depth: float
    d: float
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
    width: float
    w: float

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
    depth: float
    d: float
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
    width: float
    w: float

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



class _PolyHelixModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    coils: float
    c: float
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    direction: int
    d: int
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
    useOldInitBehaviour: bool
    oib: bool
    radius: float
    r: float
    roundCap: bool
    rcp: bool
    subdivisionsAxis: int
    sa: int
    subdivisionsCaps: int
    sc: int
    subdivisionsCoil: int
    sco: int
    texture: int
    tx: int
    width: float
    w: float

class _PolyHelixCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    coils: float
    c: float
    caching: bool
    cch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: int
    cuv: int
    direction: int
    d: int
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
    useOldInitBehaviour: bool
    oib: bool
    radius: float
    r: float
    roundCap: bool
    rcp: bool
    subdivisionsAxis: int
    sa: int
    subdivisionsCaps: int
    sc: int
    subdivisionsCoil: int
    sco: int
    texture: int
    tx: int
    width: float
    w: float

@overload
def polyHelix(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyHelixCreateFlags],
) -> tuple[PolyHelix]: ...

@overload
def polyHelix(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyHelixCreateFlags],
) -> tuple[PolyHelix]: ...

@overload
def polyHelix(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyHelixCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyHelix(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyHelixCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyHelix(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyHelixCreateFlags],
) -> tuple[Transform, PolyHelix]: ...

@overload
def polyHelix(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyHelixCreateFlags],
) -> tuple[Transform, PolyHelix] | tuple[Transform] | tuple[PolyHelix]: ...

@overload
def polyHelix(
    *args: str | PolyHelix | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyHelixModeFlags],
) -> NodeState: ...

@overload
def polyHelix(
    *args: str | PolyHelix | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyHelixModeFlags],
) -> NodeState: ...

@overload
def polyHelix(
    *args: str | PolyHelix | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyHelixModeFlags],
) -> NodeState: ...

@overload
def polyHelix(
    *args: str | PolyHelix | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyHelixModeFlags],
) -> NodeState: ...

@overload
def polyHelix(
    *args: str | PolyHelix | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyHelixModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyHelix(
    *args: str | PolyHelix | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyHelixModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyHelix(
    *args: str | PolyHelix | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyHelixModeFlags],
) -> Any: ...



class _PolyPipeModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: bool
    cuv: bool
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
    thickness: float
    t: float
    texture: bool
    tx: bool

class _PolyPipeCreateFlags(TypedDict, total=False):
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
    createUVs: bool
    cuv: bool
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
    thickness: float
    t: float
    texture: bool
    tx: bool

@overload
def polyPipe(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPipeCreateFlags],
) -> tuple[PolyPipe]: ...

@overload
def polyPipe(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPipeCreateFlags],
) -> tuple[PolyPipe]: ...

@overload
def polyPipe(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPipeCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyPipe(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPipeCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyPipe(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPipeCreateFlags],
) -> tuple[Transform, PolyPipe]: ...

@overload
def polyPipe(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyPipeCreateFlags],
) -> tuple[Transform, PolyPipe] | tuple[Transform] | tuple[PolyPipe]: ...

@overload
def polyPipe(
    *args: str | PolyPipe | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPipeModeFlags],
) -> NodeState: ...

@overload
def polyPipe(
    *args: str | PolyPipe | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPipeModeFlags],
) -> NodeState: ...

@overload
def polyPipe(
    *args: str | PolyPipe | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPipeModeFlags],
) -> NodeState: ...

@overload
def polyPipe(
    *args: str | PolyPipe | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPipeModeFlags],
) -> NodeState: ...

@overload
def polyPipe(
    *args: str | PolyPipe | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPipeModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyPipe(
    *args: str | PolyPipe | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPipeModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyPipe(
    *args: str | PolyPipe | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPipeModeFlags],
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



class _PolyPlatonicSolidModeFlags(TypedDict, total=False):
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
    sideLength: float
    l: float
    name: str
    n: str
    object: bool
    o: bool
    radius: float
    r: float
    solidType: int
    st: int
    texture: int
    tx: int

class _PolyPlatonicSolidCreateFlags(TypedDict, total=False):
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
    sideLength: float
    l: float
    name: str
    n: str
    nodeState: int
    nds: int
    radius: float
    r: float
    solidType: int
    st: int
    texture: int
    tx: int

@overload
def polyPlatonicSolid(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPlatonicSolidCreateFlags],
) -> tuple[PolyPlatonicSolid]: ...

@overload
def polyPlatonicSolid(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPlatonicSolidCreateFlags],
) -> tuple[PolyPlatonicSolid]: ...

@overload
def polyPlatonicSolid(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPlatonicSolidCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyPlatonicSolid(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPlatonicSolidCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyPlatonicSolid(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPlatonicSolidCreateFlags],
) -> tuple[Transform, PolyPlatonicSolid]: ...

@overload
def polyPlatonicSolid(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyPlatonicSolidCreateFlags],
) -> tuple[Transform, PolyPlatonicSolid] | tuple[Transform] | tuple[PolyPlatonicSolid]: ...

@overload
def polyPlatonicSolid(
    *args: str | PolyPlatonicSolid | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPlatonicSolidModeFlags],
) -> NodeState: ...

@overload
def polyPlatonicSolid(
    *args: str | PolyPlatonicSolid | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPlatonicSolidModeFlags],
) -> NodeState: ...

@overload
def polyPlatonicSolid(
    *args: str | PolyPlatonicSolid | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPlatonicSolidModeFlags],
) -> NodeState: ...

@overload
def polyPlatonicSolid(
    *args: str | PolyPlatonicSolid | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPlatonicSolidModeFlags],
) -> NodeState: ...

@overload
def polyPlatonicSolid(
    *args: str | PolyPlatonicSolid | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPlatonicSolidModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyPlatonicSolid(
    *args: str | PolyPlatonicSolid | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPlatonicSolidModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyPlatonicSolid(
    *args: str | PolyPlatonicSolid | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPlatonicSolidModeFlags],
) -> Any: ...



class _PolyPrimitiveModeFlags(TypedDict, total=False):
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
    sideLength: float
    l: float
    name: str
    n: str
    object: bool
    o: bool
    polyType: int
    pt: int
    radius: float
    r: float
    texture: int
    tx: int

class _PolyPrimitiveCreateFlags(TypedDict, total=False):
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
    sideLength: float
    l: float
    name: str
    n: str
    nodeState: int
    nds: int
    polyType: int
    pt: int
    radius: float
    r: float
    texture: int
    tx: int

@overload
def polyPrimitive(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPrimitiveCreateFlags],
) -> tuple[PolyPrimitiveMisc]: ...

@overload
def polyPrimitive(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPrimitiveCreateFlags],
) -> tuple[PolyPrimitiveMisc]: ...

@overload
def polyPrimitive(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPrimitiveCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyPrimitive(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPrimitiveCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyPrimitive(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPrimitiveCreateFlags],
) -> tuple[Transform, PolyPrimitiveMisc]: ...

@overload
def polyPrimitive(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyPrimitiveCreateFlags],
) -> tuple[Transform, PolyPrimitiveMisc] | tuple[Transform] | tuple[PolyPrimitiveMisc]: ...

@overload
def polyPrimitive(
    *args: str | PolyPrimitiveMisc | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPrimitiveModeFlags],
) -> NodeState: ...

@overload
def polyPrimitive(
    *args: str | PolyPrimitiveMisc | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPrimitiveModeFlags],
) -> NodeState: ...

@overload
def polyPrimitive(
    *args: str | PolyPrimitiveMisc | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPrimitiveModeFlags],
) -> NodeState: ...

@overload
def polyPrimitive(
    *args: str | PolyPrimitiveMisc | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPrimitiveModeFlags],
) -> NodeState: ...

@overload
def polyPrimitive(
    *args: str | PolyPrimitiveMisc | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPrimitiveModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyPrimitive(
    *args: str | PolyPrimitiveMisc | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPrimitiveModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyPrimitive(
    *args: str | PolyPrimitiveMisc | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPrimitiveModeFlags],
) -> Any: ...



class _PolyPrismModeFlags(TypedDict, total=False):
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
    length: float
    l: float
    name: str
    n: str
    numberOfSides: int
    ns: int
    numderOfSides: int
    nsi: int
    object: bool
    o: bool
    subdivisionsCaps: int
    sc: int
    subdivisionsHeight: int
    sh: int
    texture: int
    tx: int
    sideLength: float
    w: float

class _PolyPrismCreateFlags(TypedDict, total=False):
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
    length: float
    l: float
    name: str
    n: str
    nodeState: int
    nds: int
    numberOfSides: int
    ns: int
    numderOfSides: int
    nsi: int
    subdivisionsCaps: int
    sc: int
    subdivisionsHeight: int
    sh: int
    texture: int
    tx: int
    sideLength: float
    w: float

@overload
def polyPrism(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPrismCreateFlags],
) -> tuple[PolyPrism]: ...

@overload
def polyPrism(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyPrismCreateFlags],
) -> tuple[PolyPrism]: ...

@overload
def polyPrism(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPrismCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyPrism(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPrismCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyPrism(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyPrismCreateFlags],
) -> tuple[Transform, PolyPrism]: ...

@overload
def polyPrism(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyPrismCreateFlags],
) -> tuple[Transform, PolyPrism] | tuple[Transform] | tuple[PolyPrism]: ...

@overload
def polyPrism(
    *args: str | PolyPrism | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPrismModeFlags],
) -> NodeState: ...

@overload
def polyPrism(
    *args: str | PolyPrism | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPrismModeFlags],
) -> NodeState: ...

@overload
def polyPrism(
    *args: str | PolyPrism | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPrismModeFlags],
) -> NodeState: ...

@overload
def polyPrism(
    *args: str | PolyPrism | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyPrismModeFlags],
) -> NodeState: ...

@overload
def polyPrism(
    *args: str | PolyPrism | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPrismModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyPrism(
    *args: str | PolyPrism | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPrismModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyPrism(
    *args: str | PolyPrism | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyPrismModeFlags],
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
    numberOfSides: int
    ns: int
    numderOfSides: int
    nsi: int
    object: bool
    o: bool
    subdivisionsCaps: int
    sc: int
    subdivisionsHeight: int
    sh: int
    texture: bool
    tx: bool
    sideLength: float
    w: float

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
    subdivisionsCaps: int
    sc: int
    subdivisionsHeight: int
    sh: int
    texture: bool
    tx: bool
    sideLength: float
    w: float

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



class _PolyTorusModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    componentTagCreate: bool
    ctc: bool
    createUVs: bool
    cuv: bool
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
    sectionRadius: float
    sr: float
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    twist: float
    tw: float
    texture: bool
    tx: bool

class _PolyTorusCreateFlags(TypedDict, total=False):
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
    createUVs: bool
    cuv: bool
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
    sectionRadius: float
    sr: float
    subdivisionsX: int
    sx: int
    subdivisionsY: int
    sy: int
    twist: float
    tw: float
    texture: bool
    tx: bool

@overload
def polyTorus(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyTorusCreateFlags],
) -> tuple[PolyTorus]: ...

@overload
def polyTorus(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_PolyTorusCreateFlags],
) -> tuple[PolyTorus]: ...

@overload
def polyTorus(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyTorusCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyTorus(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyTorusCreateFlags],
) -> tuple[Transform]: ...

@overload
def polyTorus(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_PolyTorusCreateFlags],
) -> tuple[Transform, PolyTorus]: ...

@overload
def polyTorus(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_PolyTorusCreateFlags],
) -> tuple[Transform, PolyTorus] | tuple[Transform] | tuple[PolyTorus]: ...

@overload
def polyTorus(
    *args: str | PolyTorus | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyTorusModeFlags],
) -> NodeState: ...

@overload
def polyTorus(
    *args: str | PolyTorus | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyTorusModeFlags],
) -> NodeState: ...

@overload
def polyTorus(
    *args: str | PolyTorus | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyTorusModeFlags],
) -> NodeState: ...

@overload
def polyTorus(
    *args: str | PolyTorus | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_PolyTorusModeFlags],
) -> NodeState: ...

@overload
def polyTorus(
    *args: str | PolyTorus | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyTorusModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyTorus(
    *args: str | PolyTorus | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyTorusModeFlags],
) -> Literal["Values edited."]: ...

@overload
def polyTorus(
    *args: str | PolyTorus | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_PolyTorusModeFlags],
) -> Any: ...


def removeJoint(*args: str | Node | Sequence[str | Node]) -> None: ...


class _SpaceLocatorFlags(TypedDict, total=False):
    absolute: bool
    a: bool
    relative: bool
    r: bool

class _SpaceLocatorCreateFlags(_SpaceLocatorFlags, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    name: str
    n: str
    position: tuple[float, float, float]
    p: tuple[float, float, float]

class _SpaceLocatorModeFlags(_SpaceLocatorFlags, total=False):
    edit: bool
    e: bool
    query: bool
    q: bool
    name: str | bool
    n: str | bool
    position: tuple[float, float, float] | bool
    p: tuple[float, float, float] | bool

@overload
def spaceLocator(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_SpaceLocatorCreateFlags],
) -> Transform: ...

@overload
def spaceLocator(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_SpaceLocatorModeFlags],
) -> Any: ...



class _SphereModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    degree: int
    d: int
    endSweep: float
    esw: float
    frozen: bool
    fzn: bool
    heightRatio: float
    hr: float
    name: str
    n: str
    spans: int
    nsp: int
    object: bool
    o: bool
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    radius: float
    r: float
    sections: int
    s: int
    startSweep: float
    ssw: float
    tolerance: float
    tol: float
    useTolerance: bool
    ut: bool

class _SphereCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    degree: int
    d: int
    endSweep: float
    esw: float
    frozen: bool
    fzn: bool
    heightRatio: float
    hr: float
    name: str
    n: str
    nodeState: int
    nds: int
    spans: int
    nsp: int
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    radius: float
    r: float
    sections: int
    s: int
    startSweep: float
    ssw: float
    tolerance: float
    tol: float
    useTolerance: bool
    ut: bool

@overload
def sphere(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_SphereCreateFlags],
) -> tuple[MakeNurbSphere]: ...

@overload
def sphere(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_SphereCreateFlags],
) -> tuple[MakeNurbSphere]: ...

@overload
def sphere(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_SphereCreateFlags],
) -> tuple[Transform]: ...

@overload
def sphere(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_SphereCreateFlags],
) -> tuple[Transform]: ...

@overload
def sphere(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_SphereCreateFlags],
) -> tuple[Transform, MakeNurbSphere]: ...

@overload
def sphere(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_SphereCreateFlags],
) -> tuple[Transform, MakeNurbSphere] | tuple[Transform] | tuple[MakeNurbSphere]: ...

@overload
def sphere(
    *args: str | MakeNurbSphere | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_SphereModeFlags],
) -> NodeState: ...

@overload
def sphere(
    *args: str | MakeNurbSphere | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_SphereModeFlags],
) -> NodeState: ...

@overload
def sphere(
    *args: str | MakeNurbSphere | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_SphereModeFlags],
) -> NodeState: ...

@overload
def sphere(
    *args: str | MakeNurbSphere | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_SphereModeFlags],
) -> NodeState: ...

@overload
def sphere(
    *args: str | MakeNurbSphere | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_SphereModeFlags],
) -> Literal["Values edited."]: ...

@overload
def sphere(
    *args: str | MakeNurbSphere | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_SphereModeFlags],
) -> Literal["Values edited."]: ...

@overload
def sphere(
    *args: str | MakeNurbSphere | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_SphereModeFlags],
) -> Any: ...


class _SpotLightFlags(TypedDict, total=False):
    bottomBarnDoorAngle: float
    bbd: float
    barnDoors: bool
    bd: bool
    dropOff: float
    do: float
    discRadius: float
    drs: float
    exclusive: bool
    exc: bool
    leftBarnDoorAngle: float
    lbd: float
    rightBarnDoorAngle: float
    rbd: float
    rgb: tuple[float, float, float]
    useRayTraceShadows: bool
    rs: bool
    shadowColor: tuple[float, float, float]
    sc: tuple[float, float, float]
    shadowDither: float
    sd: float
    shadowSamples: int
    sh: int
    softShadow: bool
    ss: bool
    topBarnDoorAngle: float
    tbd: float

class _SpotLightCreateFlags(_SpotLightFlags, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    coneAngle: float
    ca: float
    decayRate: int
    d: int
    intensity: float
    i: float
    name: str
    n: str
    penumbra: float
    p: float
    position: tuple[float, float, float]
    pos: tuple[float, float, float]
    rotation: tuple[float, float, float]
    rot: tuple[float, float, float]

class _SpotLightModeFlags(_SpotLightFlags, total=False):
    edit: bool
    e: bool
    query: bool
    q: bool
    coneAngle: float | bool
    ca: float | bool
    decayRate: int | bool
    d: int | bool
    intensity: float | bool
    i: float | bool
    name: str | bool
    n: str | bool
    penumbra: float | bool
    p: float | bool
    position: tuple[float, float, float] | bool
    pos: tuple[float, float, float] | bool
    rotation: tuple[float, float, float] | bool
    rot: tuple[float, float, float] | bool

@overload
def spotLight(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_SpotLightCreateFlags],
) -> SpotLight: ...

@overload
def spotLight(
    *args: str | Node | Sequence[str | Node],
    **kwargs: Unpack[_SpotLightModeFlags],
) -> Any: ...



class _TorusModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    constructionHistory: bool
    ch: bool
    degree: int
    d: int
    endSweep: float
    esw: float
    frozen: bool
    fzn: bool
    heightRatio: float
    hr: float
    minorSweep: float
    msw: float
    name: str
    n: str
    spans: int
    nsp: int
    object: bool
    o: bool
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    radius: float
    r: float
    sections: int
    s: int
    startSweep: float
    ssw: float
    tolerance: float
    tol: float
    useTolerance: bool
    ut: bool

class _TorusCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    degree: int
    d: int
    endSweep: float
    esw: float
    frozen: bool
    fzn: bool
    heightRatio: float
    hr: float
    minorSweep: float
    msw: float
    name: str
    n: str
    nodeState: int
    nds: int
    spans: int
    nsp: int
    pivot: tuple[float, float, float]
    p: tuple[float, float, float]
    polygon: int
    po: int
    radius: float
    r: float
    sections: int
    s: int
    startSweep: float
    ssw: float
    tolerance: float
    tol: float
    useTolerance: bool
    ut: bool

@overload
def torus(
    *args: str,
    object: Literal[False],
    o: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_TorusCreateFlags],
) -> tuple[MakeNurbTorus]: ...

@overload
def torus(
    *args: str,
    o: Literal[False],
    object: bool = ...,
    constructionHistory: bool = ...,
    ch: bool = ...,
    **kwargs: Unpack[_TorusCreateFlags],
) -> tuple[MakeNurbTorus]: ...

@overload
def torus(
    *args: str,
    constructionHistory: Literal[False],
    ch: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_TorusCreateFlags],
) -> tuple[Transform]: ...

@overload
def torus(
    *args: str,
    ch: Literal[False],
    constructionHistory: bool = ...,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_TorusCreateFlags],
) -> tuple[Transform]: ...

@overload
def torus(
    *args: str,
    constructionHistory: Literal[True] = True,
    ch: Literal[True] = True,
    object: Literal[True] = True,
    o: Literal[True] = True,
    **kwargs: Unpack[_TorusCreateFlags],
) -> tuple[Transform, MakeNurbTorus]: ...

@overload
def torus(
    *args: str,
    constructionHistory: bool = ...,
    ch: bool = ...,
    object: bool = ...,
    o: bool = ...,
    **kwargs: Unpack[_TorusCreateFlags],
) -> tuple[Transform, MakeNurbTorus] | tuple[Transform] | tuple[MakeNurbTorus]: ...

@overload
def torus(
    *args: str | MakeNurbTorus | Transform,
    query: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_TorusModeFlags],
) -> NodeState: ...

@overload
def torus(
    *args: str | MakeNurbTorus | Transform,
    query: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    q: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_TorusModeFlags],
) -> NodeState: ...

@overload
def torus(
    *args: str | MakeNurbTorus | Transform,
    q: Literal[True],
    nodeState: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nds: int = ...,
    **kwargs: Unpack[_TorusModeFlags],
) -> NodeState: ...

@overload
def torus(
    *args: str | MakeNurbTorus | Transform,
    q: Literal[True],
    nds: Literal[True],
    edit: bool = False,
    e: bool = False,
    query: bool = ...,
    nodeState: int = ...,
    **kwargs: Unpack[_TorusModeFlags],
) -> NodeState: ...

@overload
def torus(
    *args: str | MakeNurbTorus | Transform,
    edit: Literal[True],
    e: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_TorusModeFlags],
) -> Literal["Values edited."]: ...

@overload
def torus(
    *args: str | MakeNurbTorus | Transform,
    e: Literal[True],
    edit: bool = False,
    query: Literal[False] = False,
    q: Literal[False] = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_TorusModeFlags],
) -> Literal["Values edited."]: ...

@overload
def torus(
    *args: str | MakeNurbTorus | Transform,
    edit: bool = False,
    e: bool = False,
    query: bool = False,
    q: bool = False,
    nodeState: int = ...,
    nds: int = ...,
    **kwargs: Unpack[_TorusModeFlags],
) -> Any: ...


__all__ = ["ambientLight", "circle", "cone", "connectJoint", "createNode", "cylinder", "directionalLight", "ikHandle", "ikHandleDisplayScale", "ikSolver", "ikSystemInfo", "insertJoint", "joint", "jointDisplayScale", "ls", "mirrorJoint", "nurbsCube", "nurbsPlane", "nurbsSquare", "pointLight", "polyCone", "polyCube", "polyCylinder", "polyHelix", "polyPipe", "polyPlane", "polyPlatonicSolid", "polyPrimitive", "polyPrism", "polyPyramid", "polySphere", "polyTorus", "removeJoint", "spaceLocator", "sphere", "spotLight", "torus"]
