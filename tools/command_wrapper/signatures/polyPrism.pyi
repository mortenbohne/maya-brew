from typing import Any, Literal, TypedDict, Unpack, overload

from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import PolyPrism, Transform

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
    texture: int
    tx: int

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
    sideLength: float
    w: float
    subdivisionsCaps: int
    sc: int
    subdivisionsHeight: int
    sh: int
    texture: int
    tx: int

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
