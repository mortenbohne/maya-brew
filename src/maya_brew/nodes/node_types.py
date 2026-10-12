from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated.maya_2027.classes import *  # noqa: F403, F401

from ._foundation import node_extensions as _node_extensions
from ._foundation.node_registry import registry as _registry


def __getattr__(name: str) -> type[_node_extensions.Node]:
    from ._foundation.native_node_hierarchy import (
        discover_node_types,
        python_class_name,
    )

    if name.startswith("_"):
        raise AttributeError(name)
    for maya_type in discover_node_types(include_plugins=True):
        if python_class_name(maya_type) == name:
            wrapper = _registry.get_or_create_class(maya_type)
            globals()[name] = wrapper
            return wrapper
    raise AttributeError(f"No native node class named {name!r}")
