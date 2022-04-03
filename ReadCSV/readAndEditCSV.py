# read and edit csv file
import csv

with open("data/students.csv") as read_file:
    rows = list(csv.reader(read_file))

    for index, row in enumerate(rows):
        if index == 0:
            rows[index].append('birthplace')
        else:
            rows[index].append(66)

    print(rows)

    with open("data/students.csv", "w") as write_file:
        writer = csv.writer(write_file)
        writer.writerows(rows)