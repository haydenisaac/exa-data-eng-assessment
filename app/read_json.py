import os
from fhir.resources.bundle import Bundle

path = "./data/"
json_files = os.listdir(path)

collections = set()

for i in range(len(json_files)):
	filename = path + json_files[i]
	data = Bundle.parse_file(filename)
	for item in data.entry:
		resource_type = item.resource.resource_type
		if resource_type not in collections:
			collections.add(resource_type)
			## Create Mongo db collection 

		## Push the data to mongo


