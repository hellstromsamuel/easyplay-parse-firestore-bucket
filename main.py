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







# # for line in output_file:
# #     doc = json.loads(line)
# #     if doc["_key"]["path"].startswith("live_events"):
#         live_events_docs.append(doc)
#     else:
#         baneplan_events_docs.append(doc)

# print(f"Live events: {len(live_events_docs)}")
# print(f"Baneplan events: {len(baneplan_events_docs)}")

# # Write to json files
# for doc in all_docs:
#     if doc["_key"]["path"].startswith("live_events"):
#         live_events_data["count"] += 1
#         live_events_data["docs"].append(doc)
#     else:
#         baneplan_events_data["count"] += 1
#         baneplan_events_data["docs"].append(doc)

# # Write final data to files
# with open("live_events.json", "w") as live_events_json_file:
#     json.dump(live_events_data, live_events_json_file)
    
# with open("baneplan_events.json", "w") as baneplan_events_json_file:
#     json.dump(baneplan_events_data, baneplan_events_json_file)





"""
  {
    "activityType": "LIVE_FROM_BANEPLAN",
    "activityTypeName": null,
    "baneplanEventId": "1729670815734-bv1ary",
    "baneplanId": "4ZqYd1gsUFf7FfmmnhdI",
    "clubId": "BmN5EYWRsw8BpP2fNlXW",
    "date": "2024-12-04",
    "endTime": "19:00",
    "id": "1729670815734-bv1ary_2024-12-04",
    "indexWeekday": 2,
    "isCancelled": false,
    "isEdited": false,
    "mainStadiumId": "XMI4dtiNLbQaGh2pCOVb",
    "mainStadiumName": "Grilstadbanen",
    "originalDate": "2024-12-04",
    "stadiumSize": "7",
    "stadiumZone": null,
    "startTime": "17:45",
    "tags": null,
    "teamId": "FKtTtzqDISj5MR4hgq9I",
    "teamName": "G8 (2017)",
    "title": "G8 (2017): Trening",
    "type": "LiveEventBaneplan",
    "_key": {
      "id": null,
      "name": "1729670815734-bv1ary_2024-12-04",
      "namespace": "",
      "app": "e~easyplay-no",
      "path": "live_events/1729670815734-bv1ary_2024-12-04"
    }
  },
"""