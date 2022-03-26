secret = str(1234)
tents = [4379, 2379]

results = []

for tent in tents:
    found = 0
    match_position = 0

    for digit in str(tent):
        if digit in secret:
            found += 1

            if secret.index(digit) == str(tent).index(digit):
                match_position += 1
    res = f"{match_position}-{found}"
    results.append(res)

print(results)