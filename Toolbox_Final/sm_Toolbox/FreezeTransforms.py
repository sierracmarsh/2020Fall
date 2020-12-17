import maya.cmds as cmds
class FreezeTransforms():
   def __init__(self):
        self.WindowUI = 'UIWindow'

   def create(self):
        self.delete()

   def delete(self):
        if cmds.window(self.WindowUI, exists=True):
            cmds.deleteUI(self.WindowUI)

        self.WindowUI = cmds.window(self.WindowUI, title='Select Obj and Freeze', widthHeight=(300, 300))
        self.column = cmds.columnLayout(parent=self.WindowUI, adjustableColumn=True)
        cmds.button(parent=self.column, label='Apply', command=lambda *x: self.freezeTransforms())
       
        cmds.setParent('..')

        cmds.showWindow(self.WindowUI)
    
   def freezeTransforms(self,*_):
        sels = cmds.ls(sl=True)
        if sels >= 1:
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=2)


WindowUI = FreezeTransforms()
WindowUI.create()



