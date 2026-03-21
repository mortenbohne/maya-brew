import typing
from typing import Optional, Any
from .. import OpenMaya2, cmds
from ..exceptions import MayaBrewAttributeError
from ..nodes.node_types import DagNode, Node

PlugInput = typing.Union[OpenMaya2.MPlug, str]
A = typing.TypeVar("A", bound="Attribute")


class Attribute:
    _getter_type: str
    _creator_type: str
    _creator_type_arg = "attributeType"
    _setter_type_needed = False
    _setter_unpack = False

    def __new__(cls: type[A], plug_or_path: PlugInput) -> A:
        if cls is not Attribute:
            return typing.cast(A, super().__new__(cls))

        if isinstance(plug_or_path, OpenMaya2.MPlug):
            plug = plug_or_path
        elif isinstance(plug_or_path, str):
            plug = cls._plug_from_path(plug_or_path)
        else:
            raise ValueError("plug_or_path must be an MPlug or attribute path string.")

        try:
            mobj_attr = plug.attribute()
        except (RuntimeError, ValueError) as e:
            raise RuntimeError(
                f"Failed to obtain MObject attribute for plug {plug}"
            ) from e

        api_type = getattr(mobj_attr, "apiTypeStr", None)
        if not api_type:
            raise RuntimeError(
                f"Attribute object for plug {plug} has no apiTypeStr; cannot dispatch."
            )

        try:
            subclass: type[Attribute] = _API_TYPE_SUBCLASS_MAP[api_type]
        except KeyError:
            raise NotImplementedError(
                f"Unsupported attribute apiTypeStr '{api_type}'. Could cast attribute for '{plug}'. "
                f"Known types: {sorted(_API_TYPE_SUBCLASS_MAP)}"
            )

        instance = super().__new__(subclass)
        setattr(instance, "_pre_init_plug", plug)
        return typing.cast(A, instance)

    @typing.overload
    def __init__(self, plug_or_path: str): ...

    @typing.overload
    def __init__(self, plug_or_path: OpenMaya2.MPlug): ...

    def __init__(self, plug_or_path: PlugInput):
        # _pre_init_plug is injected by Attribute.__new__ ONLY when the user called
        # Attribute(...) (base class factory dispatch). Direct subclass construction
        # (e.g. FloatAttribute(...)) bypasses that path, so pre will be None and we
        # must resolve plug_or_path here.
        pre = getattr(self, "_pre_init_plug", None)
        if pre is not None:
            self.plug = pre
            delattr(self, "_pre_init_plug")
            return

        if isinstance(plug_or_path, OpenMaya2.MPlug):
            self.plug = plug_or_path
        elif isinstance(plug_or_path, str):
            self.plug = self._plug_from_path(plug_or_path)
        else:
            raise ValueError("plug_or_path must be an MPlug or attribute path string.")

    @staticmethod
    def _plug_from_path(path: str) -> OpenMaya2.MPlug:
        """
        Resolve a string path to an MPlug using MSelectionList and MFnDependencyNode.
        Works for both DAG and dependency nodes without casting.
        :param path: The full path to the attribute, e.g. '|grp|node|nodeShape.visibility'
        :return: The MPlug for the attribute.
        """
        if "." not in path:
            raise ValueError(
                "Attribute path must include a '.' separating node and attribute."
            )
        node_path, attr_name = path.rsplit(".", 1)
        selection_list = OpenMaya2.MSelectionList()
        selection_list.add(node_path)
        mobj = selection_list.getDependNode(0)
        fn_dep = OpenMaya2.MFnDependencyNode(mobj)
        return fn_dep.findPlug(attr_name, False)

    def __str__(self):
        return self.name()

    def get(self):
        return self._get_plug_value(self.plug)

    def set(self, value):
        attr_name = self.plug.name()
        if self._setter_type_needed:
            if self._setter_type_needed:
                cmds.setAttr(attr_name, *value, type=self._creator_type)
            else:
                cmds.setAttr(attr_name, value, type=self._creator_type)
        else:
            cmds.setAttr(attr_name, value)

    def node(self):
        return self._get_node_from_plug(self.plug)

    def name(self):
        return self.plug.name()

    def connect(self, dest: "Attribute", force: bool = False, next_available=False):
        """
        Connect this attribute to another attribute.
        :param dest: The destination attribute to connect to.
        :param force: Whether to force the connection if the destination is already connected.
        :param next_available: Whether to connect to the next available index if the destination is an array attribute.
        """
        cmds.connectAttr(
            self.plug.name(),
            dest.plug.name(),
            force=force,
            nextAvailable=next_available,
        )

    def disconnect(self, dest: "Attribute", next_available=False):
        """
        Disconnect this attribute from another attribute.
        :param dest: The destination attribute to disconnect from.
        :param next_available: Whether to disconnect from the next available index if the destination is an
        array attribute.
        """
        cmds.disconnectAttr(
            self.plug.name(), dest.plug.name(), nextAvailable=next_available
        )

    @classmethod
    def _get_value(cls, node: Node, attr_name: str):
        plug = cls._get_plug_from_node(node, attr_name)
        return cls._get_plug_value(plug)

    @staticmethod
    def _get_plug_from_node(node: Node, attr_name: str) -> OpenMaya2.MPlug:
        """
        Get the MPlug for the given attribute name from a Node or DagNode.
        """
        if hasattr(node, "get_mfndependency_node"):
            fn_dep = node.get_mfndependency_node()
        else:
            # For non-DAG nodes, resolve node.node_path to MObject
            selection_list = OpenMaya2.MSelectionList()
            selection_list.add(node.node_path)
            mobj = selection_list.getDependNode(0)
            fn_dep = OpenMaya2.MFnDependencyNode(mobj)
        return fn_dep.findPlug(attr_name, False)

    @staticmethod
    def _get_node_from_plug(plug: OpenMaya2.MPlug) -> Node:
        mobj = plug.node()
        if mobj.hasFn(OpenMaya2.MFn.kDagNode):
            return DagNode(OpenMaya2.MFnDagNode(mobj).fullPathName())
        else:
            name = OpenMaya2.MFnDependencyNode(mobj).name()
            return Node(name)

    @classmethod
    def _get_plug_value(cls, plug: OpenMaya2.MPlug):
        return getattr(plug, cls._getter_type)()

    def delete(self):
        """
        Delete a custom attribute from the specified node.
        """
        name = self.plug.name()
        try:
            cmds.deleteAttr(name)
        except Exception as e:
            raise MayaBrewAttributeError(f"Failed to delete attribute '{name}': {e}")

    @classmethod
    def create(cls, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def _create(
        cls,
        node_name: str,
        attr_name: str,
        cached_internally: Optional[bool] = None,
        category: Optional[str] = None,
        default_value: Optional[Any] = None,
        disconnect_behaviour: Optional[int] = None,
        enum_name: Optional[str] = None,
        index_matters: Optional[bool] = None,
        keyable: bool = True,
        max_value: int | float | None = None,
        min_value: int | float | None = None,
        multi: Optional[bool] = None,
        nice_name: Optional[str] = None,
        number_of_children: Optional[int] = None,
        parent: Optional[str] = None,
        proxy: Optional[str] = None,
        readable: Optional[bool] = None,
        short_name: Optional[str] = None,
        soft_max_value: int | float | None = None,
        soft_min_value: int | float | None = None,
        storable: Optional[bool] = None,
        used_as_color: Optional[bool] = None,
        used_as_filename: Optional[bool] = None,
        used_as_proxy: Optional[bool] = None,
        writeable: Optional[bool] = None,
    ) -> A:
        """
        Create an attribute on the specified node.
        :param node_name: Name of the Maya node.
        :param attr_name: Name of the custom attribute to create.
        """
        kwargs = dict()
        kwargs[cls._creator_type_arg] = cls._creator_type
        if cached_internally is not None:
            kwargs["cachedInternally"] = cached_internally
        if category is not None:
            kwargs["category"] = category
        if default_value is not None:
            kwargs["defaultValue"] = default_value
        if disconnect_behaviour is not None:
            kwargs["disconnectBehaviour"] = disconnect_behaviour
        if enum_name is not None:
            kwargs["enumName"] = enum_name
        if index_matters is not None:
            kwargs["indexMatters"] = index_matters
        if keyable is not None:
            kwargs["keyable"] = keyable
        if max_value is not None:
            kwargs["maxValue"] = max_value
        if min_value is not None:
            kwargs["minValue"] = min_value
        if multi is not None:
            kwargs["multi"] = multi
        if nice_name is not None:
            kwargs["niceName"] = nice_name
        if number_of_children is not None:
            kwargs["numberOfChildren"] = number_of_children
        if parent is not None:
            kwargs["parent"] = parent
        if proxy is not None:
            kwargs["proxy"] = proxy
        if readable is not None:
            kwargs["readable"] = readable
        if short_name is not None:
            kwargs["shortName"] = short_name
        if soft_max_value is not None:
            kwargs["softMaxValue"] = soft_max_value
        if soft_min_value is not None:
            kwargs["softMinValue"] = soft_min_value
        if storable is not None:
            kwargs["storable"] = storable
        if used_as_color is not None:
            kwargs["usedAsColor"] = used_as_color
        if used_as_filename is not None:
            kwargs["usedAsFilename"] = used_as_filename
        if used_as_proxy is not None:
            kwargs["usedAsProxy"] = used_as_proxy
        if writeable is not None:
            kwargs["writeable"] = writeable
        full_attr = f"{node_name}.{attr_name}"
        if cmds.objExists(full_attr):
            raise MayaBrewAttributeError(f"Attribute '{full_attr}' already exists.")
        attr_type = cls._creator_type
        try:
            cmds.addAttr(node_name, longName=attr_name, **kwargs)
        except Exception as e:
            raise MayaBrewAttributeError(
                f"Failed to create attribute '{full_attr}': {e}"
            )
        return typing.cast(A, cls(full_attr))


class _Attribute(Attribute):
    @classmethod
    def create(
        cls,
        node_name: str,
        attr_name: str,
        cached_internally: Optional[bool] = None,
        category: Optional[str] = None,
        disconnect_behaviour: Optional[int] = None,
        keyable: bool = True,
        nice_name: Optional[str] = None,
        parent: Optional[str] = None,
        proxy: Optional[str] = None,
        readable: Optional[bool] = None,
        short_name: Optional[str] = None,
        storable: Optional[bool] = None,
        used_as_proxy: Optional[bool] = None,
        writeable: Optional[bool] = None,
    ):
        return super()._create(
            node_name=node_name,
            attr_name=attr_name,
            cached_internally=cached_internally,
            category=category,
            disconnect_behaviour=disconnect_behaviour,
            keyable=keyable,
            nice_name=nice_name,
            parent=parent,
            proxy=proxy,
            readable=readable,
            short_name=short_name,
            storable=storable,
            used_as_proxy=used_as_proxy,
            writeable=writeable,
        )


class _NonNumericAttribute(_Attribute):
    _setter_type_needed = True
    _setter_unpack = True


class _MultiAttribute(_NonNumericAttribute):
    _num_children: int

    @classmethod
    def _get_plug_value(cls, plug: OpenMaya2.MPlug):
        mobj = plug.asMObject()
        numeric_data = OpenMaya2.MFnNumericData(mobj)
        return tuple(numeric_data.getData())


class _NumericAttribute(Attribute):
    @classmethod
    def create(
        cls,
        node_name: str,
        attr_name: str,
        cached_internally: Optional[bool] = None,
        category: Optional[str] = None,
        default_value: Optional[Any] = None,
        disconnect_behaviour: Optional[int] = None,
        keyable: bool = True,
        max_value: int | float | None = None,
        min_value: int | float | None = None,
        nice_name: Optional[str] = None,
        parent: Optional[str] = None,
        proxy: Optional[str] = None,
        readable: Optional[bool] = None,
        short_name: Optional[str] = None,
        soft_max_value: int | float | None = None,
        soft_min_value: int | float | None = None,
        storable: Optional[bool] = None,
        used_as_proxy: Optional[bool] = None,
        writeable: Optional[bool] = None,
    ):

        return super()._create(
            node_name,
            attr_name,
            cached_internally=cached_internally,
            category=category,
            default_value=default_value,
            disconnect_behaviour=disconnect_behaviour,
            keyable=keyable,
            max_value=max_value,
            min_value=min_value,
            nice_name=nice_name,
            parent=parent,
            proxy=proxy,
            readable=readable,
            short_name=short_name,
            soft_max_value=soft_max_value,
            soft_min_value=soft_min_value,
            storable=storable,
            used_as_proxy=used_as_proxy,
            writeable=writeable,
        )


class _AttributeWithCreatedChildren(Attribute):
    @classmethod
    def create(
        cls,
        node_name: str,
        attr_name: str,
        number_of_children: int,
        cached_internally: Optional[bool] = None,
        category: Optional[str] = None,
        disconnect_behaviour: Optional[int] = None,
        keyable: bool = True,
        nice_name: Optional[str] = None,
        parent: Optional[str] = None,
        proxy: Optional[str] = None,
        readable: Optional[bool] = None,
        short_name: Optional[str] = None,
        storable: Optional[bool] = None,
        used_as_proxy: Optional[bool] = None,
        writeable: Optional[bool] = None,
    ):
        return super()._create(
            node_name=node_name,
            attr_name=attr_name,
            cached_internally=cached_internally,
            category=category,
            disconnect_behaviour=disconnect_behaviour,
            keyable=keyable,
            nice_name=nice_name,
            number_of_children=number_of_children,
            parent=parent,
            proxy=proxy,
            readable=readable,
            short_name=short_name,
            storable=storable,
            used_as_proxy=used_as_proxy,
            writeable=writeable,
        )


class FloatAttribute(_NumericAttribute):
    _getter_type = "asDouble"
    _creator_type = "double"


class BoolAttribute(_Attribute):
    _getter_type = "asBool"
    _creator_type = "bool"


class MessageAttribute(_Attribute):
    _getter_type = "kMessage"
    _creator_type = "message"

    @classmethod
    def _get_plug_value(cls, plug: OpenMaya2.MPlug):
        raise MayaBrewAttributeError("Message attributes do not hold data.")

    @classmethod
    def set(cls, value):
        raise MayaBrewAttributeError("Message attributes are not settable.")


class EnumAttribute(Attribute):
    _getter_type = "asShort"
    _creator_type = "enum"

    @classmethod
    def create(
        cls,
        node_name: str,
        attr_name: str,
        enum_data: dict[str, Any],
        cached_internally: Optional[bool] = None,
        category: Optional[str] = None,
        disconnect_behaviour: Optional[int] = None,
        enum_name: Optional[str] = None,
        index_matters: Optional[bool] = None,
        keyable: bool = True,
        max_value: int | float | None = None,
        min_value: int | float | None = None,
        multi: Optional[bool] = None,
        nice_name: Optional[str] = None,
        number_of_children: Optional[int] = None,
        parent: Optional[str] = None,
        proxy: Optional[str] = None,
        readable: Optional[bool] = None,
        short_name: Optional[str] = None,
        soft_max_value: int | float | None = None,
        soft_min_value: int | float | None = None,
        storable: Optional[bool] = None,
        used_as_color: Optional[bool] = None,
        used_as_filename: Optional[bool] = None,
        used_as_proxy: Optional[bool] = None,
        writeable: Optional[bool] = None,
    ):
        maya_enum_string = cls._convert_to_maya_enum_string(enum_data)
        return super()._create(
            node_name=node_name,
            attr_name=attr_name,
            cached_internally=cached_internally,
            category=category,
            disconnect_behaviour=disconnect_behaviour,
            enum_name=maya_enum_string,
            keyable=keyable,
            nice_name=nice_name,
            parent=parent,
            proxy=proxy,
            readable=readable,
            short_name=short_name,
            storable=storable,
            used_as_proxy=used_as_proxy,
            writeable=writeable,
        )

    @staticmethod
    def _convert_to_maya_enum_string(data: dict[str, int]):
        result = []
        used_values = set(v for v in data.values() if v is not None)
        next_value = 0
        for name, value in data.items():
            if value is None:
                while next_value in used_values:
                    next_value += 1
                result.append(f"{name}={next_value}")
                used_values.add(next_value)
                next_value += 1
            else:
                result.append(f"{name}={value}")
        return ":".join(result)


class TypedAttribute(_Attribute):
    """
    Handles Maya kTypedAttribute types. By default, returns the MObject stored in the plug.
    Extend this class if you need to handle specific typed data (e.g., strings, matrices).
    """

    _getter_type = "asMObject"
    _creator_type = "typed"


class CompoundAttribute(_AttributeWithCreatedChildren):
    """
    Handles Maya kCompoundAttribute types. Returns a list of child Attribute instances.
    """

    _creator_type = "compound"


class MultiFloatAttribute(_AttributeWithCreatedChildren):
    _num_children: int
    _creator_type = "double3"


class Float2Attribute(_MultiAttribute):
    """
    Handles Maya kAttribute2Double types (e.g., UV coordinates).
    Returns a tuple of two float values (u, v).
    """

    _num_children = 2
    _creator_type = "double2"
    _creator_type_arg = "dataType"
    _getter_type = "asDouble"


class Float3Attribute(_MultiAttribute):
    """
    Handles Maya kAttribute3Double types (e.g., translate, rotate, scale).
    Returns a tuple of three float values (x, y, z).
    """

    _num_children = 3
    _creator_type = "double3"
    _creator_type_arg = "dataType"
    _getter_type = "asDouble"


class Float4Attribute(_MultiAttribute):
    """
    Handles Maya kAttribute4Double types (e.g., quaternions).
    Returns a tuple of four float values (x, y, z, w).
    """

    _num_children = 4
    _creator_type = "double4"
    _creator_type_arg = "dataType"
    _getter_type = "asDouble"


class MatrixAttribute(_NonNumericAttribute):
    """
    Handles Maya kMatrixAttribute types. Returns an OpenMaya2.MMatrix instance.
    """

    _creator_type = "matrix"
    _creator_type_arg = "dataType"

    @classmethod
    def _get_plug_value(cls, plug: OpenMaya2.MPlug):
        mobj = plug.asMObject()
        matrix_data = OpenMaya2.MFnMatrixData(mobj)
        return matrix_data.matrix()


class GenericAttribute(_Attribute):
    """
    Handles Maya kGenericAttribute types. Returns the MObject stored in the plug, or raises an error if not supported.
    """

    _creator_type = "generic"

    @classmethod
    def _get_plug_value(cls, plug: OpenMaya2.MPlug):
        return plug.asMObject()


_API_TYPE_SUBCLASS_MAP = {
    "kDoubleLinearAttribute": FloatAttribute,
    "kMessageAttribute": MessageAttribute,
    "kNumericAttribute": BoolAttribute,
    "kEnumAttribute": EnumAttribute,
    "kTypedAttribute": TypedAttribute,
    "kCompoundAttribute": CompoundAttribute,
    "kAttribute3Double": Float3Attribute,
    "kAttribute4Double": Float4Attribute,
    "kAttribute2Float": Float2Attribute,
    "kAttribute3Float": Float3Attribute,
    "kDoubleAngleAttribute": FloatAttribute,
    "kMatrixAttribute": MatrixAttribute,
    "kGenericAttribute": GenericAttribute,
}


class AttributeAccessor:
    def __init__(self, node: "Node"):
        self._node = node

    def __getattr__(self, attr_name: str):
        try:
            return Attribute(f"{self._node}.{attr_name}")
        except (ValueError, RuntimeError, NotImplementedError, AttributeError) as e:
            raise MayaBrewAttributeError(
                f"Failed to access attribute '{attr_name}' on node '{self._node}'"
            ) from e
