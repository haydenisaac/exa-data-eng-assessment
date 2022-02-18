from pymongo import MongoClient

client = MongoClient("mongodb://root:password@mongo:27017")

db = client["test"]
collection = db["author"]
collection.insert_one({"name": "Hayden"})
