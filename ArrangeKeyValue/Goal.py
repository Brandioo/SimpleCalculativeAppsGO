users = {
    "Mubashir": "Name",
    "31": "Age",
    "Male": "Sex",
    "Pilot": "Job",
    "Matt": "Name",
    "40": "Age",
    "Programmer": "Job"
}

new_users = {}

for key, value in users.items():
    if value in new_users:
        new_users[value].append(key)
    else:
        new_users[value] = [key]

print(new_users)
