import maya.cmds as cmds

def RenameObj(name_string):

    char_count = name_string.count('x')
    part_count = name_string.partition('x'*char_count)

    if item_count[1]:
        select = cmds.ls(selection=True)
        next_numb = 0
        for sel in select:
            next_numb += 1
            string_next = str(next_numb)
            tempname = string_next.zfill(char_count)
            cmds.rename(sel, part_count[0] + tempname + part_count[2])
        else:
            cmds.error('Not valid. Please correct naming convention')

            RenameObj("Leg_xx_Obj")

