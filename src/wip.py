import maya_brew

from maya_brew.nodes.node_types import Transform, Shape

nodes = maya_brew.cmds.ls(type=(Transform, Shape))

cube = maya_brew.cmds.polyCube(name="my_cube")

maya_brew.cmds.CreateJiggleDeformer(cube)

print(maya_brew.cmds.ls())