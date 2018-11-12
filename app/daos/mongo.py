import os

from bson import ObjectId
from pymongo import MongoClient


class MongoDatabase:
    def __init__(self):
        mongo_url = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/test')
        client = MongoClient(mongo_url)
        mongo_db = client.test

        self.mongo_db = mongo_db

    def create(self, collection: str, entity: dict) -> str:
        insert_object = self.mongo_db[collection].insert_one(entity)
        return str(insert_object.inserted_id)

    def get(self, collection: str, id: str):
        return self.mongo_db[collection].find_one({'_id': ObjectId(id)})

    def find(self, collection: str, query: dict = None):
        return self.mongo_db[collection].find(query)
