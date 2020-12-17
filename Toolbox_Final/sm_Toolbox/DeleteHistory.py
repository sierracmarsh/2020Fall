import maya.cmds as cmds
class DeleteHistory():
   def __init__(self):
        self.WindowUI = 'UIWindow'

   def create(self):
        self.delete()

   def delete(self):
        if cmds.window(self.WindowUI, exists=True):
            cmds.deleteUI(self.WindowUI)

        self.WindowUI = cmds.window(self.WindowUI, title='Delete History', widthHeight=(300, 300))
        self.column = cmds.columnLayout(parent=self.WindowUI, adjustableColumn=True)
        cmds.text(label="Select Obj and Delete", parent=self.column)
        cmds.button(parent=self.column,label='Delete',command=self.deletehistory)
       
        cmds.setParent('..')

        cmds.showWindow(self.WindowUI)
    
   def deletehistory(self,*_):
        sels = cmds.ls(sl=True)
        cmds.constructionHistory(query=True, toggle=True)
        cmds.delete(ch=True)


WindowUI = DeleteHistory()
WindowUI.create()

