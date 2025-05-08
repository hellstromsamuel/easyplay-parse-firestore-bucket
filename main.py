import json

COLLECTION_NAMES = ["baneplan_events", "live_events"]

live_events_docs = []
baneplan_events_docs = []

output_file_name = "output/output.json"
output_file = open(output_file_name, "r")

for line in output_file:
    try:
        doc: dict = json.loads(line)
        path = doc["_key"]["path"]

        collection = path.split("/")[0]
        id = path.split("/")[1]

        # Add field "id", remove "_key"
        doc["id"] = id
        del doc["_key"]

        if collection == "live_events":
            live_events_docs.append(doc)
        elif collection == "baneplan_events":
                baneplan_events_docs.append(doc)
    except Exception as e:
        print(f"Error: {e}")

output_file.close()

print(f"Live events: {len(live_events_docs)}")
print(f"Baneplan events: {len(baneplan_events_docs)}")



BANEPLAN_ID = "zSF5JJnVPVlsZComZqm7"
live_events_docs_with_baneplan_id = [doc for doc in live_events_docs if "baneplanId" in doc and doc["baneplanId"] == BANEPLAN_ID]
baneplan_events_docs_with_baneplan_id = [doc for doc in baneplan_events_docs if "baneplanId" in doc and doc["baneplanId"] == BANEPLAN_ID]

print(f"Live events with baneplan id: {len(live_events_docs_with_baneplan_id)}")
print(f"Baneplan events with baneplan id: {len(baneplan_events_docs_with_baneplan_id)}")

output_file = open(f"output/live_events_with_baneplan_id-{BANEPLAN_ID}.json", "w")
json_data = { }
for doc in live_events_docs_with_baneplan_id:
     try:
          json_data[doc["id"]] = doc
     except Exception as e:
          print(f"Error live_events: {e}")
output_file.write(json.dumps(json_data))
output_file.close()

output_file = open(f"output/baneplan_events_with_baneplan_id-{BANEPLAN_ID}.json", "w")
json_data = { }
for doc in baneplan_events_docs_with_baneplan_id:
     try:
          json_data[doc["id"]] = doc
     except Exception as e:
          print(f"Error baneplan_events: {e}")
output_file.write(json.dumps(json_data))
output_file.close()