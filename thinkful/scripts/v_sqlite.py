# The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite

# Connect to database
con = lite.connect('../db/getting_started.db')

with con:
	# From the connection, you get a cursor object. The cursor is what goes over the records that result from a query
	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')
	# You're fetching the data from the cursor object. Because you're only fetching one record, you'll use the `fetchone()` method. If fetching more than one record, use the `fetchall()` method.
	data = cur.fetchone()
	# Finally, print the result.
	print "SQLite version: %s" % data