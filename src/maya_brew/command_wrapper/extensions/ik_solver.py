from ... import _maya_cmds
from ...nodes.node_types import IkSolver
from ..extension_utils import _node_result, mode_node_command

ikSolver = mode_node_command(
    name="ikSolver",
    command_getter=lambda: _maya_cmds.ikSolver,
    expected_type=IkSolver,
    result_processor=_node_result,
    docstring=(
        "Return a native solver wrapper on creation instead of its name.\n\n"
        "Accept wrapped targets individually or in flat sequences. Edits and "
        "queries retain Maya's results. Maya runtime errors are raised as "
        "NodeException."
    ),
)
