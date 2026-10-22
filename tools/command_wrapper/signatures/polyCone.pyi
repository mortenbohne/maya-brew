from typing import Any, Literal, TypedDict, Unpack, overload

from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import PolyCone, Transform

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
