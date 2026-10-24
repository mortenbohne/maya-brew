from collections.abc import Sequence
from typing import Any, Literal, Never, TypedDict, Unpack, overload

from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_types import Joint

class _JointCreateFlags(TypedDict, total=False):
    edit: Literal[False]
    e: Literal[False]
    query: Literal[False]
    q: Literal[False]
    absolute: bool
    a: bool
    automaticLimits: bool
    al: bool
    autoOrientSecondaryAxis: bool
    aos: bool
    assumePreferredAngles: bool
    apa: bool
    angleX: float | str
    ax: float | str
    angleY: float | str
    ay: float | str
    angleZ: float | str
    az: float | str
    children: bool
    ch: bool
    component: bool
    co: bool
    degreeOfFreedom: str
    dof: str
    limitSwitchX: bool
    lsx: bool
    limitSwitchY: bool
    lsy: bool
    limitSwitchZ: bool
    lsz: bool
    limitX: tuple[float | str, float | str]
    lx: tuple[float | str, float | str]
    limitY: tuple[float | str, float | str]
    ly: tuple[float | str, float | str]
    limitZ: tuple[float | str, float | str]
    lz: tuple[float | str, float | str]
    name: str
    n: str
    orientation: tuple[float | str, float | str, float | str]
    o: tuple[float | str, float | str, float | str]
    orientJoint: str
    oj: str
    position: tuple[float | str, float | str, float | str]
    p: tuple[float | str, float | str, float | str]
    relative: bool
    r: bool
    radius: float
    rad: float
    rotationOrder: str
    roo: str
    scale: tuple[float, float, float]
    s: tuple[float, float, float]
    symmetryAxis: str
    sa: str
    secondaryAxisOrient: str
    sao: str
    scaleCompensate: bool
    sc: bool
    scaleOrientation: tuple[float | str, float | str, float | str]
    so: tuple[float | str, float | str, float | str]
    setPreferredAngles: bool
    spa: bool
    stiffnessX: float
    stx: float
    stiffnessY: float
    sty: float
    stiffnessZ: float
    stz: float
    symmetry: bool
    sym: bool
    zeroScaleOrient: bool
    zso: bool

class _JointModeFlags(TypedDict, total=False):
    edit: bool
    e: bool
    query: bool
    q: bool
    absolute: bool
    a: bool
    automaticLimits: bool
    al: bool
    autoOrientSecondaryAxis: bool
    aos: bool
    assumePreferredAngles: bool
    apa: bool
    angleX: float | str | bool
    ax: float | str | bool
    angleY: float | str | bool
    ay: float | str | bool
    angleZ: float | str | bool
    az: float | str | bool
    children: bool
    ch: bool
    component: bool
    co: bool
    degreeOfFreedom: str | bool
    dof: str | bool
    limitSwitchX: bool
    lsx: bool
    limitSwitchY: bool
    lsy: bool
    limitSwitchZ: bool
    lsz: bool
    limitX: tuple[float | str, float | str] | bool
    lx: tuple[float | str, float | str] | bool
    limitY: tuple[float | str, float | str] | bool
    ly: tuple[float | str, float | str] | bool
    limitZ: tuple[float | str, float | str] | bool
    lz: tuple[float | str, float | str] | bool
    name: str | bool
    n: str | bool
    orientation: tuple[float | str, float | str, float | str] | bool
    o: tuple[float | str, float | str, float | str] | bool
    orientJoint: str
    oj: str
    position: tuple[float | str, float | str, float | str] | bool
    p: tuple[float | str, float | str, float | str] | bool
    relative: bool
    r: bool
    radius: float
    rad: float
    rotationOrder: str | bool
    roo: str | bool
    scale: tuple[float, float, float] | bool
    s: tuple[float, float, float] | bool
    symmetryAxis: str
    sa: str
    secondaryAxisOrient: str
    sao: str
    scaleCompensate: bool
    sc: bool
    scaleOrientation: tuple[float | str, float | str, float | str] | bool
    so: tuple[float | str, float | str, float | str] | bool
    setPreferredAngles: bool
    spa: bool
    stiffnessX: float
    stx: float
    stiffnessY: float
    sty: float
    stiffnessZ: float
    stz: float
    symmetry: bool
    sym: bool
    zeroScaleOrient: bool
    zso: bool

@overload
def joint(
    *args: str | Node | Sequence[str | Node],
    exists: Never = ...,
    ex: Never = ...,
    **kwargs: Unpack[_JointCreateFlags],
) -> Joint: ...
@overload
def joint(
    *args: str | Node | Sequence[str | Node],
    exists: str | bool,
    ex: str | bool = ...,
    **kwargs: Unpack[_JointModeFlags],
) -> bool: ...
@overload
def joint(
    *args: str | Node | Sequence[str | Node],
    ex: str | bool,
    exists: str | bool = ...,
    **kwargs: Unpack[_JointModeFlags],
) -> bool: ...
@overload
def joint(
    *args: str | Node | Sequence[str | Node],
    exists: str | bool = ...,
    ex: str | bool = ...,
    **kwargs: Unpack[_JointModeFlags],
) -> Any: ...
