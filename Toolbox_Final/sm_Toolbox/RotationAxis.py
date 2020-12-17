import maya.cmds as cmds

class RotationAxis():
    def __init__(self):
        self.WindowUI = 'UIWindow'

    def create(self):
        self.delete()
    def delete(self):
        if cmds.window(self.WindowUI, exists=True):
            cmds.deleteUI(self.WindowUI)

            
        self.parent_window = cmds.window(self.WindowUI, title = "View Rotation Axis", widthHeight = (300, 300))
        self.column = cmds.columnLayout(parent=self.WindowUI, adjustableColumn=True)
        cmds.button(parent=self.column, label='Switch Axis View On', command=lambda *x: self.AxisOn())
        cmds.showWindow(self.WindowUI)
        
   
    def AxisOn(self, *_):
            sels = cmds.ls(sl=True)
            selsNum = len(sels)
            for i in range(selsNum):
                cmds.toggle(sels[i], localAxis=True)
                cmds.setAttr(sels[i]+".displayLocalAxis", k=True)
                cmds.setAttr(sels[i] + ".jointOrientX", k=True)
                cmds.setAttr(sels[i] + ".jointOrientY", k=True)
                cmds.setAttr(sels[i] + ".jointOrientZ", k=True)

            
WindowUI = RotationAxis()
WindowUI.create()

