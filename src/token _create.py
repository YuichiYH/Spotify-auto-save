import json
import os

if not os.path.isdir('json'):
    os.mkdir('json')

client_id = input("Insert your client ID tonken\n")
client_secret = input("Insert your client secret tonken\n")

x = {
    'client_id': client_id,
    'client_secret':client_secret
}


with open("json/token.json", "w") as file:
    print("creating or updating file...")
    json.dump(x,file)
    print("File updated")