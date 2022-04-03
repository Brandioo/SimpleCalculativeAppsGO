users = [
    {"name": "mimoza", "grade": 9.1, "birthplace": "tirana"},
    {"name": "majlinda", "grade": 6, "birthplace": "gramshi"},
    {"name": "majlinda", "grade": 7, "birthplace": "peqini"},
    {"name": "test", "grade": 4, "birthplace": "kucova"},
]

names = ["Sokol", "Edit", "zana", "bora"]

filter_grades = filter( lambda user: user["grade"] >= 7 , users)
filter_birthplace = filter( lambda user: user["birthplace"] == "tirana" , list(filter_grades))


print(list(filter_birthplace))