#get average salary for users.csv
import csv
s = 0
c = 0
with open('data/users.csv') as f:
    reader = csv.reader(f)
    for index,row in enumerate(reader):
        if index != 0:
            s += float(row[-1])
            c += 1

print(s/c)