import maya.cmds as cmds
import sm_Toolbox

class Window:
    def __init__(self):
        self.my_window = 'sm_ToolBox_UI'

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,title='MayaUI',widthHeight=(400, 400))
        self.column = cmds.columnLayout(parent=self.my_window,adjustableColumn=True)
        cmds.showWindow(self.my_window)

        cmds.button(parent=self.column,
                    label='Random Generator',
                    c=lambda *x: self.randUI())
        cmds.button(parent=self.column,
                    label='Rename Numbered Objects',
                    c=lambda *x: self.renamUI())
        cmds.button(parent=self.column,
                    label='Freeze Transformations',
                    c=lambda *x: self.freezeUI())
        cmds.button(parent=self.column,
                    label='Parent Group',
                    c=lambda *x: self.parentUI())
        cmds.button(parent=self.column,
                    label='Delete History',
                    c=lambda *x: self.deletUI())
        cmds.button(parent=self.column,
                    label='Constrain',
                    c=lambda *x: self.constrainUI())
        cmds.button(parent=self.column,
                    label='Axis Toggle',
                    c=lambda *x: self.AxisUI())

    def randUI(self):
        import randUI
        reload(RandomUI2)
        instance = RandomUI2.RandomTool()
        instance.create()

    def renamUI(self):
        import RenameObjs
        reload(RenameObjs)
        instance = RenameObjs.Renamer()
        instance.create()

    def freezeUI(self):
        import FreezeTransforms
        reload(FreezeTransforms)
       

    def parentUI(self):
        import ParentGroup
        reload(ParentGroup)

    def deletUI(self):
        import DeleteHistory
        reload(DeleteHistory)

    def ConstrainandParent(self):
        import ParentConstrain
        reload(ParentConstrain)

    def AxisUI(self):
        import RotationAxis
        reload(RotationAxis)
        instance = RotationAxisn.AxisOn()
        instance.create()


my_window = Window()
my_window.create()

