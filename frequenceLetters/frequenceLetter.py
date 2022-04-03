word = "aaananana"

frequence = {}

for letter in word:
    frequence[letter] = word.count(letter)

new_word = []

key_counter = filter(lambda x: x[1] > 0, frequence.items())

while sum(frequence.values()) > 0:

    for key, value in frequence.items():

        if value > 0:
            new_word.append(key)
            frequence[key] -= 1

    print(frequence)
    print(new_word)