import maya.cmds as cmds

class RandomTool():
    def __init__(self):
        self.WindowUI = 'UIWindow'

    def create(self):
        self.delete()

    def delete(self):
        if cmds.window(self.WindowUI, exists=True):
            cmds.deleteUI(self.WindowUI)

        self.WindowUI = cmds.window(self.WindowUI, title='RandomTool', widthHeight=(150, 300))
        self.column = cmds.columnLayout(parent=self.WindowUI, adjustableColumn=True)
        cmds.button(parent=self.column, label='Apply', command=lambda *x: self.RandomPlacement())
        cmds.separator(parent=self.column, height=30)
        cmds.showWindow(self.WindowUI)
        cmds.text(label="Number of Duplicates", parent=self.column)
        self.numDups = cmds.intField(parent=self.column)
        cmds.text(label="MinX", parent=self.column)
        self.minX = cmds.intField(parent=self.column)
        cmds.text(label="MaxX", parent=self.column)
        self.maxX = cmds.intField(parent=self.column)
        cmds.text(label="MinY", parent=self.column)
        self.minY = cmds.intField(parent=self.column)
        cmds.text(label="MaxY", parent=self.column)
        self.maxY = cmds.intField(parent=self.column)
        cmds.text(label="MinZ", parent=self.column)
        self.minZ = cmds.intField(parent=self.column)
        cmds.text(label="MaxZ", parent=self.column)
        self.maxZ = cmds.intField(parent=self.column)

    def RandomPlacement(self):

        sel = cmds.ls(selection=True)
        Copies = cmds.intField(self.numDups, q=True, value=True)
        minX = cmds.intField(self.minX, q=True, value=True)
        maxX = cmds.intField(self.maxX, q=True, value=True)
        minY = cmds.intField(self.minY, q=True, value=True)
        maxY = cmds.intField(self.maxY, q=True, value=True)
        minZ = cmds.intField(self.maxZ, q=True, value=True)
        maxZ = cmds.intField(self.maxZ, q=True, value=True)

        for obj in range(len(cmds.ls(selection=True))):
            index = obj

            for obj in range(Copies):
                tempObj = (cmds.duplicate(sel[index], rr=True))
                RandX = random.uniform(minX, maxX)
                RandY = random.uniform(minY, maxY)
                RandZ = random.uniform(minZ, maxZ)

                cmds.select(tempObj)
                cmds.xform(worldSpace=True, translation=[RandX, RandY, RandZ])


WindowUI = RandomTool()
WindowUI.create()