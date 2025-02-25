import requests

body = {
    "name": "xinni",
    "age": 16,
}

r = requests.post("http://127.0.0.1:5000/postDemo", json=body)
print(r.json())


