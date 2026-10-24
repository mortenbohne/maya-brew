from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.node_types import Cluster
from ..extension_utils import _first_node_result, mode_node_command


_cluster_command = mode_node_command(
    name="cluster",
    command_getter=lambda: _maya_cmds.cluster,
    expected_type=Cluster,
    result_processor=_first_node_result,
    docstring="Return a Cluster wrapper on creation; edits and queries keep Maya results.",
)


def cluster(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    try:
        return _cluster_command(*args, **kwargs)
    except NodeException as e:
        if "Transforms not related in hierarchy." in str(e) and any(
            flag in kwargs for flag in ("weightedNode", "wn")
        ):
            raise NodeException(
                "cluster weightedNode expects related parent/child transforms"
            ) from e
        raise



