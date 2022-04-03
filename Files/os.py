import os
import json


list_of_file_names = os.listdir("data")

os.mkdir("test_new_dir")

for file in list_of_file_names:
    with open("data/"+file) as f:
        if file.endswith(".json"):
            data = json.load(f)
            print(data)