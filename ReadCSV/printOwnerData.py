import json

with open('data/animals.json') as file:
    animals = json.load(file)

    for animal in animals:
        if "owner_data" in animal:
            owners = animal["owner_data"]
            if "preview_users" in owners:
                previews_owners = owners["preview_users"]
                for owner in previews_owners:
                    print(owner["name"])