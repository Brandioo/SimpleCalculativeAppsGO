with open('lyrics/song.txt') as f:
    data = f.readlines()
    counter = 0
    for row in data:
        for word in row.split():
            if word.lower() == "love":
                counter += 1
print(counter)