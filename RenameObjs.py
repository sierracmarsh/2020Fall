import maya.cmds as cmds
#requires an argument string in the format "Name_##_NodeType"
# look for the "#" characters and replace them with the next number in a sequence.
#objs wouldnt stay as ## so I used xx
#


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

#redo for tuple