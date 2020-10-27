import maya.cmds as cmds

if not cmds.commandPort(':4434', query=True):
    cmds.commandPort(name=':4434')

cmds.polySphere(name="Bug", radius=1, subdivisionsAxis=10, subdivisionsHeight=10)
cmds.select("Bug")
cmds.scale(1, 1, 1)
cmds.move(4,1,0)
cmds.duplicate("Bug")
cmds.scale(2, 2, 2)
cmds.move(5,1,0)
cmds.duplicate("Bug1")
cmds.scale(3, 3, 3)
cmds.move(9,2,0)
cmds.duplicate("Bug2")
cmds.scale(4, 4, 4)
cmds.move(15,3,0)
cmds.duplicate("Bug3")
cmds.scale(5, 5, 5)
cmds.move(23,4,0)
cmds.duplicate("Bug4")
cmds.scale(6,7,5)
cmds.move(32,3,0)
cmds.select("Bug5.f[55]", "Bug5.f[51]")
cmds.polyExtrudeFacet('Bug5.f[56]', 'Bug5.f[51]', kft=True, ltz=2, ls=(.5, .5, 10))
cmds.select("Bug4")
cmds.duplicate("Bug4")
cmds.scale(.5,.5,.5)
cmds.move(36.5,3,3)
cmds.duplicate("Bug6")
cmds.move(36.5,3,-3)



