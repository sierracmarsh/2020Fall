import maya.cmds as cmds
from random 


def RandomGenerator(numCopies, minX, maxX, minY, maxY, minZ, maxZ):
    sel = cmds.ls(selection=True)


    numCopies = cmds.ls(sl = True)
        index = obj

        for obj in range(numCopies):
            randomX = random.uniform(minX, maxX)
            randomY = random.uniform(minY, maxY)
            randomZ = random.uniform(minZ, maxZ)

            cmds.select(obj)
            cmds.xform(worldSpace=True, translation=[randomX, randomY, randomZ])


RandomGenerator(3, 0, 5, 0, 5, 0, 5)
