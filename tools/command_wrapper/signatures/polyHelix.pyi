from typing import Any, Literal, TypedDict, Unpack, overload

from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import PolyHelix, Transform

class _PolyHelixModeFlags(TypedDict, total=False):
    axis: tuple[float, float, float] | bool
    ax: tuple[float, float, float] | bool
    caching: bool
    cch: bool
    coils: float
    c: float
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
    useOldInitBehaviour: bool
    oib: bool
    width: float
    w: float

class _PolyHelixCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    axis: tuple[float, float, float]
    ax: tuple[float, float, float]
    caching: bool
    cch: bool
    coils: float
    c: float
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
    useOldInitBehaviour: bool
    oib: bool
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
