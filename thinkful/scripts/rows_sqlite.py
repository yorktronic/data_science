import sqlite3 as lite

cities = (('Las Vegas', 'NV'), ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December', 90), ('Atlanta', 2013, 'July', 'January', 80))

con = lite.connect('../db/getting_started.db')

# Inserting rows to db
cur = con.cursor()

with con:
	cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
	cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
	cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 65)")
	cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 79)")

	# A more efficient way is to use executemany()
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)