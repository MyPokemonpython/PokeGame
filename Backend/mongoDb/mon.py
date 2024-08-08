from pymongo import MongoClient


class MongoDBService:
    def init(self, uri, db_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
