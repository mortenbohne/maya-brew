from typing import Any, Literal, TypedDict, Unpack, overload

from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import PolyPrimitiveMisc, Transform

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
    name: str
    n: str
    object: bool
    o: bool
    polyType: int
    pt: int
    radius: float
    r: float
    sideLength: float
    l: float
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
    name: str
    n: str
    nodeState: int
    nds: int
    polyType: int
    pt: int
    radius: float
    r: float
    sideLength: float
    l: float
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
) -> (
    tuple[Transform, PolyPrimitiveMisc] | tuple[Transform] | tuple[PolyPrimitiveMisc]
): ...
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
