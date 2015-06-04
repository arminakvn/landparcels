################################## Parcels #######################################
# this tool works on the result of the Append To Mosaic Tool and will populate the
# fields from the dissolve model result
# Armin Akhavan 
# armin.akhavan@gmail.com
import sys
import string
import os
import arcpy
import arcpy.da
from formatter_functions import *
parcels_mosaic_gdb = arcpy.GetParameterAsText(0) # the file geodatabase containing the regional parcel mosaic
inFC = arcpy.GetParameterAsText(1) # MAPC's Parcels mosaic
inCurrParcelsGDB = arcpy.GetParameterAsText(2) # current version of the mapc's land parcels_mosaic_gdb
inCurrParcelsFC = os.path.join(inCurrParcelsGDB, "Parcels_L3E")
arcpy.env.workspace = parcels_mosaic_gdb
fieldName1_0 = "mapc_id"
fieldAlias1_0 = "MAPC Assigned ID"
fieldName1_1 = "muni_id"
fieldAlias1_1 = "Municipal ID"
fieldName1_2 = "muni"
fieldAlias1_2 = "Municipality"
fieldLength1_2 = 18
fieldName1_3 = "parloc_id"
fieldAlias1_3 = "MassGIS Parcel ID"
fieldLength1_3 = 16
fieldName1_4 = "poly_typ"
fieldAlias1_4 = "Type of Parcel"
fieldLength1_4 = 18
fieldName2_1 = "map_num"
fieldAlias2_1 = "Assessors Map Number"
fieldLength2_1 = 18
fieldName2_2 = "mappar_id"
fieldAlias2_2 = "Assessors Block-Lot Number"
fieldLength2_2 = 50
fieldName4 = "loc_id_cnt"
fieldAlias4 = "Count of Assessors Records"
fieldPrecision4 = 5
fieldName5 = "land_value"
fieldAlias5 = "Assessed Land Value"
fieldName6 = "bldg_value"
fieldAlias6 = "Assessed Building Value"
fieldName7 = "othr_value"
fieldAlias7 = "Assessed Other Value"
fieldName8 = "total_value"
fieldAlias8 = "Total Assessed Value"
fieldName9 = "ls_price"
fieldAlias9 = "Last Sale Price"
fieldName10 = "ls_date"
fieldAlias10 = "Last Sale Date"
fieldLength10 = 10
fieldName11 = "bldg_area"
fieldAlias11 = "Gross Building Area"
fieldName12 = "res_area"
fieldAlias12 = "Finished Building Area"
fieldName13 = "luc_1"
fieldLength13 = 5
fieldAlias13 = "Assessors Use Code (Min)"
fieldName14 = "luc_2"
fieldLength14 = 5
fieldAlias14 = "Assessors Use Code (Max)"
fieldName15_1 = "luc_adj_1"
fieldLength15_1 = 5
fieldAlias15_1 = "Standard Use Code (Min)"
fieldName15_2 = "luc_adj_2"
fieldLength15_2 = 5
fieldAlias15_2 = "Standard Use Code (Max)"
fieldName16_1 = "num_units"
fieldAlias16_1 = "Reported Units"
fieldName16_2 = "units_est"
fieldAlias16_2 = "Estimated Units"
fieldName16_3 = "units_src"
fieldAlias16_3 = "Estimated Units Source"
fieldLength16_3 = 8
fieldName17 = "num_rooms"
fieldAlias17 = "Reported Rooms"
fieldName20 = "yr_built"
fieldAlias20 = "Most Recent Year Built"
fieldName21 = "site_addr"
fieldAlias21 = "Address"
fieldLength21 = 80
fieldName22 = "addr_str"
fieldAlias22 = "Street"
fieldLength22 = 60
fieldName23 = "addr_num"
fieldAlias23 = "Street Number"
fieldLength23 = 12
fieldName24 = "addr_zip"
fieldAlias24 = "Zip Code"
fieldLength24 = 12
fieldName25 = "owner_name"
fieldAlias25 = "Owner Name"
fieldLength25 = 80
fieldName26 = "owner_addr"
fieldAlias26 = "Owner Address"
fieldLength26 = 80
fieldName27 = "owner_city"
fieldAlias27 = "Owner City"
fieldLength27 = 25
fieldName28 = "owner_stat"
fieldAlias28 = "Owner State"
fieldLength28 = 4
fieldName29 = "owner_zip"
fieldAlias29 = "Owner Zip Code"
fieldLength29 = 10
fieldName30 = "fy"
fieldAlias30 = "Fiscal Year"
fieldName31 = "lot_areaft"
fieldAlias31 = "Lot Area (square feet)"
fieldName32 = "far"
fieldAlias32 = "Floor Area Ratio"
fieldName33 = "pct_imperv"
fieldAlias33 = "Percent Impervious (Total)"
fieldName34 = "pct_bldg"
fieldAlias34 = "Percent Building Coverage"
fieldName35 = "pct_pave"
fieldAlias35 = "Percent Paevement Coverage"
fieldAlias34 = "Percent Building Coverage"
fieldName38 = "sqm_imperv"
fieldAlias38 = "Total  Impervious Area (sqm)"
fieldName39 = "sqm_bldg"
fieldAlias39 = "Building Coverage Area (sqm)"
fieldName40 = "sqm_pave"
fieldAlias40 = "Paved Coverage Area (sqm)"
fieldName41 = "bldlnd_rat"
fieldAlias41 = "Improvement to Land Value Ratio"
fieldName42 = "landv_pac"
fieldAlias42 = "Land Value per Acre"
fieldName43 = "Bldgv_psf"
fieldAlias43 = "Building Value per Sq Ft of Floor Area"
fieldName36 = "realest_typ"
fieldLength36 = "255"
fieldAlias36 = "Real Estate Type"
field_names_BFOR = [str(f.name) for f in arcpy.ListFields(inFC)]
try: 
  arcpy.AddField_management(inFC, fieldName42, "DOUBLE", "", "", "", fieldAlias42, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName43, "DOUBLE", "", "", "", fieldAlias43, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName38, "DOUBLE", "", "", "", fieldAlias38, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName39, "DOUBLE", "", "", "", fieldAlias39, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName40, "DOUBLE", "", "", "", fieldAlias40, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName41, "DOUBLE", "", "", "", fieldAlias41, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName1_0, "LONG", "", "", "", fieldAlias1_0, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName1_1, "SHORT", "", "", "", fieldAlias1_1, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName1_2, "TEXT", "", "", fieldLength1_2, fieldAlias1_2, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName1_3, "TEXT", "", "", fieldLength1_3, fieldAlias1_3, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName1_4, "TEXT", "", "", fieldLength1_4, fieldAlias1_4, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName2_1, "TEXT", "", "", fieldLength2_1, fieldAlias2_1, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName2_2, "TEXT", "", "", fieldLength2_2, fieldAlias2_2, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName4, "LONG", fieldPrecision4, "", "", fieldAlias4, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName5, "DOUBLE", "", "", "", fieldAlias5, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName6, "DOUBLE", "", "", "", fieldAlias6, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName7, "DOUBLE", "", "", "", fieldAlias7, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName8, "DOUBLE", "", "", "", fieldAlias8, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName9, "DOUBLE", "", "", "", fieldAlias9, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName10, "TEXT", "", "", fieldLength10, fieldAlias10, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName11, "DOUBLE", "", "", "", fieldAlias11, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName12, "DOUBLE", "", "", "", fieldAlias12, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName13, "TEXT", "", "",fieldLength13, fieldAlias13, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName14, "TEXT", "", "",fieldLength14, fieldAlias14, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName15_1, "TEXT", "", "",fieldLength15_1, fieldAlias15_1, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName15_2, "TEXT", "", "",fieldLength15_2, fieldAlias15_2, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName16_1, "DOUBLE", "", "", "", fieldAlias16_1, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName16_2, "DOUBLE", "", "", "", fieldAlias16_2, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName16_3, "TEXT", "", "", fieldLength16_3, fieldAlias16_3, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName17, "DOUBLE", "", "", "", fieldAlias17, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName20, "LONG", "", "", "", fieldAlias20, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName21, "TEXT", "", "", fieldLength21, fieldAlias21, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName22, "TEXT", "", "", fieldLength22, fieldAlias22, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName23, "TEXT", "", "", fieldLength23, fieldAlias23, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName24, "TEXT", "", "", fieldLength24, fieldAlias24, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName25, "TEXT", "", "", fieldLength25, fieldAlias25, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName26, "TEXT", "", "", fieldLength26, fieldAlias26, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName27, "TEXT", "", "", fieldLength27, fieldAlias27, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName28, "TEXT", "", "", fieldLength28, fieldAlias28, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName29, "TEXT", "", "", fieldLength29, fieldAlias29, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName30, "LONG", "", "", "", fieldAlias30, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName31, "DOUBLE", "", "", "", fieldAlias31, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName32, "DOUBLE", "", "", "", fieldAlias32, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName33, "DOUBLE", "", "", "", fieldAlias33, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName34, "DOUBLE", "", "", "", fieldAlias34, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName35, "DOUBLE", "", "", "", fieldAlias35, "NULLABLE", "NON_REQUIRED")
  arcpy.AddField_management(inFC, fieldName36, "TEXT", "", "", fieldLength36, fieldAlias36, "NULLABLE", "NON_REQUIRED")
except:
  print arcpy.GetMessages()
  pass
arcpy.CalculateField_management (inFC, "lot_areaft", "!Shape.Area@squarefeet!", "PYTHON")
field_names = [str(f.name) for f in arcpy.ListFields(inFC)]
cwdMuniTablePath = inCurrParcelsGDB
inTablePath = os.path.join(cwdMuniTablePath, "lkuptbl")
lookuptable = inTablePath
fields = ["TOWN_ID", "USE_CODE", "LUC_Assign"]
ludict = {}
with arcpy.da.SearchCursor(lookuptable, fields) as cursor:
  for row in cursor:
    ludict.update({(row[0], row[1]): row[2]})
inMuniTablepath = os.path.join(cwdMuniTablePath, "MuniKeys")
lookupMuni = inMuniTablepath
keyfields = ["MUNI", "MUNI_ID"]
muniDic = {}
with arcpy.da.SearchCursor(lookupMuni, keyfields) as cursor:
  for row in cursor:
    muniDic.update({row[1]: row[0]})
_not_to_drop_field_list = ['OBJECTID', 'SHAPE_Area', 'SHAPE_Length']
aftFldLEN = len(field_names)
mapc_ids = {row[0]: row[1] for row in arcpy.da.SearchCursor(inCurrParcelsFC, ("OID@", 'mapc_id'))}
max_mapc_ids = max(mapc_ids.values())
rec=max_mapc_ids
befFldLEN = len(field_names_BFOR) 
adddFldCnt = befFldLEN - aftFldLEN
with arcpy.da.UpdateCursor(inFC, field_names) as cursor:
  for row in cursor:
    # row[field_names.index('mapc_id')] = autoIncrement(rec)
    row[field_names.index('muni_id')] = muni_idCalctor(row[field_names.index('MAX_Assess_TOWN_ID')], row[field_names.index('TOWN_ID')], muniDic)
    row[field_names.index('muni')] = MuniLookup(str(row[field_names.index('muni_id')]), muniDic)
    row[field_names.index('parloc_id')] = row[field_names.index('LOC_ID')]
    row[field_names.index('poly_typ')] = row[field_names.index('POLY_TYPE')]
    row[field_names.index('map_num')] = row[field_names.index('MAP_NO')]
    row[field_names.index('mappar_id')] = row[field_names.index('MAP_PAR_ID')]
    row[field_names.index('loc_id_cnt')] = row[field_names.index('COUNT_Assess_LOC_ID')]
    row[field_names.index('land_value')] = row[field_names.index('SUM_Assess_LAND_VAL')]
    row[field_names.index('bldg_value')] = row[field_names.index('SUM_Assess_BLDG_VAL')]
    row[field_names.index('othr_value')] = row[field_names.index('SUM_Assess_OTHER_VAL')]
    row[field_names.index('total_value')] = row[field_names.index('SUM_Assess_TOTAL_VAL')]
    row[field_names.index('ls_price')] = row[field_names.index('SUM_Assess_LS_PRICE')]
    row[field_names.index('ls_date')] = row[field_names.index('MAX_Assess_LS_DATE')]
    row[field_names.index('bldg_area')] = row[field_names.index('SUM_Assess_BLD_AREA')]
    row[field_names.index('res_area')] = row[field_names.index('SUM_Assess_RES_AREA')]
    row[field_names.index('luc_1')] = row[field_names.index('MIN_Assess_USE_CODE')]
    row[field_names.index('luc_2')] = row[field_names.index('MAX_Assess_USE_CODE')]
    row[field_names.index('luc_adj_1')] = fixluc(row[field_names.index('muni_id')], row[field_names.index('luc_1')])
    row[field_names.index('luc_adj_2')] = fixluc(row[field_names.index('muni_id')], row[field_names.index('luc_2')])
    row[field_names.index('num_units')] = row[field_names.index('SUM_Assess_UNITS')]
    row[field_names.index('units_est')] = LU_UnitsCalctor(row[field_names.index('luc_adj_1')], row[field_names.index('num_units')], row[field_names.index('loc_id_cnt')])
    row[field_names.index('units_src')] = Units_SourceFindr(row[field_names.index('units_est')], row[field_names.index('num_units')], row[field_names.index('loc_id_cnt')])
    row[field_names.index('num_rooms')] = row[field_names.index('SUM_Assess_NUM_ROOMS')]
    row[field_names.index('yr_built')] = row[field_names.index('MAX_Assess_YEAR_BUILT')]
    row[field_names.index('site_addr')] = row[field_names.index('MAX_Assess_SITE_ADDR')]
    row[field_names.index('addr_str')] = row[field_names.index('MAX_Assess_FULL_STR')]
    row[field_names.index('addr_num')] = row[field_names.index('MAX_Assess_ADDR_NUM')]
    row[field_names.index('addr_zip')] = row[field_names.index('MAX_Assess_ZIP')]
    row[field_names.index('owner_name')] = row[field_names.index('MAX_Assess_OWNER1')]
    row[field_names.index('owner_addr')] = row[field_names.index('MAX_Assess_OWN_ADDR')]
    row[field_names.index('owner_city')] = row[field_names.index('FIRST_Assess_OWN_CITY')]
    row[field_names.index('owner_stat')] = row[field_names.index('FIRST_Assess_OWN_STATE')]
    row[field_names.index('owner_zip')] = row[field_names.index('FIRST_Assess_OWN_ZIP')]
    row[field_names.index('fy')] = row[field_names.index('FIRST_Assess_FY')]
    row[field_names.index('sqm_imperv')] = row[field_names.index('SUM_imp_bld_fc_areasqm_12')]
    row[field_names.index('sqm_bldg')] = row[field_names.index('building_footp_sqm_j')] 
    row[field_names.index('sqm_imperv')] = fixImperv(row[field_names.index('sqm_imperv')], row[field_names.index('sqm_bldg')])
    row[field_names.index('sqm_pave')] = sqmPavedCalctor(row[field_names.index('sqm_imperv')], row[field_names.index('sqm_bldg')])
    row[field_names.index('far')] = FARcalctor(row[field_names.index('lot_areaft')], row[field_names.index('bldg_area')], row[field_names.index('res_area')])
    row[field_names.index('pct_imperv')] = PropImprvCalctor(row[field_names.index('sqm_imperv')], row[field_names.index('lot_areaft')]  )
    row[field_names.index('pct_bldg')] = PropBldRFTpCalctor(row[field_names.index('building_footp_sqm_j')], row[field_names.index('lot_areaft')])
    row[field_names.index('pct_pave')] = PropPavdCalctor(row[field_names.index('sqm_imperv')], row[field_names.index('sqm_bldg')], row[field_names.index('lot_areaft')])
    row[field_names.index('landv_pac')] = calcLandValPerAcre(row[field_names.index('land_value')], row[field_names.index('lot_areaft')]) 
    row[field_names.index('Bldgv_psf')] = calcBldgValPerSqft(row[field_names.index('bldg_value')], row[field_names.index('far')], row[field_names.index('lot_areaft')])
    row[field_names.index('bldlnd_rat')] = calcILratio(row[field_names.index('bldg_value')], row[field_names.index('othr_value')], row[field_names.index('land_value')])
    cursor.updateRow(row)