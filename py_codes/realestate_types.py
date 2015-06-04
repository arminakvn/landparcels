import sys
import string
import os
import arcpy
import arcpy.da
from parcels import dclass_parcels as _parcel
from lookup_csv_to_dict import read_luc_csv_to_dict, read_realestatetypes_csv_to_dict
################################## Parcels #######################################
# this tool works on the result of the Append To Mosaic Tool and will populate the
# fields from the dissolve model result

# setting the workspace
try:
    os.chdir(scriptPath)
except: 
    print "location setting didn't work"

parcels_mosaic_gdb = arcpy.GetParameterAsText(0) # the file geodatabase containing the regional parcel mosaic
inFC = arcpy.GetParameterAsText(1) # MAPC's Parcels mosaic
realestate_type_lookup_table = arcpy.GetParameterAsText(2) # "real_estate_type_lookup.csv"

# setting the workspace
arcpy.env.workspace = parcels_mosaic_gdb
# checking to see if the fields are there if not creating them
fieldName1_2 = "realest_typ"
fieldLength1_2 = "255"
fieldAlias1_2 = "Real Estate Type"

try:
	arcpy.AddField_management(inFC, fieldName1_2, "TEXT", "", "", fieldLength1_2, fieldAlias1_2, "NULLABLE", "NON_REQUIRED")
except:
	print arcpy.GetMessages() 

id_cntr= 0
ret_lookup = read_realestatetypes_csv_to_dict(realestate_type_lookup_table)
field_names = [str(f.name) for f in arcpy.ListFields(inFC)]
with arcpy.da.UpdateCursor(inFC, field_names) as cursor:
    for each_row in cursor:
        id_cntr += 1
        # using the class, first define an instance, set the neccessary attributes then run the method for the instance
        e_parcel = _parcel(id_cntr)
        setattr(e_parcel, 'mapc_id', each_row[field_names.index('mapc_id')])
        setattr(e_parcel, 'land_use_dtax_1', each_row[field_names.index('luc_adj_1')])
        setattr(e_parcel, 'far', each_row[field_names.index('far')])
        e_parcel.det_real_estate_type(ret_lookup)
        each_row[field_names.index('realest_typ')] = getattr(e_parcel, 'real_estate_type')
        cursor.updateRow(each_row)