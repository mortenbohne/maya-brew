from dataclasses import dataclass
from typing import Any

import maya.cmds as maya_cmds
import pytest
from maya_brew import cmds


@dataclass(frozen=True)
class PrimitiveCase:
    command: str
    creation: dict[str, Any]
    edits: tuple[tuple[str, str, Any], ...]
    queries: tuple[str, ...] = ()
    approximate: bool = False

    @property
    def query_flags(self) -> tuple[str, ...]:
        return self.queries or tuple(
            flag for name, alias, _ in self.edits for flag in (name, alias)
        )


CASES = [
    PrimitiveCase(
        "polyCone",
        dict(radius=2.0, height=3.0, sx=8, sy=2, sz=1),
        (
            ("radius", "r", 4.0),
            ("height", "h", 5.0),
            ("roundCap", "rcp", True),
            ("subdivisionsAxis", "sa", 10),
            ("subdivisionsCap", "sc", 2),
            ("subdivisionsHeight", "sh", 3),
            ("subdivisionsX", "sx", 10),
            ("subdivisionsY", "sy", 3),
            ("subdivisionsZ", "sz", 2),
            ("createUVs", "cuv", 0),
            ("texture", "tx", False),
        ),
    ),
    PrimitiveCase(
        "polyCube",
        dict(width=2.0, height=3.0, depth=4.0, sx=2, sy=3, sz=4),
        (("width", "w", 5.0), ("height", "h", 5.0), ("depth", "d", 5.0)),
        queries=(
            "width",
            "w",
            "height",
            "h",
            "depth",
            "d",
            "subdivisionsWidth",
            "sw",
            "subdivisionsHeight",
            "sh",
            "subdivisionsDepth",
            "sd",
            "subdivisionsX",
            "sx",
            "subdivisionsY",
            "sy",
            "subdivisionsZ",
            "sz",
            "createUVs",
            "cuv",
            "texture",
            "tx",
        ),
    ),
    PrimitiveCase(
        "polyCylinder",
        dict(radius=2.0, height=3.0, sx=8, sy=2, sz=1),
        (
            ("radius", "r", 4.0),
            ("height", "h", 5.0),
            ("roundCap", "rcp", True),
            ("roundCapHeightCompensation", "rch", False),
            ("subdivisionsAxis", "sa", 10),
            ("subdivisionsCaps", "sc", 2),
            ("subdivisionsHeight", "sh", 3),
            ("subdivisionsX", "sx", 10),
            ("subdivisionsY", "sy", 3),
            ("subdivisionsZ", "sz", 2),
            ("createUVs", "cuv", 0),
            ("texture", "tx", 1),
        ),
    ),
    PrimitiveCase(
        "polyHelix",
        dict(coils=2.5, height=4.0, width=3.0, radius=0.25, sa=8, sco=12),
        (
            ("coils", "c", 3.5),
            ("direction", "d", 0),
            ("height", "h", 5.0),
            ("width", "w", 4.0),
            ("radius", "r", 0.5),
            ("roundCap", "rcp", True),
            ("subdivisionsAxis", "sa", 10),
            ("subdivisionsCaps", "sc", 2),
            ("subdivisionsCoil", "sco", 16),
            ("createUVs", "cuv", 0),
            ("texture", "tx", 0),
            ("useOldInitBehaviour", "oib", True),
        ),
        approximate=True,
    ),
    PrimitiveCase(
        "polyPipe",
        dict(radius=3.0, height=4.0, thickness=0.5, sa=8, sc=2, sh=3),
        (
            ("radius", "r", 4.0),
            ("height", "h", 5.0),
            ("thickness", "t", 0.75),
            ("roundCap", "rcp", True),
            ("roundCapHeightCompensation", "rch", True),
            ("subdivisionsAxis", "sa", 10),
            ("subdivisionsCaps", "sc", 3),
            ("subdivisionsHeight", "sh", 4),
            ("createUVs", "cuv", False),
            ("texture", "tx", False),
        ),
        approximate=True,
    ),
    PrimitiveCase(
        "polyPlane",
        dict(width=2.0, height=3.0, sx=2, sy=3),
        (("width", "w", 5.0),),
        queries=("width", "w", "height", "h", "sx", "sy"),
    ),
    PrimitiveCase(
        "polyPlatonicSolid",
        dict(radius=2.0, solidType=1),
        (
            ("radius", "r", 3.0),
            ("sideLength", "l", 2.0),
            ("solidType", "st", 2),
            ("createUVs", "cuv", 0),
            ("texture", "tx", 0),
        ),
        approximate=True,
    ),
    *[
        PrimitiveCase(
            "polyPrimitive",
            {"radius": 2.0, type_flag: 0},
            (
                ("radius", "r", 3.0),
                ("sideLength", "l", 0.8),
                ("createUVs", "cuv", 0),
                ("texture", "tx", 0),
            ),
            queries=(
                "radius",
                "r",
                "sideLength",
                "l",
                "polyType",
                "pt",
                "createUVs",
                "cuv",
                "texture",
                "tx",
            ),
            approximate=True,
        )
        for type_flag in ("polyType", "pt")
    ],
    PrimitiveCase(
        "polyPrism",
        dict(sideLength=2.0, length=3.0, numberOfSides=5, sc=2, sh=3),
        (
            ("sideLength", "w", 4.0),
            ("length", "l", 5.0),
            ("numberOfSides", "ns", 6),
            # Maya exposes this misspelled flag alongside numberOfSides.
            ("numderOfSides", "nsi", 6),
            ("subdivisionsCaps", "sc", 3),
            ("subdivisionsHeight", "sh", 4),
            ("createUVs", "cuv", 0),
            ("texture", "tx", 0),
        ),
    ),
    PrimitiveCase(
        "polyPyramid",
        dict(sideLength=2.0, numberOfSides=5, sc=2, sh=3),
        (
            ("sideLength", "w", 4.0),
            ("numberOfSides", "ns", 6),
            ("numderOfSides", "nsi", 6),
            ("subdivisionsCaps", "sc", 3),
            ("subdivisionsHeight", "sh", 4),
            ("createUVs", "cuv", 0),
            ("texture", "tx", False),
        ),
    ),
    PrimitiveCase(
        "polySphere",
        dict(radius=2.0, subdivisionsX=10, subdivisionsY=15),
        (("radius", "r", 3.0),),
        queries=("radius", "r", "sx", "subdivisionsY"),
    ),
    PrimitiveCase(
        "polyTorus",
        dict(radius=3.0, sectionRadius=0.5, sx=8, sy=6, twist=30.0),
        (
            ("radius", "r", 4.0),
            ("sectionRadius", "sr", 0.75),
            ("twist", "tw", 45.0),
            ("subdivisionsAxis", "sa", 10),
            ("subdivisionsHeight", "sh", 8),
            ("subdivisionsX", "sx", 10),
            ("subdivisionsY", "sy", 8),
            ("createUVs", "cuv", False),
            ("texture", "tx", False),
        ),
        approximate=True,
    ),
]


@pytest.fixture
def primitive_case(request):
    case = request.param
    command = getattr(cmds, case.command)
    return case, command, command(**case.creation)


@pytest.mark.parametrize(
    "primitive_case, flag",
    [
        pytest.param(case, flag, id=f"{case.command}-{flag}")
        for case in CASES
        for flag in case.query_flags
    ],
    indirect=["primitive_case"],
)
@pytest.mark.parametrize("target", [0, 1])
@pytest.mark.parametrize("query", ["query", "q"])
def test_queries_match_maya(primitive_case, flag, target, query):
    case, command, nodes = primitive_case
    flags = {query: True, flag: True}
    assert command(nodes[target], **flags) == getattr(maya_cmds, case.command)(
        str(nodes[target]), **flags
    )


@pytest.mark.parametrize(
    "primitive_case, flag, value",
    [
        pytest.param(case, flag, value, id=f"{case.command}-{flag}")
        for case in CASES
        for name, alias, value in case.edits
        for flag in (name, alias)
    ],
    indirect=["primitive_case"],
)
@pytest.mark.parametrize("edit", ["edit", "e"])
@pytest.mark.parametrize("query", ["query", "q"])
def test_edits_wrapped_target(primitive_case, flag, value, edit, query):
    case, command, nodes = primitive_case
    assert command(nodes[1], **{edit: True, flag: value}) == "Values edited."
    expected = pytest.approx(float(value)) if case.approximate else value
    assert command(nodes[1], **{query: True, flag: True}) == expected
