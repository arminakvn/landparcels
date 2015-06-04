import os
import sys
import arcpy
import arcpy.da
import csv
from arcpy import env

WorkSpace = arcpy.GetParameterAsText(0)
fc = arcpy.GetParameterAsText(1)
output_txt = arcpy.GetParameterAsText(2)
env.workspace = WorkSpace

fields = arcpy.ListFields(fc)
field_names = [field.name for field in fields]

for i, f in enumerate(field_names):
	if f == 'Shape':
		del field_names[i]

with open(output_txt, 'w') as f:
	f.write(','.join(field_names)+'\n') #csv headers
	with arcpy.da.SearchCursor(fc, field_names) as cursor:
		for row in cursor:
			try:
				f.write(','.join([str(r) for r in row])+'\n')
			except:
				pass
