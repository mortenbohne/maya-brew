from ... import _maya_cmds
from ...nodes.node_types import PointLight
from ..extension_utils import _node_result, mode_node_command


pointLight = mode_node_command(
    name="pointLight",
    command_getter=lambda: _maya_cmds.pointLight,
    expected_type=PointLight,
    result_processor=_node_result,
    docstring="Return a PointLight wrapper on creation; edits and queries keep Maya results.",
)
