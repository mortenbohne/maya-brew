# AUTO-GENERATED; DO NOT EDIT.
# @generated
from typing import Literal, TypeVar, overload

from maya_brew.nodes._foundation.node_extensions import Node
from .concrete_nodes import ConcreteNode

T = TypeVar("T", bound=ConcreteNode)


@overload
def createNode(node_type: type[T], *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: Literal[False] = False, s: Literal[False] = False, skipSelect: bool = ..., ss: bool = ...) -> T: ...


@overload
def createNode(node_type: type[T], *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: bool = False, s: bool = False, skipSelect: bool = ..., ss: bool = ...) -> T | None: ...


@overload
def createNode(node_type: str, *, name: str = ..., n: str = ..., parent: str | Node = ..., p: str | Node = ..., shared: bool = False, s: bool = False, skipSelect: bool = ..., ss: bool = ...) -> Node | None: ...


__all__ = ["createNode"]
