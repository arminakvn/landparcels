def read_luc_csv_to_dict(csvfile):
    import csv
    lu_lookup = {}
    with open(csvfile, 'rb') as mycsv:
        reader = csv.reader(mycsv)
        for row in reader:
             lu_lookup.update({(row[0], row[1]): row[2]})
    return lu_lookup

def read_realestatetypes_csv_to_dict(csvfile):
   
    import csv
    ret_lookup = {}
    with open (csvfile, 'rb') as mycsv:
        reader = csv.reader(mycsv)
        for row in reader:
            ret_lookup.update({row[0]:row[1]})
    return ret_lookup

def read_stndrd_usecode_csv_to_dict(csvfile):
    import csv
    suc_lookup = {}
    with open (csvfile, 'rb') as mycsv:
        reader = csv.reader(mycsv)
        for row in reader:
            suc_lookup.update({row[0]:row[1]})
    return suc_lookup

def read_muni_ids_to_dict(csvfile):
    import csv
    muniDic = {}
    with open (csvfile, 'rb') as mycsv:
        reader = csv.reader(mycsv)
        for row in reader:
            muniDic.update({row[1]: row[0]})
    return muniDic