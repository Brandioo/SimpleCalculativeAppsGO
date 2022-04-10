def make_upper(func):
    def wrapper(args):
        result = func(args)
        return result.upper()

    return wrapper


@make_upper
def remove_vowels(sentence):
    vowels = "aeuio"
    new_sentence = ""
    for letter in sentence:
        if letter not in vowels:
            new_sentence += letter
    return new_sentence


remove_vowels("hello")