import sqlite3 as lite
import pandas as pd

con = lite.connect('../db/getting_started.db')

# Select all the rows and print the result set one at a time
with con:

	cur = con.cursor()
	cur.execute("SELECT * FROM cities")

	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)