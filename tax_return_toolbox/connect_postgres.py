# connecting to mapc's sdevm postgres data
# author: armin.akhavan@gmail.com
import psycopg2 # on windows install using :http://www.stickpeople.com/projects/python/win-psycopg/
import sys
import pprint

conn_string = "host='sdevm' dbname='ds' user='viewer' password='mapcview451'"
# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()

# execute our Query
cursor.execute("SELECT * FROM tabular._datakeys_muni351")

# retrieve the records from the database
records = cursor.fetchall()

# print out the records using pretty print
# note that the NAMES of the columns are not shown, instead just indexes.
# for most people this isn't very useful so we'll show you how to return
# columns as a dictionary (hash) in the next example.
# pprint.pprint(records)
colnames = [desc[0] for desc in cursor.description]
# pprint.pprint(colnames)
# pprint.pprint(cursor.description)
# pprint.pprint(records[1])

def makeMuniLookUpDict():
	muni_dict = {}
	for row in records:
		muni_dict.update({row[colnames.index('municipal')]:row[colnames.index('muni_id')]})
	return muni_dict