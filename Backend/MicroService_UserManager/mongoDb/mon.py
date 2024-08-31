# mon.py
from pymongo import MongoClient
from fastapi import HTTPException


class MongoDBService:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["users"]  # Collection for user

    def insert_user(self, user):
        self.collection.insert_one(user.__dict__)

    def get_user(self, user_id):
        user = self.collection.find_one({"user_id": user_id})
        if user:
            user = dict(user)  # casting to dict for pop warning
            user.pop('_id', None)
        return user

    def update_user(self, user):
        user_data = {k: v for k, v in user.__dict__.items() if k != '_id'}
        res = self.collection.update_one({"user_id": user.user_id}, {"$set": user_data})
        if res.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found to update")

    def delete_user(self, user_id):
        self.collection.delete_one({"user_id": user_id})

    def get_all_users(self):
        user_cursor = self.collection.find()
        user_list = list(user_cursor)
        for user in user_list:
            user.pop('_id')
        return user_list


