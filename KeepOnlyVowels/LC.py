import timeit
# keep only vowels version 2, LC
solution1 = ""
def keep_only_vowels(func):

    def wrapper(args):
        result = func(args)

        vowels = "aeuio"
        return "".join([ letter for letter in result if letter.lower() in vowels ])
    return wrapper


@keep_only_vowels
def print_words(sentence):
    return sentence.upper()
print_words("hello world")

print(timeit.timeit(solution1))