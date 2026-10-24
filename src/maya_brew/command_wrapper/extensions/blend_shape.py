from ... import _maya_cmds
from ...nodes.node_types import BlendShape
from ..extension_utils import _single_node_result, mode_node_command

blendShape = mode_node_command(
    name="blendShape",
    command_getter=lambda: _maya_cmds.blendShape,
    expected_type=BlendShape,
    result_processor=_single_node_result,
    docstring="Return a BlendShape wrapper on creation; edits and queries keep Maya results.",
)
