def is_anagram(word1, word2):
    if sorted(word1) == sorted(word2) :
        print("This two words are anagram")
    else:
        print("This two words are not anagram")

is_anagram('listen','silent')