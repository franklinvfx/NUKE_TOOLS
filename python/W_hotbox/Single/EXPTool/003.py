#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY MAGIC HOTBOX
#
# NAME: Show Value
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
	if i.knob('label').value() == '':
	    i.knob('label').setValue('[value mode] : [value red] ')
	else:
	    i.knob('label').setValue('')