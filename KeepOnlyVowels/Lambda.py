import timeit
# keep only vowels version 2, lambda
solution2 = ""
def keep_only_vowels(func):

    def wrapper(args):
        result = func(args)

        vowels = "aeuio"
        new_word = filter(lambda l: l.lower() in vowels,  result)
        return "".join(list(new_word))
    return wrapper


@keep_only_vowels
def print_words(sentence):
    return sentence.upper()
print_words("hello wolrd")

print(timeit.timeit(solution2))