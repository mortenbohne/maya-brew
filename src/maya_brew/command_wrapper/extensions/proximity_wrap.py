from ... import _maya_cmds
from ...nodes.node_types import ProximityWrap
from ..extension_utils import _single_node_result, mode_node_command


proximityWrap = mode_node_command(
    name="proximityWrap",
    command_getter=lambda: _maya_cmds.proximityWrap,
    expected_type=ProximityWrap,
    result_processor=_single_node_result,
    docstring="Return a ProximityWrap wrapper on creation; edits and queries keep Maya results.",
)
