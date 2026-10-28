from typing import Any, Literal, assert_type

from maya_brew import cmds
from maya_brew.command_wrapper import (
    ambientLight,
    circle,
    cone,
    connectJoint,
    createNode,
    cylinder,
    directionalLight,
    ikHandle,
    ikHandleDisplayScale,
    ikSolver,
    ikSystemInfo,
    insertJoint,
    joint,
    jointDisplayScale,
    ls,
    mirrorJoint,
    nonLinear,
    nurbsCube,
    nurbsPlane,
    nurbsSquare,
    pointLight,
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
    spaceLocator,
    sphere,
    spotLight,
    torus,
)
from maya_brew.command_wrapper._generated.maya_2027.commands import (
    CreateJiggleDeformer,
    CreateWrap,
    blendShape,
    cluster,
    deformer,
    deltaMush,
    flexor,
    lattice,
    proximityWrap,
    sculpt,
    skinCluster,
    softMod,
    tension,
    textureDeformer,
    wire,
    wrinkle,
)
from maya_brew.command_wrapper.extensions.deformer import DeformerType
from maya_brew.command_wrapper.extensions.flexor import (
    FlexorDeformerCommand,
    FlexorType,
)
from maya_brew.command_wrapper.extensions.non_linear import NonLinearType
from maya_brew.command_wrapper.extensions.texture_deformer import (
    TextureDeformerDirection,
    TextureDeformerPointSpace,
    TextureDeformerVectorSpace,
)
from maya_brew.command_wrapper.extensions.wrinkle import WrinkleStyle
from maya_brew.nodes._foundation.node_extensions import Node
from maya_brew.nodes.node_state import NodeState
from maya_brew.nodes.node_types import (
    AmbientLight,
    BlendShape,
    Cluster,
    DagNode,
    DeltaMush,
    DirectionalLight,
    Ffd,
    FlexorShape,
    IkEffector,
    IkHandle,
    IkSolver,
    Joint,
    Light,
    MakeNurbCircle,
    MakeNurbCone,
    MakeNurbCube,
    MakeNurbCylinder,
    MakeNurbPlane,
    MakeNurbSphere,
    MakeNurbsSquare,
    MakeNurbTorus,
    NonLinear,
    PointLight,
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
    ProximityWrap,
    Sculpt,
    Shape,
    SkinCluster,
    SoftMod,
    SpotLight,
    Tension,
    TextureDeformer,
    Transform,
    Wire,
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


def check_light_and_locator_types(mode: bool) -> None:
    ambient = cmds.ambientLight(intensity=0.8, name="ambient_1")
    assert_type(ambient, AmbientLight)
    assert_type(ambientLight(ambient, q=True, intensity=True), Any)
    assert_type(ambientLight(str(ambient), query=mode, intensity=True), Any)
    assert_type(ambientLight([ambient], e=True, intensity=0.4), Any)

    directional = directionalLight(i=0.7)
    assert_type(directional, DirectionalLight)
    assert_type(directionalLight(directional, q=True, intensity=True), Any)

    point = pointLight(i=0.6)
    assert_type(point, PointLight)
    assert_type(pointLight(point, e=True, intensity=0.3), Any)

    spot = spotLight(ca=35.0)
    assert_type(spot, SpotLight)
    assert_type(spotLight(spot, q=True, coneAngle=True), Any)

    locator = spaceLocator(name="locator_1")
    assert_type(locator, Transform)
    assert_type(spaceLocator(locator, q=True, position=True), Any)
    assert_type(spaceLocator((locator,), e=True, p=(1.0, 2.0, 3.0)), Any)


def check_deformer_types(mode: bool) -> None:
    assert_type(CreateJiggleDeformer(), None)
    assert_type(CreateWrap(), None)

    assert_type(blendShape("source", "target", envelope=0.8), BlendShape)
    assert_type(blendShape("blendShape1", q=True, envelope=True), Any)
    assert_type(blendShape("blendShape1", query=mode, en=True), Any)
    assert_type(blendShape("blendShape1", e=True, envelope=0.25), Any)

    assert_type(cluster("target", envelope=0.6), Cluster)
    assert_type(cluster("cluster1", q=True, envelope=True), Any)
    assert_type(cluster("cluster1", query=mode, en=True), Any)
    assert_type(cluster("cluster1", e=True, envelope=0.3), Any)

    assert_type(deformer("target", type=DeformerType.CLUSTER), Node)
    assert_type(deformer("deformer1", q=True, geometry=True), Any)
    assert_type(deformer("deformer1", query=mode, g=True), Any)
    assert_type(deformer("deformer1", e=True, geometry="pSphereShape1"), Any)

    assert_type(skinCluster("joint1", "target", skinMethod=0), SkinCluster)
    assert_type(skinCluster("skinCluster1", q=True, skinMethod=True), Any)
    assert_type(skinCluster("skinCluster1", query=mode, sm=True), Any)
    assert_type(skinCluster("skinCluster1", e=True, normalizeWeights=1), Any)

    assert_type(deltaMush("target", envelope=1.0), DeltaMush)
    assert_type(deltaMush("deltaMush1", q=True, envelope=True), Any)
    assert_type(deltaMush("deltaMush1", query=mode, en=True), Any)
    assert_type(deltaMush("deltaMush1", e=True, envelope=0.4), Any)

    assert_type(lattice("target", divisions=[2, 3, 4]), Ffd)
    assert_type(lattice("ffd1", q=True, divisions=True), Any)
    assert_type(lattice("ffd1", e=True, divisions=[2, 2, 2]), Any)

    assert_type(
        flexor(type=FlexorType.SCULPT, deformerCommand=FlexorDeformerCommand.SCULPT),
        FlexorShape,
    )
    assert_type(flexor(q=True, l=True), Any)
    assert_type(flexor(query=mode, type=True), Any)
    assert_type(flexor(e=True, type=FlexorType.SCULPT), Any)

    assert_type(nonLinear("target", type="bend"), NonLinear)
    assert_type(nonLinear("target", typ=NonLinearType.FLARE), NonLinear)
    assert_type(nonLinear("target", type=NonLinearType.SINE), NonLinear)
    assert_type(nonLinear("target", typ="squash"), NonLinear)
    assert_type(nonLinear("nonLinear1", q=True, geometry=True), Any)
    assert_type(nonLinear("nonLinear1", query=mode, g=True), Any)
    assert_type(nonLinear("nonLinear1", e=True, geometry="pSphereShape1"), Any)

    assert_type(proximityWrap("driver", "target"), ProximityWrap)
    assert_type(proximityWrap("proximityWrap1", q=True, freeDriverIndex=True), Any)
    assert_type(proximityWrap("proximityWrap1", e=True, addDrivers="driver2"), Any)

    assert_type(sculpt("target", mode=["flip"]), Sculpt)
    assert_type(sculpt("sculpt1", q=True, mode=True), Any)
    assert_type(sculpt("sculpt1", q=True, insideMode=True), Any)
    assert_type(sculpt("sculpt1", e=True, mode=["stretch"]), Any)

    assert_type(softMod("target", envelope=0.6), SoftMod)
    assert_type(softMod("softMod1", q=True, envelope=True), Any)
    assert_type(softMod("softMod1", query=mode, en=True), Any)
    assert_type(softMod("softMod1", e=True, envelope=0.2), Any)

    assert_type(tension("target", envelope=0.6), Tension)
    assert_type(tension("tension1", q=True, envelope=True), Any)
    assert_type(tension("tension1", query=mode, en=True), Any)
    assert_type(tension("tension1", e=True, envelope=0.2), Any)

    assert_type(textureDeformer("target", strength=0.8), TextureDeformer)
    assert_type(
        textureDeformer(
            "target",
            direction=TextureDeformerDirection.VECTOR,
            pointSpace=TextureDeformerPointSpace.UV,
            vectorSpace=TextureDeformerVectorSpace.TANGENT,
        ),
        TextureDeformer,
    )
    assert_type(textureDeformer("textureDeformer1", q=True, strength=True), Any)
    assert_type(textureDeformer("textureDeformer1", query=mode, s=True), Any)
    assert_type(textureDeformer("textureDeformer1", e=True, strength=0.5), Any)

    assert_type(wire("target", envelope=1.0), Wire)
    assert_type(wire("wire1", q=True, envelope=True), Any)
    assert_type(wire("wire1", query=mode, en=True), Any)
    assert_type(wire("wire1", e=True, envelope=0.5), Any)

    assert_type(wrinkle("target"), tuple[Node, ...])
    assert_type(wrinkle("target", style=WrinkleStyle.RADIAL), tuple[Node, ...])


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
    transforms = cmds.ls(type=Transform)
    assert_type(transforms, list[Transform])
    assert_type(ls(typ=[Transform, "joint"]), list[Node | str])
    assert_type(ls(exactType=Joint), list[Joint])
    assert_type(ls(et=(Joint, Transform)), list[Joint | Transform])
    assert_type(ls(excludeType=Transform), list[Node | str])
    assert_type(ls(ext=[Joint], objectsOnly=True), list[Node])


def check_ls_class_filter_types(mode: bool, node_type: type[Transform]) -> None:
    assert_type(cmds.ls(type=Transform, long=True), list[Transform])
    assert_type(ls(typ=Transform, selection=True), list[Transform])
    assert_type(ls(exactType=Joint), list[Joint])
    assert_type(ls(et=Joint), list[Joint])
    assert_type(ls(type=DagNode), list[DagNode])
    assert_type(ls(type=node_type), list[Transform])
    assert_type(ls(type=CustomJoint), list[CustomJoint])
    assert_type(ls(type=CustomJoint, o=True), list[CustomJoint])
    assert_type(ls(type=Transform, objectsOnly=True), list[Transform])
    assert_type(ls(typ=Transform, o=True), list[Transform])
    assert_type(ls(exactType=Joint, objectsOnly=True), list[Joint])
    assert_type(ls(et=Joint, o=True), list[Joint])
    assert_type(ls(type=Transform, o=True, st=False, uid=False), list[Transform])
    assert_type(ls(type=Transform, o=mode), list[Transform])
    assert_type(ls(type=Transform, objectsOnly=False), list[Transform])
    assert_type(ls("cube.translateX", type=Transform), list[Transform])
    assert_type(ls(type=Transform, sl=mode, ocs=mode), list[Transform])
    assert_type(ls(type=Transform, uuid=False, showType=False), list[Transform])
    assert_type(ls(type=Transform, sns=False, ufe=False), list[Transform])
    assert_type(ls(type=Transform, showType=True), list[Transform | str])
    assert_type(ls(typ=Transform, st=mode, o=True), list[Transform | str])
    assert_type(ls(type=Joint, showNamespace=True), list[Joint | str])
    assert_type(ls(et=Joint, sns=mode, o=True), list[Joint | str])
    assert_type(ls(type=Transform, ufeObjects=True), list[Transform | str])
    assert_type(ls(type=Transform, ufe=mode, objectsOnly=True), list[Transform | str])
    assert_type(ls(type=Transform, uuid=True), list[str])
    assert_type(ls(typ=Transform, uid=True, o=True), list[str])
    assert_type(ls(exactType=Joint, nodeTypes=True), list[str])
    assert_type(ls(et=Joint, nt=True), list[str])
    assert_type(ls(type=Transform, uuid=mode), list[Transform | str])
    assert_type(ls(type=Transform, shapes=True), list[Node | str])
    assert_type(ls(type=Transform, s=mode, o=True), list[Node])
    assert_type(ls(type=Transform, shapes=False), list[Transform])
    assert_type(ls(type=Transform, dag=True), list[Node | str])
    assert_type(ls(type=Transform, dep=True, o=True), list[Node])
    assert_type(ls(type=Transform, containerType="custom"), list[Node | str])
    assert_type(ls(type="transform", o=True), list[Node])
    assert_type(ls(type=[Transform]), list[Node | str])
    assert_type(ls(type=[]), list[Node | str])
    assert_type(ls(type=[], objectsOnly=True), list[Node])
    ls(type=42)  # type: ignore[call-overload]
    # Intentionally invalid flag to verify static typing catches unknown kwargs.
    # pylint: disable-next=unexpected-keyword-arg
    ls(type=Transform, missingFlag=True)  # type: ignore[call-overload]


def check_ls_tuple_filter_types(
    mode: bool,
    node_types: tuple[type[Shape], type[Transform]],
    nonempty: tuple[type[Transform], *tuple[type[Transform], ...]],
    possibly_empty: tuple[type[Transform], ...],
    node_list: list[type[Transform]],
) -> None:
    nodes = cmds.ls(type=(Shape, Transform))
    assert_type(nodes, list[Shape | Transform])
    assert_type(ls(typ=(Shape, Transform), long=True), list[Shape | Transform])
    assert_type(ls(exactType=(Shape, Transform)), list[Shape | Transform])
    assert_type(ls(et=(Shape, Transform)), list[Shape | Transform])
    assert_type(ls(type=node_types), list[Shape | Transform])
    assert_type(ls(type=(Transform,)), list[Transform])
    assert_type(ls(typ=(CustomJoint,), o=True), list[CustomJoint])
    assert_type(ls(type=(Shape, CustomJoint)), list[Shape | CustomJoint])
    assert_type(
        ls(type=(Shape, Transform, CustomJoint)), list[Shape | Transform | CustomJoint]
    )
    assert_type(ls(type=nonempty), list[Transform])
    assert_type(ls(type=(Shape, Transform), objectsOnly=True), list[Shape | Transform])
    assert_type(ls(type=(Shape, Transform), o=mode), list[Shape | Transform])
    assert_type(ls(type=(Shape, Transform), shapes=False), list[Shape | Transform])
    assert_type(ls(type=(Shape, Transform), uuid=True), list[str])
    assert_type(ls(typ=(Shape, Transform), uid=True), list[str])
    assert_type(ls(exactType=(Shape, Transform), nodeTypes=True), list[str])
    assert_type(ls(et=(Shape, Transform), nt=True), list[str])
    assert_type(
        ls(type=(Shape, Transform), showType=True), list[Shape | Transform | str]
    )
    assert_type(ls(typ=(Shape, Transform), st=mode), list[Shape | Transform | str])
    assert_type(ls(type=(Shape, Transform), sns=True), list[Shape | Transform | str])
    assert_type(ls(et=(Shape, Transform), ufe=mode), list[Shape | Transform | str])
    assert_type(ls(type=(Shape, Transform), uuid=mode), list[Shape | Transform | str])
    assert_type(ls(type=(Shape, Transform), shapes=True), list[Node | str])
    assert_type(ls(type=(Shape, Transform), s=mode, o=True), list[Node])
    assert_type(ls(type=(Shape, Transform), containerType="custom"), list[Node | str])
    assert_type(ls(type=(Transform, "mesh")), list[Node | str])
    assert_type(ls(excludeType=(Shape, Transform)), list[Node | str])
    assert_type(ls(type=[Shape, Transform]), list[Node | str])
    assert_type(ls(type=node_list), list[Node | str])
    assert_type(ls(type=possibly_empty), list[Node | str])
    assert_type(ls(type=()), list[Node | str])
    assert_type(ls(type=(), o=True), list[Node])


def check_ls_multi_class_tuple_types(mode: bool) -> None:
    nodes = cmds.ls(type=(Shape, Transform, Light))
    assert_type(nodes, list[Shape | Transform | Light])
    node_types = (Shape, Transform, BlendShape)
    assert_type(ls(type=node_types), list[Shape | Transform | BlendShape])
    assert_type(ls(typ=node_types), list[Shape | Transform | BlendShape])
    assert_type(ls(exactType=node_types), list[Shape | Transform | BlendShape])
    assert_type(ls(et=node_types), list[Shape | Transform | BlendShape])
    assert_type(ls(type=node_types, o=True), list[Shape | Transform | BlendShape])
    assert_type(
        ls(type=node_types, showType=True), list[Shape | Transform | BlendShape | str]
    )
    assert_type(
        ls(type=node_types, uuid=mode), list[Shape | Transform | BlendShape | str]
    )
    assert_type(ls(type=node_types, uuid=True), list[str])
    assert_type(ls(type=node_types, shapes=True), list[Node | str])
    assert_type(ls(type=node_types, shapes=True, o=True), list[Node])


def check_ls_tuple_precision_boundary() -> None:
    sixteen_types = (
        BlendShape,
        DeltaMush,
        Ffd,
        IkSolver,
        MakeNurbCircle,
        MakeNurbCone,
        MakeNurbCube,
        MakeNurbCylinder,
        MakeNurbPlane,
        MakeNurbSphere,
        MakeNurbsSquare,
        MakeNurbTorus,
        PolyCube,
        PolySphere,
        Shape,
        Transform,
    )
    assert_type(
        ls(type=sixteen_types),
        list[
            BlendShape
            | DeltaMush
            | Ffd
            | IkSolver
            | MakeNurbCircle
            | MakeNurbCone
            | MakeNurbCube
            | MakeNurbCylinder
            | MakeNurbPlane
            | MakeNurbSphere
            | MakeNurbsSquare
            | MakeNurbTorus
            | PolyCube
            | PolySphere
            | Shape
            | Transform
        ],
    )
    seventeen_types = (*sixteen_types, CustomJoint)
    assert_type(ls(type=seventeen_types), list[Node])
    assert_type(ls(type=seventeen_types, showType=True), list[Node | str])
    assert_type(ls(type=seventeen_types, uuid=True), list[str])


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
