from ... import _maya_cmds
from ...nodes.node_types import Ffd
from ..extension_utils import _first_node_result, mode_node_command

lattice = mode_node_command(
    name="lattice",
    command_getter=lambda: _maya_cmds.lattice,
    expected_type=Ffd,
    result_processor=_first_node_result,
    docstring="Return an Ffd wrapper on creation; edits and queries keep Maya results.",
)
