import sys
import string
import os
import arcpy
import arcpy.da
parcels_mosaic_gdb = arcpy.GetParameterAsText(0)
inFC = arcpy.GetParameterAsText(1)
def stringNullChecker(value):
  if (value == None) or (value == " "):
    return ""
  else:
    return value
def numNullChecker(value):
  if value == None:
    return -0.9999
  else:
    return value
for f in arcpy.ListFields(inFC):
	if f.type == "String":
		with arcpy.da.UpdateCursor(inFC, f.name) as cursor:
  			for row in cursor:
  				row[0] = stringNullChecker(row[0])
  				cursor.updateRow(row)
  	elif f.type == "Double":
  			with arcpy.da.UpdateCursor(inFC, f.name) as cursor:
	  			for row in cursor:
	  				row[0] = numNullChecker(row[0])
	  				cursor.updateRow(row)