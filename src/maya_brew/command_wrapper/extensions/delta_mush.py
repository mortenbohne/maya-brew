from ... import _maya_cmds
from ...nodes.node_types import DeltaMush
from ..extension_utils import _single_node_result, mode_node_command


deltaMush = mode_node_command(
    name="deltaMush",
    command_getter=lambda: _maya_cmds.deltaMush,
    expected_type=DeltaMush,
    result_processor=_single_node_result,
    docstring="Return a DeltaMush wrapper on creation; edits and queries keep Maya results.",
)
