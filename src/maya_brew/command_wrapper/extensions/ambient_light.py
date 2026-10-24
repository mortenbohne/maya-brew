from ... import _maya_cmds
from ...nodes.node_types import AmbientLight
from ..extension_utils import _node_result, mode_node_command


ambientLight = mode_node_command(
    name="ambientLight",
    command_getter=lambda: _maya_cmds.ambientLight,
    expected_type=AmbientLight,
    result_processor=_node_result,
    docstring="Return an AmbientLight wrapper on creation; edits and queries keep Maya results.",
)
