from ... import _maya_cmds
from ...nodes.node_types import DirectionalLight
from ..extension_utils import _node_result, mode_node_command

directionalLight = mode_node_command(
    name="directionalLight",
    command_getter=lambda: _maya_cmds.directionalLight,
    expected_type=DirectionalLight,
    result_processor=_node_result,
    docstring="Return a DirectionalLight wrapper on creation; edits and queries keep Maya results.",
)
