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
        each_row[field_names.index('mapc_id')] = id_cntr
        # using the class, first define an instance, set the neccessary attributes then run the method for the instance
        e_parcel = _parcel(id_cntr)
        setattr(e_parcel, 'mapc_id', each_row[field_names.index('mapc_id')])
        setattr(e_parcel, 'land_use_dtax_1', each_row[field_names.index('luc_adj_1')])
        setattr(e_parcel, 'far', each_row[field_names.index('far')])
        e_parcel.det_real_estate_type(ret_lookup)
        each_row[field_names.index('realest_typ')] = getattr(e_parcel, 'real_estate_type')
        cursor.updateRow(each_row)

drop_fields = ['MAP_PAR_ID', 'LOC_ID', 'POLY_TYPE', 'MAP_NO', 'SOURCE', 'PLAN_ID', 'LAST_EDIT', 'BND_CHK', 'NO_MATCH', 'TOWN_ID', 'FIRST_Assess_LOC_ID', 'COUNT_Assess_LOC_ID', 'SUM_Assess_BLDG_VAL', 'SUM_Assess_LAND_VAL', 'SUM_Assess_OTHER_VAL', 'SUM_Assess_TOTAL_VAL', 'SUM_Assess_LS_PRICE', 'MIN_Assess_USE_CODE', 'MAX_Assess_USE_CODE', 'MAX_Assess_YEAR_BUILT', 'SUM_Assess_BLD_AREA', 'SUM_Assess_UNITS', 'SUM_Assess_RES_AREA', 'SUM_Assess_NUM_ROOMS', 'FIRST_Assess_FY', 'MAX_Assess_LS_DATE', 'MAX_Assess_SITE_ADDR', 'MAX_Assess_ADDR_NUM', 'MAX_Assess_FULL_STR', 'MAX_Assess_ZIP', 'MAX_Assess_OWNER1', 'MAX_Assess_OWN_ADDR', 'FIRST_Assess_OWN_CITY', 'FIRST_Assess_OWN_STATE', 'FIRST_Assess_OWN_ZIP', 'MAX_Assess_ZONING', 'FIRST_Assess_STYLE', 'MAX_Assess_TOWN_ID', 'total_impervious_sqm_j', 'SUM_imp_bld_fc_areasqm', 'building_footp_sqm_j', 'SUM_imp_bld_fc_areasqm_1', 'SUM_imp_bld_fc_areasqm_12']

arcpy.DeleteField_management(inFC, drop_fields)