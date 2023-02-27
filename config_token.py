import json

x = {
    'client_id': "YOUR CLIENT ID TOKEN",
    'client_secret':"YOUR CLIENT SECRET TOKEN"
}

with open("json/token.json", "w") as file:
    json.dump(x,file)