students = [
    ["Sokoli", 10],
    ["Albani", 8],
    ["Bora", 4],
    ["Artani", 6.8],
    ["Blerta", 6.8],
    ["0Blerta", 6.8],
    ["Aferdita", 8.7]
]

#step 1 find the second lowest grade
lowest_grade =sorted(students, key = lambda x: x[1])[1][1]

#step 2 find all the students with this grade
filtered_students = list(filter(lambda x: x[1] == lowest_grade, students ))

#step 3 sort the filtered students by Name and get first
print(sorted(filtered_students)[0])