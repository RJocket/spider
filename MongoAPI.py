'''
MongoAPI
'''
from pymongo import MongoClient

class MongoAPI(object):
	"""docstring for MongoApi"""
	def __init__(self, db_ip,db_port,db_name,collection_name):
		self.db_ip =db_ip
		self.db_port =db_port
		self.collection_name =collection_name
		self.client =MongoClient(db_ip,db_port)
		self.db =self.client[self.db_name]
		self.collection =self.db[self.collection_name]

	def get_one(self,query):
		return self.collection.find_one(query,projection ={"_id":False})

	def get_all(self,query):
		return self.collection.find(query)

	def add(self,kv_dict):
		return self.collection.insert(kv_dict)

	def delete(self,query):
		return self.collection.delete_many(query)

	def check_exist(self,query):
		ret = self.collection.find_one(query)
		return ret!= None #T or F

	#更新集合中数据，若找不到，则新增一条数据
	def update(self,query,kv_dict):
		self.collection.update_one(query,{'$set':kv_dict},upsert=True)




		