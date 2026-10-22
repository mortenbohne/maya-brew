from typing import Any, Literal, TypedDict, Unpack, overload

from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import PolyPlatonicSolid, Transform

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
    name: str
    n: str
    object: bool
    o: bool
    radius: float
    r: float
    sideLength: float
    l: float
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
    name: str
    n: str
    nodeState: int
    nds: int
    radius: float
    r: float
    sideLength: float
    l: float
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
) -> (
    tuple[Transform, PolyPlatonicSolid] | tuple[Transform] | tuple[PolyPlatonicSolid]
): ...
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
