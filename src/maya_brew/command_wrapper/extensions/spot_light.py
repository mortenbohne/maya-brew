from ... import _maya_cmds
from ...nodes.node_types import SpotLight
from ..extension_utils import _node_result, mode_node_command


spotLight = mode_node_command(
    name="spotLight",
    command_getter=lambda: _maya_cmds.spotLight,
    expected_type=SpotLight,
    result_processor=_node_result,
    docstring="Return a SpotLight wrapper on creation; edits and queries keep Maya results.",
)
