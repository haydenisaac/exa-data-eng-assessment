import os
from fhir.resources.bundle import Bundle
from mongo_connect import MongoConnection
import json

def convert_to_dict(data):
   return json.loads(data)

path = "./data/"
json_files = os.listdir(path)

client = MongoConnection()

for i in range(len(json_files)):
   filename = path + json_files[i]
   data = Bundle.parse_file(filename)
   for item in data.entry:
      resource_type = item.resource.resource_type
      dict_data = convert_to_dict(item.resource.json())
      client.pushToMongo(resource_type, dict_data)
   print("Completed %u of %u!" %(i+1, len(json_files)))

