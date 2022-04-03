import csv

with open("data/names.csv", 'a') as f:
    writer = csv.writer(f)
    writer.writerow(["Brand", "Citozi", 20, "Tirana"])