import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection=True)
    selection_count = 1
    
    for obj in sel:
        selection_input = stringName.count("#")
        lsName = stringName.partition("#" * selection_input)
        sequential_numbering = str(selection_count)
        
        if lsName[1]:
            sequential_numbering = sequential_numbering.zfill(3)
            cmds.rename(lsName[0] + sequential_numbering + lsName[2])
            
        selection_count += 1            
            
Renamer("Leg_##_Jnt")