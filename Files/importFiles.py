import csv

with open("data/names.csv") as f:
    data = csv.reader(f)

    for index, row in enumerate(data):
        if index != 0:
            if int(row[2]) >= 50:
                print(row)
