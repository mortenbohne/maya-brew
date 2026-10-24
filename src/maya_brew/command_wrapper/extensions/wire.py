from ... import _maya_cmds
from ...nodes.node_types import Wire
from ..extension_utils import _first_node_result, mode_node_command

wire = mode_node_command(
    name="wire",
    command_getter=lambda: _maya_cmds.wire,
    expected_type=Wire,
    result_processor=_first_node_result,
    docstring="Return a Wire wrapper on creation; edits and queries keep Maya results.",
)
