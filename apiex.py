import requests, json

resp = requests.get('https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow')

'''print(resp.json())'''

for item in resp.json()["items"]:
    if item["score"] == 0:
        print(item["title"])