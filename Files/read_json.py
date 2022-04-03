import json

with open('./data/data.json') as f:
    data = json.load(f)

    print(data[0])

for comment in data:
    print(comment)