# keep only vowels version 1
def keep_only_vowels(func):
    def wrapper(args):
        result = func(args)

        vowels = "aeuio"
        new_word = ""
        for letter in result:
            if letter.lower() in vowels:
                new_word += letter
        return new_word

    return wrapper


@keep_only_vowels
def print_words(sentence):
    return sentence.upper()


print(print_words("hello world"))