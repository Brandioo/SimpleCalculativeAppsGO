from string import ascii_lowercase


def alfabet_generator():
    for index, letter in enumerate(ascii_lowercase):
        yield letter, index


letters = alfabet_generator()
for letter in letters:
    print(letter)

letter = alfabet_generator()
print(next(letter))
print(next(letter))
print(next(letter))
print(next(letter))
