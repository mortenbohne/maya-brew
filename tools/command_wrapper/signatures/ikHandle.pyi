from collections.abc import Sequence
from typing import Any, Literal, Never, TypedDict, Unpack, overload

from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_types import IkEffector, IkHandle, Transform

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
) -> (
    tuple[IkHandle]
    | tuple[IkHandle, IkEffector]
    | tuple[IkHandle, IkEffector, Transform]
): ...
@overload
def ikHandle(
    *args: str | Node | Sequence[str | Node],
    exists: str | bool = ...,
    ex: str | bool = ...,
    **kwargs: Unpack[_IkHandleModeFlags],
) -> Any: ...
