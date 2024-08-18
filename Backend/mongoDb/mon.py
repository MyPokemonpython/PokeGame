from pymongo import MongoClient
from fastapi import FastAPI, HTTPException


class MongoDBService:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["users"]  ## collection for user


db_service = MongoDBService("mongodb://localhost:27017", "PokemonUsers")
db_service.close()


def insert_user(self, user):
    self.collection.insert_one(user.__dict__)


def get_user(self, user_id):
    self.collection.find_one({"user_id": user_id})


def update_user(self, user):
    self.collection.update_one({"user_id": user.user_id}, {"$set": user.__dict__})


def delete_user(self, user):
    def close(self):
        self.client.close()
