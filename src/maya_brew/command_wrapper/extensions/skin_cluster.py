from ... import _maya_cmds
from ...nodes.node_types import SkinCluster
from ..extension_utils import _single_node_result, mode_node_command


skinCluster = mode_node_command(
    name="skinCluster",
    command_getter=lambda: _maya_cmds.skinCluster,
    expected_type=SkinCluster,
    result_processor=_single_node_result,
    docstring="Return a SkinCluster wrapper on creation; edits and queries keep Maya results.",
)
