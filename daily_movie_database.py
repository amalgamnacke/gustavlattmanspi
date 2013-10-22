import sqlite3 as lite

class DailyMovieDatabase:
	def __init__(self):
		self.debugMode = True
		self.database_name = "daily_movie_database.db"

		# Initialize database
		self.debug("Initializing SQLITE3: " + self.database_name)
		con = None
		con = lite.connect(self.database_name)
		if con == None: self.debug("Could not connect to database: " + self.database_name)

		try:
			self.debug("Creating table movies...")
			con.execute("CREATE TABLE movies(id INTEGER PRIMARY KEY NOT NULL, title TEXT)")
		except:
			self.debug("Table movies already exists...")
		
		con.close()

	def debug(self, msg):
		if self.debugMode: print msg

	def isMovieInDatabase(self, title):
		con = None
		
		con = lite.connect(self.database_name)
		if con == None: self.debug("Could not connect to database: " + self.database_name)
			
		cur = con.cursor()
		
		cur.execute("INSERT INTO movies VALUES(1, 'majjo')")
		cur.execute("SELECT title FROM movies WHERE title = '"+title+"'")
		data = cur.fetchone()

		con.close()

		return data != None



jashd = DailyMovieDatabase()
print jashd.isMovieInDatabase("m")
