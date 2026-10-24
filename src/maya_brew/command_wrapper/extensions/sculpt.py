from ... import _maya_cmds
from ...nodes.node_types import Sculpt
from ..extension_utils import _first_node_result, mode_node_command

sculpt = mode_node_command(
    name="sculpt",
    command_getter=lambda: _maya_cmds.sculpt,
    expected_type=Sculpt,
    result_processor=_first_node_result,
    docstring="Return a Sculpt wrapper on creation; edits and queries keep Maya results.",
)
