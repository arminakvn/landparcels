import sys
import string
import os
import arcpy
import arcpy.da
from parcels import dclass_parcels as _parcel
################################## Parcels #######################################
# setting the workspace
try:
    os.chdir(scriptPath)
except: 
    print "location setting didn't work"

parcels_mosaic_gdb = arcpy.GetParameterAsText(0) # the file geodatabase containing the regional parcel mosaic
inFC = arcpy.GetParameterAsText(1) # MAPC's Parcels mosaic featureclass

# setting the workspace
arcpy.env.workspace = parcels_mosaic_gdb
# checking to see if the fields are there if not creating them
fieldName1_2 = "resid_type"
fieldLength1_2 = "255"
fieldAlias1_2 = "Residential Type"

try:
	arcpy.AddField_management(inFC, fieldName1_2, "TEXT", "", "", fieldLength1_2, fieldAlias1_2, "NULLABLE", "NON_REQUIRED")
except:
	print arcpy.GetMessages() 

id_cntr= 0
field_names = [str(f.name) for f in arcpy.ListFields(inFC)]
with arcpy.da.UpdateCursor(inFC, field_names) as cursor:
    for each_row in cursor:
        id_cntr += 1
        e_parcel = _parcel(id_cntr)
        setattr(e_parcel, 'land_use_dtax_1', each_row[field_names.index('luc_adj_1')])
        e_parcel.det_res_type()
        each_row[field_names.index('resid_type')] = getattr(e_parcel, 'residential_type')
        cursor.updateRow(each_row)