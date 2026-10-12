from typing import TYPE_CHECKING, Any, Callable, ClassVar, Self, TypeVar, overload

from ... import OpenMaya2, cmds
from ...exceptions import AbstractNodeCreationError, NodeException
from ...log import get_logger
from .. import casting

if TYPE_CHECKING:
    from ...attributes.node_attribute import Attribute, AttributeAccessor

A = TypeVar("A", bound="Attribute")
logger = get_logger(__name__)


class Node:
    _maya_type: ClassVar[str | None] = None
    _abstract: ClassVar[bool] = True
    _cmds_creator: ClassVar[Callable[..., str] | None] = None
    _cmds_creator_args: ClassVar[dict[str, Any]] = {}

    def __init__(self, node_path: str) -> None:
        self.node_path = node_path

    def __str__(self) -> str:
        return self.node_path

    def __repr__(self) -> str:
        return f'{type(self).__name__}("{str(self)}")'

    def rename(self, new_name: str, *args: Any, **kwargs: Any) -> str:
        try:
            actual_new_name = cmds.rename(str(self), new_name, *args, **kwargs)
        except RuntimeError as e:
            raise NodeException(f"Cannot rename '{self}': {e}") from e
        self.node_path = actual_new_name
        return actual_new_name

    def _cmd_caller(self, func_name: str, *args: Any, **kwargs: Any) -> Any:
        return cmds.attr(func_name, self.node_path, *args, **kwargs)

    @classmethod
    def create(cls, name: str, **kwargs: Any) -> Self:
        if cls._abstract or cls._maya_type is None:
            raise AbstractNodeCreationError(
                f"Cannot create a node from abstract class {cls.__name__}"
            )
        kwargs.update(cls._cmds_creator_args)
        kwargs["name"] = name
        try:
            if cls._cmds_creator is not None:
                result = cls._cmds_creator(**kwargs)
            else:
                result = cls._create_native(**kwargs)
        except RuntimeError as e:
            raise NodeException(f"Cannot create {cls._maya_type}: {e}") from e
        if result != name:
            logger.debug(f"Name was not unique. New name: {result}.")
        return cls(result)

    @classmethod
    def _create_native(cls, **kwargs: Any) -> str:
        if cls._maya_type is None:
            raise NodeException("Generic Node has no native Maya type")
        return cmds.createNode(cls._maya_type, **kwargs)

    @overload
    def list_attributes(self, attr_type: type[A], **kwargs: Any) -> list[A]: ...

    @overload
    def list_attributes(
        self, attr_type: None = None, **kwargs: Any
    ) -> list["Attribute"]: ...

    def list_attributes(
        self, attr_type: "type[A] | None" = None, **kwargs: Any
    ) -> "list[A] | list[Attribute]":
        from ...attributes.node_attribute import Attribute

        try:
            names = cmds.listAttr(str(self), **kwargs)
        except RuntimeError as e:
            raise NodeException(f"Cannot list attributes on '{self}': {e}") from e
        attrs = [Attribute(f"{self}.{name}") for name in names or []]
        if attr_type is not None:
            return [attr for attr in attrs if isinstance(attr, attr_type)]
        return attrs

    @property
    def at(self) -> "AttributeAccessor":
        from ...attributes.node_attribute import AttributeAccessor

        return AttributeAccessor(self)

    def get_depend_node(self) -> OpenMaya2.MObject:
        selection = OpenMaya2.MSelectionList()
        try:
            selection.add(str(self))
            return selection.getDependNode(0)
        except RuntimeError as e:
            raise NodeException(f"Cannot resolve '{self}': {e}") from e

    def get_mfndependency_node(self) -> OpenMaya2.MFnDependencyNode:
        try:
            return OpenMaya2.MFnDependencyNode(self.get_depend_node())
        except RuntimeError as e:
            raise NodeException(f"Cannot access dependency node '{self}': {e}") from e


class DagNode(Node):
    def __init__(self, node_path: str) -> None:
        super().__init__(node_path)
        self.dag_path = casting.get_dag_path_from_string(node_path)

    def __str__(self) -> str:
        return self.get_full_path()

    def get_depend_node(self) -> OpenMaya2.MObject:
        try:
            return self.dag_path.node()
        except RuntimeError as e:
            raise NodeException(f"Cannot access DAG node: {e}") from e

    def get_full_path(self) -> str:
        try:
            full_path = self.dag_path.fullPathName()
        except RuntimeError as e:
            raise NodeException(f"Cannot access DAG path: {e}") from e
        if not full_path:
            logger.warning(f"Node has been deleted. Original path: {self.node_path}")
        return full_path


class Transform(Node):
    @classmethod
    def _create_native(cls, **kwargs: Any) -> str:
        if cls._maya_type == "transform":
            kwargs["empty"] = True
            return cmds.group(**kwargs)
        return super()._create_native(**kwargs)


def get_bases(class_name: str, parent: type[Node]) -> tuple[type[Node], ...]:
    extension = globals().get(class_name)
    if extension is None:
        return (parent,)
    if not isinstance(extension, type) or not issubclass(extension, Node):
        raise NodeException(f"{class_name} must be a Node extension class")
    if issubclass(parent, extension):
        return (parent,)
    return (extension, parent)
