from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.casting import cast
from ...nodes.node_types import Joint
from ..extension_utils import _node_target_names


def insertJoint(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Joint:
    """Return the inserted Joint wrapper instead of its name.

    Accept wrapped targets individually or in flat sequences. Preserve Maya's
    selection and parenting behavior. Maya runtime errors become NodeException.
    """
    targets = _node_target_names(args)
    try:
        result: Any = _maya_cmds.insertJoint(*targets, **kwargs)
    except RuntimeError as e:
        raise NodeException(f"insertJoint failed: {e}") from e
    if not isinstance(result, str):
        raise NodeException(f"Unexpected result from insertJoint: {result!r}")
    return cast(result, Joint)
