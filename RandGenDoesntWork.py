import maya.cmds as cmds
import random

def RandomObj(Clones, minX, maxX, minY, maxY, minZ, maxZ):
    sel = cmds.ls(selection=True)

    for obj in range(len(cmds.ls(selection=True))):
        index = obj

        for obj in range(Clones):
            tempObj = (cmds.duplicate(sel[index], rr=True))
            randomX = random.uniform(minX, maxX)
            randomY = random.uniform(minY, maxY)
            randomZ = random.uniform(minZ, maxZ)

            cmds.select(tempObj)
            cmds.xform(worldSpace=True, translation=[randomX, randomY, randomZ])


RandomGenerator(10,0,10,0,10,0,10)