import requests

url = "https://meowfacts.herokuapp.com/"

r = requests.get(url)
print(r.json()["data"][0])