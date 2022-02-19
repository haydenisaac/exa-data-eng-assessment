from pymongo import MongoClient

class MongoConnection:
    """
        Establishes a connection with the mongo database client.
        Allows the user to insert data into a collection.
    """
    def __init__(self):
        self.client_address = "mongodb://root:password@mongo:27017"

    def connect(self):
        self.client = MongoClient(self.client_address)
        self.db = self.client.health

    def closeConnection(self):
        self.client.close()

    def insertToCollection(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_one(data)

    def pushToMongo(self, resourceType, data):
        self.connect()
        self.insertToCollection(resourceType, data)    
        self.closeConnection()    

