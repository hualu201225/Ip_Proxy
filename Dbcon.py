import mysql.connector as mysql
import dbconfig

class Dbcon(object):

	def getDbCon(self):
		return mysql.connect(user=dbconfig.DB_USERNAME, password=dbconfig.DB_PASSWORD, 
			database=dbconfig.DB_DEFAULT_DATABASE, host=dbconfig.DB_HOST)


	def select(self, sql):
		dbcon = self.getDbCon()
		cursor = dbcon.cursor()
		cursor.execute(sql)
		data = cursor.fetchall()
		cursor.close()
		dbcon.close()
		return data


	def insert(self, sql, listdata):
		dbcon = self.getDbCon()
		cursor = dbcon.cursor()
		cursor.executemany(sql, listdata)
		dbcon.commit()
		cursor.close()
		return cursor.rowcount




