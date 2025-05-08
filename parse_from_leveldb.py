import os
import json
from leveldb_export import parse_leveldb_documents

COLLECTION_NAMES = ["baneplan_events", "live_events"]
BASE_DIR_PATH = "all_namespaces/all_kinds"

# Get all output files
all_output_files: list[str] = [f for f in os.listdir(BASE_DIR_PATH) if f.startswith("output")]
number_of_files = len(all_output_files)
print(f"Number of files: {number_of_files}")

# Parse all files - create one file output.json with all docs.
metadata_file_name = "output/metadata.json"
metadata_file = open(metadata_file_name, "w")

output_file_name = "output/output.json"
output_file = open(output_file_name, "w")

collections: dict[str, dict] = {}
for i in range(number_of_files):
    file_name = all_output_files[i]
    docs = list(parse_leveldb_documents(BASE_DIR_PATH+"/"+file_name))
    for doc in docs:
        try:
            output_file.write(json.dumps(doc))
            output_file.write("\n")

            collection_name = doc["_key"]["path"].split("/")[0]
            if collection_name not in collections:
                collections[collection_name] = {
                    "name": collection_name,
                    "count": 0,
                }
            collections[collection_name]["count"] += 1
            
        except Exception as e:
            print(f"Error: {e}")

output_file.write("]")
output_file.close()

metadata_file.write(json.dumps(collections))
metadata_file.close()