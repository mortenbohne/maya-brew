from typing import overload, Union
from .. import OpenMaya2
from ..nodes.node_types import DagNode
from ..nodes import cast


api_type_str_getter_map = {"kDoubleLinearAttribute": "asDouble"}


class Attribute:
    @overload
    def __init__(self, plug: OpenMaya2.MPlug): ...
    @overload
    def __init__(self, plug_path: str): ...
    def __init__(self, plug_or_path: Union[OpenMaya2.MPlug, str]):
        """
        Initialize the Attribute with a plug or a string path.
        :param plug_or_path: The plug of the attribute or a string path.
        """
        if isinstance(plug_or_path, OpenMaya2.MPlug):
            self.plug = plug_or_path
        elif isinstance(plug_or_path, str):
            self.plug = self._plug_from_path(plug_or_path)
        else:
            raise TypeError("Attribute expects an MPlug or a string path.")

    @staticmethod
    def _plug_from_path(path: str) -> OpenMaya2.MPlug:
        """
        Resolve a string path to an MPlug.
        :param path: The full path to the attribute, e.g. '|grp|node|nodeShape.visibility'
        :return: The MPlug for the attribute.
        """
        # Split path into node path and attribute name
        if "." not in path:
            raise ValueError(
                "Attribute path must include a '.' separating node and attribute."
            )
        node_path, attr_name = path.rsplit(".", 1)
        node_dag_path = cast.get_dag_path_from_string(node_path)
        node = DagNode(node_dag_path.fullPathName())
        plug = Attribute.get_plug_from_node(node, attr_name)
        return plug

    def __str__(self):
        return self.name()

    def get(self):
        return self._get_plug_value(self.plug)

    @classmethod
    def _get_value(cls, node: DagNode, attr_name: str):
        """
        Get the value of the attribute from the node.
        :param node: The node to get the attribute from.
        :param attr_name: The name of the attribute.
        :return: The value of the attribute.
        """
        plug = cls.get_plug_from_node(node, attr_name)
        return cls._get_plug_value(plug)

    @classmethod
    def get_plug_from_node(cls, node: DagNode, attr_name: str) -> OpenMaya2.MPlug:
        """
        Get the plug of the attribute from the node.
        :param node: The node to get the plug from.
        :param attr_name: The name of the attribute.
        :return: The plug of the attribute.
        """
        fn_dep = node.get_mfndependency_node()
        return fn_dep.findPlug(attr_name, False)

    def get_node_from_plug(self) -> DagNode:
        """
        Get the node from the plug.
        :return: The node that the plug belongs to.
        """
        fn_dep = self.plug.node()
        return DagNode(fn_dep.fullPathName())

    @classmethod
    def _get_plug_value(cls, plug: OpenMaya2.MPlug):
        """
        Get the value of the plug.
        :param plug: The plug to get the value from.
        :return: The value of the plug.
        """
        attribute = plug.attribute()
        type_str = attribute.apiTypeStr
        getter_name = api_type_str_getter_map.get(type_str)
        if getter_name:
            try:
                return getattr(plug, getter_name)()
            except AttributeError as e:
                raise ValueError(
                    f"Attribute type '{type_str}' does not support '{getter_name}'"
                ) from e
        else:
            if type_str == "kCompound":
                return tuple(
                    cls._get_plug_value(plug.child(i))
                    for i in range(plug.numChildren())
                )
            if type_str == "kMessage":
                raise AttributeError("Message attributes do not hold data.")
            raise ValueError(f"Unsupported attribute type: {attribute.apiTypeStr}")

    def name(self):
        raise NotImplementedError
