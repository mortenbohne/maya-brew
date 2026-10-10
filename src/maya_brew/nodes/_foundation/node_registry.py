import importlib

from ... import cmds
from ...exceptions import MayaBrewException, NodeTypeInheritanceError
from ...log import get_logger
from .. import _generated
from . import node_extensions
from .native_node_hierarchy import (
    python_class_name,
    query_node_type,
)
from .node_extensions import Node

logger = get_logger(__name__)


class NodeRegistry:
    def __init__(self, use_generated: bool = True) -> None:
        self._use_generated = use_generated
        self._loaded = False
        self._classes: dict[str, type[Node]] = {}

    def _load_snapshot(self) -> None:
        if self._loaded:
            return
        if not self._use_generated:
            self._loaded = True
            return
        try:
            major_version = cmds.about(majorVersion=True)
        except RuntimeError as e:
            raise MayaBrewException(f"Cannot determine Maya version: {e}") from e
        package_name = f"{_generated.__name__}.maya_{major_version}"
        module_name = f"{package_name}.constants"
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError as e:
            if e.name not in {package_name, module_name}:
                raise
            logger.warning(
                f"No generated node snapshot for Maya {major_version}; "
                "using runtime-generated classes."
            )
            self._loaded = True
            return
        self._classes.update(module.TYPE_CLASSES)
        self._loaded = True

    def get_or_create_class(self, maya_type: str) -> type[Node]:
        self._load_snapshot()
        if maya_type in self._classes:
            return self._classes[maya_type]
        return self._create_class(maya_type)

    def _create_class(self, maya_type: str) -> type[Node]:
        chain = query_node_type(maya_type)
        try:
            concrete = set(cmds.allNodeTypes() or [])
        except RuntimeError as e:
            raise NodeTypeInheritanceError(
                f"Cannot query concrete node types: {e}"
            ) from e
        parent: type[Node] = Node
        for name in chain:
            if name in self._classes:
                parent = self._classes[name]
                continue
            class_name = python_class_name(name)
            wrapper = type(
                class_name,
                node_extensions.get_bases(class_name, parent),
                {},
            )
            wrapper._maya_type = name
            wrapper._abstract = name not in concrete
            wrapper.__module__ = __name__
            self._classes[name] = wrapper
            parent = wrapper
        return parent


registry = NodeRegistry()
