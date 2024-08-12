from pymongo import MongoClient
from fastapi import FastAPI, HTTPException


class MongoDBService:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def close(self):
        self.client.close()


db_service = MongoDBService("mongodb://localhost:27017", "PokemonUsers")
db_service.close()


def insert_user(self, user):
    pass


def get_user(self,user_id):
    pass

def update_user(self,user):
    pass

def delete_user(self,user):
    pass
