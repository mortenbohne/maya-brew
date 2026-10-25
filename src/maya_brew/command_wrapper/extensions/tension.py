from ... import _maya_cmds
from ...nodes.node_types import Tension
from ..extension_utils import _single_node_result, mode_node_command

tension = mode_node_command(
    name="tension",
    command_getter=lambda: _maya_cmds.tension,
    expected_type=Tension,
    result_processor=_single_node_result,
    docstring="Return a Tension wrapper on creation; edits and queries keep Maya results.",
)
