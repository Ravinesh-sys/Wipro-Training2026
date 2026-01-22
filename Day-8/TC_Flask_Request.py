import requests

#& geturl 1

geturl1 = "http://127.0.0.1:5000/users"

response = requests.get(geturl1)

print(response.status_code)
print(response.json())

#& geturl with id

geturl2 = "http://127.0.0.1:5000/users/1"

response = requests.get(geturl2)

print(response.status_code)
print(response.json())

#& posturl

posturl = "http://127.0.0.1:5000/users"

body = {
    "name": "Neha"
}

response = requests.post(posturl, json=body)

print(response.status_code)
print(response.json())

#& patch url

patchurl = "http://127.0.0.1:5000/users"

body = {
    "name": "Ravi"
}

response = requests.post(patchurl, json=body)

print(response.status_code)
print(response.json())

#& delete object

deleteurl = "http://127.0.0.1:5000/users/2"

response = requests.delete(deleteurl)

print(response.status_code)
print(response.json())