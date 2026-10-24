from ... import _maya_cmds
from ...nodes.node_types import SoftMod
from ..extension_utils import _first_node_result, mode_node_command


softMod = mode_node_command(
    name="softMod",
    command_getter=lambda: _maya_cmds.softMod,
    expected_type=SoftMod,
    result_processor=_first_node_result,
    docstring="Return a SoftMod wrapper on creation; edits and queries keep Maya results.",
)
