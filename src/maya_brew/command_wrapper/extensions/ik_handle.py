from collections.abc import Sequence
from typing import Any

from ... import _maya_cmds
from ...exceptions import NodeException
from ...nodes._foundation.node_extensions import Node
from ...nodes.casting import cast
from ...nodes.node_types import IkEffector, IkHandle, Transform
from ..extension_utils import _node_target_names


def ikHandle(*args: str | Node | Sequence[str | Node], **kwargs: Any) -> Any:
    """Return created handle/effector nodes as a tuple of wrappers.

    Preserve Maya's result order and length: an existing effector can leave only
    the handle, and a returned spline curve adds its transform as a third item.
    Edits and queries, including node-name and joint-list queries, retain Maya's results.
    Accept wrapped targets individually or in flat sequences, and wrapped nodes
    for startJoint/sj, endEffector/ee, curve/c, and solver/sol.
    Selection and flag behavior are unchanged, including exists/ex results
    without query mode. Maya runtime errors are raised as NodeException.
    """
    targets = _node_target_names(args)
    for flag in (
        "startJoint",
        "sj",
        "endEffector",
        "ee",
        "curve",
        "c",
        "solver",
        "sol",
    ):
        if isinstance(kwargs.get(flag), Node):
            kwargs[flag] = str(kwargs[flag])
    try:
        result = _maya_cmds.ikHandle(*targets, **kwargs)
    except RuntimeError as e:
        raise NodeException(f"ikHandle failed: {e}") from e
    if any(kwargs.get(flag) for flag in ("edit", "e", "query", "q")) or any(
        flag in kwargs for flag in ("exists", "ex")
    ):
        return result
    if (
        not isinstance(result, list)
        or len(result) not in (1, 2, 3)
        or not all(isinstance(name, str) for name in result)
    ):
        raise NodeException(f"Unexpected result from ikHandle: {result!r}")
    handle = cast(result[0], IkHandle)
    if len(result) == 1:
        return (handle,)
    effector = cast(result[1], IkEffector)
    if len(result) == 3:
        return handle, effector, cast(result[2], Transform)
    return handle, effector
