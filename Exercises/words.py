list_of_words = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']

result = {}

for word in list_of_words:
    key = tuple(sorted(word))
    if key not in result:
        result[key] = [word]
    else:
        result[key].append(word)

print(list(result.values()))