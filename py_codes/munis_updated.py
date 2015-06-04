import sys
import string
import os
import arcpy
import arcpy.da
parcels_mosaic_gdb = arcpy.GetParameterAsText(0)
inFC = arcpy.GetParameterAsText(1)
inFC_old = arcpy.GetParameterAsText(2)
munis_set = set()
field_names = [str(f.name) for f in arcpy.ListFields(inFC)]
with arcpy.da.SearchCursor(inFC, field_names) as cursor:
  for row in cursor:
  	munis_set.add(row[field_names.index('muni_id')])

with arcpy.da.UpdateCursor(inFC_old, ["muni_id"]) as cursor:
    # Delete all rows that have a roads type of 4
    #
    for row in cursor:
        if row[0] in munis_set:
            cursor.deleteRow()

arcpy.Append_management([inFC_old], inFC, "NO_TEST","","")
def stringNullChecker(value):
  if value == None:
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