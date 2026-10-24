from typing import Any, Literal, assert_type

from maya_brew import cmds
from maya_brew.command_wrapper import (
    circle,
    cone,
    connectJoint,
    createNode,
    cylinder,
    ikHandle,
    ikHandleDisplayScale,
    ikSolver,
    ikSystemInfo,
    insertJoint,
    joint,
    jointDisplayScale,
    ls,
    mirrorJoint,
    nurbsCube,
    nurbsPlane,
    nurbsSquare,
    polyCone,
    polyCube,
    polyCylinder,
    polyHelix,
    polyPipe,
    polyPlane,
    polyPlatonicSolid,
    polyPrimitive,
    polyPrism,
    polyPyramid,
    polySphere,
    polyTorus,
    removeJoint,
    sphere,
    torus,
)
from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import (
    IkEffector,
    IkHandle,
    IkSolver,
    Joint,
    MakeNurbCircle,
    MakeNurbCone,
    MakeNurbCube,
    MakeNurbCylinder,
    MakeNurbPlane,
    MakeNurbSphere,
    MakeNurbTorus,
    MakeNurbsSquare,
    PolyCone,
    PolyCube,
    PolyCylinder,
    PolyHelix,
    PolyPipe,
    PolyPlane,
    PolyPlatonicSolid,
    PolyPrimitiveMisc,
    PolyPrism,
    PolyPyramid,
    PolySphere,
    PolyTorus,
    Transform,
)


class CustomJoint(Joint):
    pass


def check_global_setting_types(mode: bool) -> None:
    assert_type(cmds.ikHandleDisplayScale(0.5), float | None)
    assert_type(ikHandleDisplayScale(query=True), float | None)
    assert_type(ikHandleDisplayScale(q=mode), float | None)
    assert_type(cmds.ikSystemInfo(globalSnapHandle=False), bool | None)
    assert_type(ikSystemInfo(False, gsh=True), bool | None)
    assert_type(ikSystemInfo(q=True, gsh=True), bool | None)
    assert_type(ikSystemInfo(query=mode, globalSnapHandle=True), bool | None)
    assert_type(cmds.jointDisplayScale(2.0, absolute=True), float | None)
    assert_type(jointDisplayScale(1, a=False, ikfk=0.5), float | None)
    assert_type(jointDisplayScale(query=True, ik=True), float | None)
    assert_type(jointDisplayScale(q=mode, ikfk=True), float | None)
    ikHandleDisplayScale("handle")  # type: ignore[arg-type]
    ikSystemInfo("on")  # type: ignore[arg-type]
    jointDisplayScale("joint")  # type: ignore[arg-type]


def check_joint_operation_types(target: Joint) -> None:
    assert_type(cmds.insertJoint(target), Joint)
    assert_type(insertJoint([target]), Joint)
    assert_type(insertJoint(), Joint)
    assert_type(cmds.mirrorJoint(target, mirrorYZ=True), tuple[Node, ...])
    assert_type(mirrorJoint([target], sr=("left_", "right_")), tuple[Node, ...])
    assert_type(mirrorJoint(myz=True, mb=True), tuple[Node, ...])
    assert_type(cmds.connectJoint(target, "parent", parentMode=True), None)
    assert_type(connectJoint((target, "parent"), cm=True), None)
    assert_type(connectJoint(), None)
    assert_type(cmds.removeJoint(target), None)
    assert_type(removeJoint([target, "other"]), None)
    assert_type(removeJoint(), None)


def check_ik_handle_types(target: Joint, curve: Transform, mode: bool) -> None:
    assert_type(
        cmds.ikHandle(sj=target, ee="tip"),
        tuple[IkHandle]
        | tuple[IkHandle, IkEffector]
        | tuple[IkHandle, IkEffector, Transform],
    )
    assert_type(
        ikHandle([target, "tip"], solver="ikSplineSolver", c=curve, ccv=False),
        tuple[IkHandle]
        | tuple[IkHandle, IkEffector]
        | tuple[IkHandle, IkEffector, Transform],
    )
    assert_type(ikHandle("handle", q=True, jointList=True), Any)
    assert_type(ikHandle("handle", query=True, startJoint=True), Any)
    assert_type(ikHandle("handle", e=True, weight=0.5), Any)
    assert_type(ikHandle("handle", edit=True, endEffector=target), Any)
    assert_type(ikHandle(exists="handle"), Any)
    assert_type(ikHandle(ex=False, q=True), Any)
    assert_type(ikHandle("handle", query=mode, sj=True), Any)
    assert_type(ikHandle("handle", e=mode, w=0.5), Any)


def check_ik_solver_types(target: IkSolver, mode: bool) -> None:
    assert_type(cmds.ikSolver(st="ikSCsolver"), IkSolver)
    assert_type(ikSolver(solverType="ikRPsolver", epsilon=0.5), IkSolver)
    assert_type(ikSolver(st="ikSplineSolver", q=False, e=False), IkSolver)
    assert_type(ikSolver(target, q=True, epsilon=True), Any)
    assert_type(ikSolver([target], query=True, name=True), Any)
    assert_type(ikSolver((target,), e=True, mxi=25), Any)
    assert_type(ikSolver(str(target), edit=True, ep=0.25), Any)
    assert_type(ikSolver(target, query=mode, st=True), Any)
    assert_type(ikSolver(target, e=mode, mxi=50), Any)


def check_joint_types(target: Joint, mode: bool) -> None:
    assert_type(cmds.joint(), Joint)
    assert_type(joint(name="root", position=(0, 1, 2)), Joint)
    assert_type(joint(target, p=(1, 2, 3), r=True), Joint)
    assert_type(joint(q=False, edit=False, ax="90deg"), Joint)
    assert_type(joint(lz=("-90deg", "90deg"), lsz=False), Joint)
    assert_type(joint(target, query=True, position=True), Any)
    assert_type(joint(target, q=True, name=True), Any)
    assert_type(joint([target], edit=True, radius=2), Any)
    assert_type(joint((target, "other"), e=True, oj="xyz", sao="yup"), Any)
    assert_type(joint(exists="root"), bool)
    assert_type(joint(ex="root", e=True), bool)
    assert_type(joint(exists=False), bool)
    assert_type(joint(target, query=mode, position=True), Any)
    assert_type(joint(target, e=mode, radius=2), Any)


def check_nurbs_primitive_types(history: bool, create_object: bool) -> None:
    circle_nodes = cmds.circle()
    assert_type(circle_nodes, tuple[Transform, MakeNurbCircle])
    assert_type(circle(ch=False), tuple[Transform])
    assert_type(circle(object=False), tuple[MakeNurbCircle])
    assert_type(circle(o=False, ch=False), tuple[MakeNurbCircle])
    assert_type(
        circle(constructionHistory=history, object=create_object),
        tuple[Transform, MakeNurbCircle] | tuple[Transform] | tuple[MakeNurbCircle],
    )
    assert_type(circle(circle_nodes[1], query=True, radius=True), Any)
    assert_type(circle(circle_nodes[1], q=True, r=True), Any)
    assert_type(
        circle(circle_nodes[1], edit=True, radius=3.0), Literal["Values edited."]
    )

    cone_nodes = cmds.cone()
    assert_type(cone_nodes, tuple[Transform, MakeNurbCone])
    assert_type(cone(cone_nodes[1], q=True, nodeState=True), NodeState)
    assert_type(cone(cone_nodes[1], q=True, radius=True), Any)
    assert_type(cone(cone_nodes[1], e=True, radius=3.0), Literal["Values edited."])

    cylinder_nodes = cmds.cylinder()
    assert_type(cylinder_nodes, tuple[Transform, MakeNurbCylinder])
    assert_type(cylinder(cylinder_nodes[1], q=True, nodeState=True), NodeState)

    sphere_nodes = cmds.sphere()
    assert_type(sphere_nodes, tuple[Transform, MakeNurbSphere])
    assert_type(sphere(sphere_nodes[1], q=True, nodeState=True), NodeState)

    torus_nodes = cmds.torus()
    assert_type(torus_nodes, tuple[Transform, MakeNurbTorus])
    assert_type(torus(torus_nodes[1], q=True, nodeState=True), NodeState)

    nurbs_plane_nodes = cmds.nurbsPlane()
    assert_type(nurbs_plane_nodes, tuple[Transform, MakeNurbPlane])
    assert_type(nurbsPlane(nurbs_plane_nodes[1], q=True, nodeState=True), NodeState)

    nurbs_cube_nodes = cmds.nurbsCube()
    assert_type(nurbs_cube_nodes, tuple[Transform, MakeNurbCube])
    assert_type(nurbsCube(nurbs_cube_nodes[1], q=True, nodeState=True), NodeState)

    nurbs_square_nodes = cmds.nurbsSquare()
    assert_type(nurbs_square_nodes, tuple[Transform, MakeNurbsSquare])
    assert_type(nurbsSquare(nurbs_square_nodes[1], q=True, nodeState=True), NodeState)


def check_poly_primitive_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyPrimitive()
    assert_type(nodes, tuple[Transform, PolyPrimitiveMisc])
    assert_type(polyPrimitive(ch=False), tuple[Transform])
    assert_type(polyPrimitive(constructionHistory=False), tuple[Transform])
    assert_type(polyPrimitive(object=False), tuple[PolyPrimitiveMisc])
    assert_type(polyPrimitive(o=False, ch=False), tuple[PolyPrimitiveMisc])
    assert_type(
        polyPrimitive(constructionHistory=history, object=create_object),
        tuple[Transform, PolyPrimitiveMisc]
        | tuple[Transform]
        | tuple[PolyPrimitiveMisc],
    )
    assert_type(polyPrimitive(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyPrimitive(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyPrimitive(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyPrimitive(nodes[0], q=True, nds=True), NodeState)
    assert_type(
        polyPrimitive(nodes[1], edit=True, radius=3.0), Literal["Values edited."]
    )
    assert_type(polyPrimitive(nodes[0], e=True, l=2.0), Literal["Values edited."])
    assert_type(polyPrimitive(nodes[1], q=True, sideLength=True), Any)
    assert_type(
        polyPrimitive(
            axis=(0.0, 1.0, 0.0),
            radius=2.0,
            sideLength=0.8,
            polyType=0,
            createUVs=4,
            texture=0,
        ),
        tuple[Transform, PolyPrimitiveMisc],
    )
    assert_type(
        polyPrimitive(pt=0, r=2.0, l=0.8, cuv=4, tx=0),
        tuple[Transform, PolyPrimitiveMisc],
    )


def check_poly_platonic_solid_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyPlatonicSolid()
    assert_type(nodes, tuple[Transform, PolyPlatonicSolid])
    assert_type(polyPlatonicSolid(ch=False), tuple[Transform])
    assert_type(polyPlatonicSolid(constructionHistory=False), tuple[Transform])
    assert_type(polyPlatonicSolid(object=False), tuple[PolyPlatonicSolid])
    assert_type(polyPlatonicSolid(o=False, ch=False), tuple[PolyPlatonicSolid])
    assert_type(
        polyPlatonicSolid(constructionHistory=history, object=create_object),
        tuple[Transform, PolyPlatonicSolid]
        | tuple[Transform]
        | tuple[PolyPlatonicSolid],
    )
    assert_type(polyPlatonicSolid(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyPlatonicSolid(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyPlatonicSolid(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyPlatonicSolid(nodes[0], q=True, nds=True), NodeState)
    assert_type(
        polyPlatonicSolid(nodes[1], edit=True, radius=3.0), Literal["Values edited."]
    )
    assert_type(polyPlatonicSolid(nodes[0], e=True, l=2.0), Literal["Values edited."])
    assert_type(polyPlatonicSolid(nodes[1], q=True, sideLength=True), Any)
    assert_type(
        polyPlatonicSolid(
            axis=(0.0, 1.0, 0.0),
            radius=2.0,
            sideLength=2.0,
            solidType=1,
            createUVs=4,
            texture=0,
        ),
        tuple[Transform, PolyPlatonicSolid],
    )
    assert_type(
        polyPlatonicSolid(st=2, r=2.0, l=2.0, cuv=4, tx=0),
        tuple[Transform, PolyPlatonicSolid],
    )


def check_poly_helix_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyHelix()
    assert_type(nodes, tuple[Transform, PolyHelix])
    assert_type(polyHelix(ch=False), tuple[Transform])
    assert_type(polyHelix(constructionHistory=False), tuple[Transform])
    assert_type(polyHelix(object=False), tuple[PolyHelix])
    assert_type(polyHelix(o=False, ch=False), tuple[PolyHelix])
    assert_type(
        polyHelix(constructionHistory=history, object=create_object),
        tuple[Transform, PolyHelix] | tuple[Transform] | tuple[PolyHelix],
    )
    assert_type(polyHelix(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyHelix(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyHelix(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyHelix(nodes[0], q=True, nds=True), NodeState)
    assert_type(polyHelix(nodes[1], edit=True, coils=4.5), Literal["Values edited."])
    assert_type(polyHelix(nodes[0], e=True, cuv=0, tx=0), Literal["Values edited."])
    assert_type(polyHelix(nodes[1], q=True, width=True), Any)
    assert_type(
        polyHelix(
            axis=(0.0, 1.0, 0.0),
            coils=3.5,
            direction=1,
            height=4.0,
            width=2.0,
            radius=0.25,
            roundCap=True,
            subdivisionsAxis=8,
            subdivisionsCaps=2,
            subdivisionsCoil=12,
            createUVs=2,
            texture=2,
            useOldInitBehaviour=False,
        ),
        tuple[Transform, PolyHelix],
    )
    assert_type(
        polyHelix(
            c=3.5, d=0, h=4.0, w=2.0, r=0.25, rcp=True, sa=8, sc=2, sco=12, oib=True
        ),
        tuple[Transform, PolyHelix],
    )


def check_poly_prism_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyPrism()
    assert_type(nodes, tuple[Transform, PolyPrism])
    assert_type(polyPrism(ch=False), tuple[Transform])
    assert_type(polyPrism(constructionHistory=False), tuple[Transform])
    assert_type(polyPrism(object=False), tuple[PolyPrism])
    assert_type(polyPrism(o=False, ch=False), tuple[PolyPrism])
    assert_type(
        polyPrism(constructionHistory=history, object=create_object),
        tuple[Transform, PolyPrism] | tuple[Transform] | tuple[PolyPrism],
    )
    assert_type(polyPrism(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyPrism(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyPrism(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyPrism(nodes[0], q=True, nds=True), NodeState)
    assert_type(polyPrism(nodes[1], edit=True, length=5.0), Literal["Values edited."])
    assert_type(polyPrism(nodes[0], e=True, cuv=0, tx=0), Literal["Values edited."])
    assert_type(polyPrism(nodes[1], q=True, sideLength=True), Any)
    assert_type(
        polyPrism(axis=(0.0, 1.0, 0.0), length=3.0, numberOfSides=5, createUVs=2),
        tuple[Transform, PolyPrism],
    )
    assert_type(polyPrism(numderOfSides=6, l=4.0), tuple[Transform, PolyPrism])
    assert_type(polyPrism(nsi=6, ns=6), tuple[Transform, PolyPrism])


def check_poly_pipe_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyPipe()
    assert_type(nodes, tuple[Transform, PolyPipe])
    assert_type(polyPipe(ch=False), tuple[Transform])
    assert_type(polyPipe(constructionHistory=False), tuple[Transform])
    assert_type(polyPipe(object=False), tuple[PolyPipe])
    assert_type(polyPipe(o=False, ch=False), tuple[PolyPipe])
    assert_type(
        polyPipe(constructionHistory=history, object=create_object),
        tuple[Transform, PolyPipe] | tuple[Transform] | tuple[PolyPipe],
    )
    assert_type(polyPipe(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyPipe(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyPipe(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyPipe(nodes[0], q=True, nds=True), NodeState)
    assert_type(
        polyPipe(nodes[1], edit=True, thickness=0.75), Literal["Values edited."]
    )
    assert_type(
        polyPipe(nodes[0], e=True, cuv=False, tx=False), Literal["Values edited."]
    )
    assert_type(polyPipe(nodes[1], q=True, thickness=True), Any)
    assert_type(
        polyPipe(axis=(0.0, 1.0, 0.0), thickness=0.5, h=3.0, createUVs=False),
        tuple[Transform, PolyPipe],
    )


def check_poly_torus_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyTorus()
    assert_type(nodes, tuple[Transform, PolyTorus])
    assert_type(polyTorus(ch=False), tuple[Transform])
    assert_type(polyTorus(constructionHistory=False), tuple[Transform])
    assert_type(polyTorus(object=False), tuple[PolyTorus])
    assert_type(polyTorus(o=False, ch=False), tuple[PolyTorus])
    assert_type(
        polyTorus(constructionHistory=history, object=create_object),
        tuple[Transform, PolyTorus] | tuple[Transform] | tuple[PolyTorus],
    )
    assert_type(polyTorus(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyTorus(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyTorus(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyTorus(nodes[0], q=True, nds=True), NodeState)
    assert_type(polyTorus(nodes[1], edit=True, twist=45.0), Literal["Values edited."])
    assert_type(
        polyTorus(nodes[0], e=True, cuv=False, tx=False), Literal["Values edited."]
    )
    assert_type(polyTorus(nodes[1], q=True, sectionRadius=True), Any)
    assert_type(
        polyTorus(axis=(0.0, 1.0, 0.0), sectionRadius=0.5, tw=30.0, createUVs=False),
        tuple[Transform, PolyTorus],
    )


def check_poly_cylinder_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyCylinder()
    assert_type(nodes, tuple[Transform, PolyCylinder])
    assert_type(polyCylinder(ch=False), tuple[Transform])
    assert_type(polyCylinder(constructionHistory=False), tuple[Transform])
    assert_type(polyCylinder(object=False), tuple[PolyCylinder])
    assert_type(polyCylinder(o=False, ch=False), tuple[PolyCylinder])
    assert_type(
        polyCylinder(constructionHistory=history, object=create_object),
        tuple[Transform, PolyCylinder] | tuple[Transform] | tuple[PolyCylinder],
    )
    assert_type(polyCylinder(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyCylinder(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyCylinder(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyCylinder(nodes[0], q=True, nds=True), NodeState)
    assert_type(
        polyCylinder(nodes[1], edit=True, radius=2.0), Literal["Values edited."]
    )
    assert_type(
        polyCylinder(nodes[0], e=True, rcp=True, tx=1), Literal["Values edited."]
    )
    assert_type(polyCylinder(nodes[1], q=True, radius=True), Any)
    assert_type(
        polyCylinder(axis=(0.0, 1.0, 0.0), subdivisionsCaps=2, texture=1, rch=False),
        tuple[Transform, PolyCylinder],
    )


def check_poly_cone_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyCone()
    assert_type(nodes, tuple[Transform, PolyCone])
    assert_type(polyCone(ch=False), tuple[Transform])
    assert_type(polyCone(constructionHistory=False), tuple[Transform])
    assert_type(polyCone(object=False), tuple[PolyCone])
    assert_type(polyCone(o=False, ch=False), tuple[PolyCone])
    assert_type(
        polyCone(constructionHistory=history, object=create_object),
        tuple[Transform, PolyCone] | tuple[Transform] | tuple[PolyCone],
    )
    assert_type(polyCone(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyCone(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyCone(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyCone(nodes[0], q=True, nds=True), NodeState)
    assert_type(polyCone(nodes[1], edit=True, radius=2.0), Literal["Values edited."])
    assert_type(
        polyCone(nodes[0], e=True, rcp=True, tx=False), Literal["Values edited."]
    )
    assert_type(polyCone(nodes[1], q=True, radius=True), Any)
    assert_type(
        polyCone(axis=(0.0, 1.0, 0.0), sx=10, sy=3, sz=2, roundCap=True),
        tuple[Transform, PolyCone],
    )


def check_poly_pyramid_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyPyramid()
    assert_type(nodes, tuple[Transform, PolyPyramid])
    assert_type(polyPyramid(ch=False), tuple[Transform])
    assert_type(polyPyramid(constructionHistory=False), tuple[Transform])
    assert_type(polyPyramid(object=False), tuple[PolyPyramid])
    assert_type(polyPyramid(o=False, ch=False), tuple[PolyPyramid])
    assert_type(
        polyPyramid(constructionHistory=history, object=create_object),
        tuple[Transform, PolyPyramid] | tuple[Transform] | tuple[PolyPyramid],
    )
    assert_type(polyPyramid(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyPyramid(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyPyramid(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyPyramid(nodes[0], q=True, nds=True), NodeState)
    assert_type(
        polyPyramid(nodes[1], edit=True, sideLength=2.0), Literal["Values edited."]
    )
    assert_type(polyPyramid(nodes[0], e=True, texture=False), Literal["Values edited."])
    assert_type(polyPyramid(nodes[1], q=True, sideLength=True), Any)
    assert_type(
        polyPyramid(axis=(0.0, 1.0, 0.0), ns=5, nsi=5, sc=2, sh=3, tx=False),
        tuple[Transform, PolyPyramid],
    )


def check_poly_cube_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polyCube()
    assert_type(nodes, tuple[Transform, PolyCube])
    assert_type(polyCube(ch=False), tuple[Transform])
    assert_type(polyCube(constructionHistory=False), tuple[Transform])
    assert_type(polyCube(object=False), tuple[PolyCube])
    assert_type(polyCube(o=False, ch=False), tuple[PolyCube])
    assert_type(
        polyCube(constructionHistory=history, object=create_object),
        tuple[Transform, PolyCube] | tuple[Transform] | tuple[PolyCube],
    )
    assert_type(polyCube(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyCube(nodes[0], query=True, nds=True), NodeState)
    assert_type(polyCube(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polyCube(nodes[0], q=True, nds=True), NodeState)
    assert_type(polyCube(nodes[1], edit=True, width=2.0), Literal["Values edited."])
    assert_type(polyCube(nodes[0], e=True, d=3.0), Literal["Values edited."])
    assert_type(polyCube(nodes[1], q=True, width=True), Any)
    assert_type(polyCube(nodes[1], query=True, axis=True), Any)
    assert_type(
        polyCube(axis=(0.0, 1.0, 0.0), sx=10, sy=15, sz=5),
        tuple[Transform, PolyCube],
    )


def check_poly_sphere_types(history: bool, create_object: bool) -> None:
    nodes = cmds.polySphere()
    assert_type(nodes, tuple[Transform, PolySphere])
    assert_type(polySphere(ch=False), tuple[Transform])
    assert_type(polySphere(constructionHistory=False), tuple[Transform])
    assert_type(polySphere(object=False), tuple[PolySphere])
    assert_type(polySphere(o=False, ch=False), tuple[PolySphere])
    assert_type(
        polySphere(constructionHistory=history, object=create_object),
        tuple[Transform, PolySphere] | tuple[Transform] | tuple[PolySphere],
    )
    assert_type(polySphere(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polySphere(nodes[0], query=True, nds=True), NodeState)
    assert_type(polySphere(nodes[1], q=True, nodeState=True), NodeState)
    assert_type(polySphere(nodes[0], q=True, nds=True), NodeState)
    assert_type(polySphere(nodes[1], edit=True, radius=2.0), Literal["Values edited."])
    assert_type(
        polySphere(nodes[0], e=True, nds=NodeState.BLOCKING),
        Literal["Values edited."],
    )
    assert_type(polySphere(nodes[1], q=True, radius=True), Any)
    assert_type(polySphere(nodes[1], query=True, axis=True), Any)
    assert_type(
        polySphere(axis=(0.0, 1.0, 0.0), sx=10, sy=15), tuple[Transform, PolySphere]
    )


def check_ls_types(node: Node, nodes: list[Transform], mode: bool) -> None:
    assert_type(ls(), list[Node | str])
    assert_type(cmds.ls(node), list[Node | str])
    assert_type(ls([node, "pPlane*"]), list[Node | str])
    assert_type(ls(nodes), list[Node | str])
    assert_type(ls((node, "pPlane*"), type=["mesh", "transform"]), list[Node | str])
    assert_type(ls(typ=("mesh", "transform"), assemblies=True), list[Node | str])
    assert_type(ls(uuid=True), list[str])
    assert_type(ls(uid=True), list[str])
    assert_type(ls(nodeTypes=True), list[str])
    assert_type(ls(nt=True), list[str])
    assert_type(ls(objectsOnly=True), list[Node])
    assert_type(ls(o=True, selection=True), list[Node])
    assert_type(ls(o=True, uid=True), list[str])
    assert_type(ls(o=True, showType=True), list[Node | str])
    assert_type(ls(o=True, ufeObjects=True), list[Node | str])
    assert_type(ls(showNamespace=True), list[Node | str])
    assert_type(ls(uuid=mode), list[Node | str])
    assert_type(cmds.ls(type=Transform), list[Node | str])
    assert_type(ls(typ=[Transform, "joint"]), list[Node | str])
    assert_type(ls(exactType=Joint), list[Node | str])
    assert_type(ls(et=(Joint, Transform)), list[Node | str])
    assert_type(ls(excludeType=Transform), list[Node | str])
    assert_type(ls(ext=[Joint], objectsOnly=True), list[Node])


def check_create_node_types(node_type: str, shared: bool) -> None:
    transform = createNode(Transform)
    assert_type(transform, Transform)
    assert_type(createNode("joint"), Node | None)
    assert_type(createNode(Joint, shared=False), Joint)
    assert_type(createNode(Joint, s=False), Joint)
    assert_type(createNode(Joint, shared=True), Joint | None)
    assert_type(createNode(Joint, s=True), Joint | None)
    assert_type(createNode(Joint, shared=shared), Joint | None)
    assert_type(createNode(Joint, s=shared), Joint | None)
    assert_type(createNode(Joint, shared=False, s=True), Joint | None)
    assert_type(createNode(node_type), Node | None)
    assert_type(createNode(node_type, shared=shared), Node | None)
    assert_type(createNode(Joint, parent=transform, skipSelect=True), Joint)
    assert_type(createNode(Joint, p=transform, n="child", ss=True), Joint)
    assert_type(createNode(Joint), Joint)
    assert_type(createNode(CustomJoint), CustomJoint)
    assert_type(createNode(node_type=Joint, shared=shared), Joint | None)
    if transform is not None:
        assert_type(transform.rename("renamed"), str)
        node: Node = transform
        assert_type(node, Node)


def check_generic_node_is_rejected() -> None:
    createNode(Node)  # type: ignore[type-var]


def check_poly_plane_types(history: bool, create_object: bool) -> None:
    nodes = polyPlane()
    assert_type(nodes, tuple[Transform, PolyPlane])
    assert_type(nodes[0], Transform)
    assert_type(nodes[1], PolyPlane)
    assert_type(polyPlane(nodes[1], query=True, nodeState=True), NodeState)
    assert_type(polyPlane(nodes[0], q=True, nds=True), NodeState)
    assert_type(
        polyPlane(nodes[1], edit=True, nodeState=NodeState.BLOCKING),
        Literal["Values edited."],
    )
    assert_type(polyPlane(nodes[0], e=True, width=2.0), Literal["Values edited."])
    assert_type(polyPlane(constructionHistory=False), tuple[Transform])
    assert_type(polyPlane(ch=False), tuple[Transform])
    assert_type(polyPlane(object=False), tuple[PolyPlane])
    assert_type(polyPlane(o=False, ch=False), tuple[PolyPlane])
    assert_type(
        polyPlane(constructionHistory=history, object=create_object),
        tuple[Transform, PolyPlane] | tuple[Transform] | tuple[PolyPlane],
    )
    assert_type(polyPlane(query=True, width=True), Any)
    assert_type(polyPlane("pPlane1", query=True, axis=True), Any)
    assert_type(polyPlane("pPlane1", q=True, ax=True), Any)
    assert_type(polyPlane(axis=(0.0, 1.0, 0.0)), tuple[Transform, PolyPlane])
    assert_type(
        polyPlane("pPlane1", edit=True, axis=(0.0, 0.0, 1.0)),
        Literal["Values edited."],
    )
    query: bool = True
    assert_type(polyPlane(q=query, w=True), Any)
    assert_type(polyPlane(nodeState=NodeState.NORMAL), tuple[Transform, PolyPlane])
    assert_type(polyPlane(nds=NodeState.HAS_NO_EFFECT), tuple[Transform, PolyPlane])
    assert_type(polyPlane("polyPlane1", query=True, nodeState=True), NodeState)
    assert_type(polyPlane("polyPlane1", query=True, nds=True), NodeState)
    assert_type(polyPlane("polyPlane1", q=True, nodeState=True), NodeState)
    assert_type(polyPlane("polyPlane1", q=True, nds=True), NodeState)
    assert_type(
        polyPlane("polyPlane1", e=True, nds=NodeState.BLOCKING),
        Literal["Values edited."],
    )
    assert_type(polyPlane(nodes[1], edit=True, query=query, width=True), Any)
