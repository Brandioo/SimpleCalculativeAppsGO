import csv

salary_by_proffession = {}

with open('data/users.csv') as f:
    reader = csv.reader(f)
    for index,row in enumerate(reader):
        if index != 0:
            profession = row[-2]
            salary = float(row[-1])

            if profession in salary_by_proffession:
                salary_by_proffession[profession].append(salary)
            else:
                salary_by_proffession[profession] = [salary]


for key, value in salary_by_proffession.items():
    print(key, sum(value)/len(value))