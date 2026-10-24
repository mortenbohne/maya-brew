from collections.abc import Sequence
from typing import Any, Literal, TypedDict, Unpack, overload

from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_types import IkSolver

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
