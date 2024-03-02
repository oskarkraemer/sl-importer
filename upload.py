import requests
import json

DB_URL = "http://localhost:8090"

def auth(user, pwd):
    #get auth token

    url = DB_URL + "/api/collections/users/auth-with-password"
    headers = {'content-type': 'application/json'}
    data = {"identity": user, "password": pwd}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    return response.json()['token']

def upload_file(path, token):
    #create collection using Authorization HTTP header; Authorization: TOKEN
    headers = {'Authorization': token}
    r = requests.post(DB_URL + "/api/collections/bibliotheca_import/records", json={}, headers=headers)

    #load file and read content
    file = open(path, "rb")

    if r.status_code == 200:
        requests.patch(DB_URL + "/api/collections/bibliotheca_import/records/" + r.json()["id"], files={"document": file}, headers=headers)

#Read credentials from .auth file
with open(".auth", "r") as f:
    auth_data = json.load(f)

token = auth(auth_data["user"], auth_data["password"])
print(token)

upload_file("./test.txt", token)