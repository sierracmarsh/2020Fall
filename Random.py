import maya.cmds as cmds
import random

def Random(numDup, minX, maxX, minY, maxY, minZ, maxZ):
    sel = cmds.ls(selection=True)
    for obj in range(len(cmds.ls(selection=True))):
        index = obj

        for obj in range(numDup):
            tempObj = (cmds.duplicate(sel[index], rr=True))
            randomX = random.uniform(minX, maxX)
            randomY = random.uniform(minY, maxY)
            randomZ = random.uniform(minZ, maxZ)

            cmds.select(tempObj)
            cmds.xform(worldSpace=True, translation=[randomX, randomY, randomZ])


Random(10,1,5,1,5,1,5)
#https://stackoverflow.com/questions/30341645/how-to-set-random-locations-to-poly-objects-in-maya-with-python

