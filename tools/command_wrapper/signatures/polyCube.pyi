from typing import Any, Literal, TypedDict, Unpack, overload

from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import PolyCube, Transform

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
