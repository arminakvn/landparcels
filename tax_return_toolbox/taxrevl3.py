# author: armin.akhavan@gmail.com
import arcpy 
import arcpy.da
from parcels import dclass_parcels as _parcel
from lookup_csv_to_dict import read_muni_ids_to_dict
from formatter_functions import MuniLookup
from connect_postgres import makeMuniLookUpDict

# parcels_mosaic_gdb = arcpy.GetParameterAsText(0) # the file geodatabase containing the regional parcel mosaic
infc = arcpy.GetParameterAsText(0) # MAPC's Parcels mosaic
taxratetb = arcpy.GetParameterAsText(1) # updated version of the departmant of revenue's tax rates by class

parcels_mosaic_gdb = arcpy.Describe(infc).path
arcpy.env.workspace = parcels_mosaic_gdb


muniDic = makeMuniLookUpDict()


# field from dor's tax rate by class dataset
fields = ["Approval_Rank", "Community_Name", "Tax_Rate_Residential", "Tax_Rate_Open_Space", "Tax_Rate_Commercial", "Tax_Rate_Industrial", "Tax_Rate_Personal", "Date_Approved", "Fiscal_Year"]
txdict = {}
txdictComm = {}
txdictIndus = {}
txdictOpenS = {}
# row[fields.index('FIRST_Assess_OWN_STATE')]
with arcpy.da.SearchCursor(taxratetb, fields) as cursor:
        for row in cursor:
            try:

                txdict.update({ ( muniDic[row[fields.index('Community_Name')]], row[fields.index('Fiscal_Year')]): row[fields.index('Tax_Rate_Residential')]})
                txdictComm.update({(muniDic[row[fields.index('Community_Name')]], row[fields.index('Fiscal_Year')]): row[fields.index('Tax_Rate_Commercial')]})
                txdictIndus.update({(muniDic[row[fields.index('Community_Name')]], row[fields.index('Fiscal_Year')]): row[fields.index('Tax_Rate_Industrial')]})
                txdictOpenS.update({(muniDic[row[fields.index('Community_Name')]], row[fields.index('Fiscal_Year')]): row[fields.index('Tax_Rate_Open_Space')]})
            except:
                print "error?"
      





fieldName1 = "txrev_pac"
fieldAlias1 = "Tax Revenue Per Acre"

arcpy.AddField_management(infc, fieldName1, "DOUBLE", "", "", "",
                          fieldAlias1, "NULLABLE", "NON_REQUIRED")

fieldName2 = "taxrate"
fieldAlias2 = "Tax Rate"

arcpy.AddField_management(infc, fieldName2, "DOUBLE", "", "", "",
                          fieldAlias2, "NULLABLE", "NON_REQUIRED")


field_names = [str(f.name) for f in arcpy.ListFields(infc)]

####### 11/25/13 ==> adjusting for 2013 inflation ########
#data is from: ftp://ftp.bls.gov/pub/special.requests/cpi/cpiai.txt

# fieldName3 = "txrvpac_adj"
# fieldAlias3 = "Tax Revenue Per Acre Adjusted for Inflation"

# arcpy.AddField_management(infc, fieldName3, "DOUBLE", "", "", "",
#                           fieldAlias3, "NULLABLE", "NON_REQUIRED")







#
#csidict = {2009: 214.537, 2010: 218.056, 2011: 224.939, 2012: 229.594, 2013: 232.9367}

def getsci(fy):
    if fy == 2007:
        return 207.342
    elif fy == 2008:
        return 215.303
    elif fy == 2009:
        return 214.537
    elif fy == 2010:
        return 218.056
    elif fy == 2011:
        return 224.939
    elif fy == 2012:
        return 229.594
    elif fy == 2013:
        return 232.9367
    


# if (id_cntr == None) or (id_cntr == null): 
id_cntr = 0

with arcpy.da.UpdateCursor(infc, field_names) as cursor:
    for row in cursor:
        id_cntr += 1
        # using the class, first define an instance, set the neccessary attributes then run the method for the instance
        e_parcel = _parcel(id_cntr) 
        setattr(e_parcel, 'fy', row[field_names.index('fy')])
        setattr(e_parcel, 'muni_id', row[field_names.index('muni_id')])
        setattr(e_parcel, 'totval_pac', row[field_names.index('totv_pac')])
        e_parcel.gettaxrate(txdict, txdictComm, txdictIndus, txdictOpenS)
        taxRate = getattr(e_parcel, "tax_rate")
        row[field_names.index('taxrate')] = taxRate
        e_parcel.taxRetPerAcre()
        taxrevPerAcre = getattr(e_parcel, "txrev_pac")
        row[field_names.index('txrev_pac')] = taxrevPerAcre
        cursor.updateRow(row)