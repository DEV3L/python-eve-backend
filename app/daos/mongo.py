from pymongo import MongoClient
from bson import ObjectId


class MongoDatabase:
    def __init__(self):
        mongo_url = "mongodb://localhost:27017/test"
        client = MongoClient(mongo_url)
        mongo_db = client.test

        self.mongo_db = mongo_db

    def create(self, collection: str, entity: dict) -> str:
        insert_object = self.mongo_db[collection].insert_one(entity)
        return str(insert_object.inserted_id)

    def get(self, collection: str, id: str):
        return self.mongo_db[collection].find_one({'_id': ObjectId(id)})
