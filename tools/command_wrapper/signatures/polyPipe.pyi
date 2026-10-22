from typing import Any, Literal, TypedDict, Unpack, overload

from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import PolyPipe, Transform

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
    texture: bool
    tx: bool
    thickness: float
    t: float

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
    texture: bool
    tx: bool
    thickness: float
    t: float

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
