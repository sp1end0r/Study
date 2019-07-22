#file name : db_module.py
#pwd : /home/sp1end0r/source/cert/project/app/module

from pymysql import *

class database():
	def __init__(self):
		self.db = connect(host='localhost', user='root', password='your_password', db='db_name',charset='utf8')
		self.cursor = self.db.cursor(cursors.DictCursor)

	def execute(self, query, args={}):
		self.cursor.execute(query,args)

	def executeOne(self, query, args={}):
		self.cursor.execute(query, args)
		row = self.cursor.fetchone()
		return row

	def executeAll(self, query, args={}):
		self.cursor.execute(query, args)
		row = self.cursor,fetchall()
		return row

	def commit():
		self.db.commit()


