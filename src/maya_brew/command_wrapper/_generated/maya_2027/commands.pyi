# AUTO-GENERATED; DO NOT EDIT.
# @generated
from typing import Any, Literal, TypeVar, overload

from maya_brew.nodes._foundation.node_extensions import Node
from .concrete_nodes import ConcreteNode

T = TypeVar("T", bound=ConcreteNode)


@overload
def createNode(node_type: type[T], *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: Literal[False] = False, s: Literal[False] = False, skipSelect: bool = ..., ss: bool = ...) -> T: ...


@overload
def createNode(node_type: type[T], *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: bool = False, s: bool = False, skipSelect: bool = ..., ss: bool = ...) -> T | None: ...


@overload
def createNode(node_type: str, *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: bool = False, s: bool = False, skipSelect: bool = ..., ss: bool = ...) -> Node | None: ...


from typing import Any, Literal, TypedDict, Unpack, overload

from maya_brew.nodes.node_types import PolyPlane, Transform
from maya_brew.nodes.node_state import NodeState

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


__all__ = ["createNode", "polyPlane"]
