import maya.cmds as cmds

class parentGroup():
    def __init__(self):
        self.WindowUI = 'UIWindow'

    def create(self):
        self.delete()

    def delete(self):
        if cmds.window(self.WindowUI, exists=True):
            cmds.deleteUI(self.WindowUI)

        self.WindowUI = cmds.window(self.WindowUI, title='Group and Match Obj', widthHeight=(300, 300))
        self.column = cmds.columnLayout(parent=self.WindowUI, adjustableColumn=True)
        self.name_field = cmds.textField(parent=self.column,placeholderText="New Group Name")
        cmds.button(parent=self.column,label='Select Objs to Group',command=self.newGroup)
        
        cmds.setParent('..')
        
        cmds.showWindow(self.WindowUI)
        
    def ApplytoGroup(self, newname):
        polySel = cmds.ls(sl=True)
        cmds.group(absolute=True, empty=True, name=newname, world=True)
        groupSel = cmds.ls(sl=True)
        cmds.select(polySel, add=True)
        cmds.MatchTransform(groupSel, polySel)
        cmds.select(groupSel, d=True)
        cmds.select(groupSel, add=True)
        cmds.Parent(polySel, groupSel)
    
    def newGroup(self, newname):
        newname = cmds.textField(self.name_field, query=True, text=True)
        self.ApplytoGroup(newname)
        
        
WindowUI = parentGroup()
WindowUI.create()