def generate_row(n):
    row = ""
    for i in range(1, n + 1):
        row += str(i)

    rev = row[::-1]
    return row + rev[1:]


def draw_piramide(n):
    given = 1
    while given <= n:
        yield generate_row(given)
        given += 1


gen = draw_piramide(8)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))