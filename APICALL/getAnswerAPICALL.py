# get json
# install - pip install requests

import requests

links = ["https://reqbin.com/echo/get/json/page/1"]

results = []

for link in links:
    response = requests.get(link)
    items = response.json()["items"]
    results.append(items)

print(results)