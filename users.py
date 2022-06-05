import json

users = {"tim": ["Tim", "02/09/02", "12345"], "james": ["James", "04/05/00", "8765"], "sarah": ["Sarah", "04/12/00", "6444"]}

json_dump_users = json.dumps(users)
json_object_users = json.loads(json_dump_users)
