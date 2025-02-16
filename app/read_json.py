import os
from fhir.resources.bundle import Bundle
from mongo_connect import MongoConnection
import json
import sys

def main(path = "./data/"):
    json_files = os.listdir(path)

    client = MongoConnection()

    for i in range(len(json_files)):
        filename = path + json_files[i]
        try:
            data = Bundle.parse_file(filename)
        except json.decoder.JSONDecodeError:
            continue
        data_out = []
        previous_type = None
        for item in data.entry:
            resource_type = item.resource.resource_type
            dict_data = json.loads(item.resource.json())
            if resource_type == previous_type or previous_type is None:
                data_out.append(dict_data) 
            else:
                client.pushToMongo(previous_type, data_out)
                data_out = [dict_data]
            previous_type = item.resource.resource_type
        client.pushToMongo(previous_type, data_out)
        print("Completed %u of %u!" %(i+1, len(json_files)))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(path= sys.argv[1])
    else:
        main()

