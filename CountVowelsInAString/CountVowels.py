# Function to count vowel
def vowel_count(string):
    if type(string) not in [str]:
        return 0
    # Initializing count variable to 0
    count = 0

    # Creating a set of vowels
    vowel = set("aeiouAEIOU")

    # Loop to traverse the alphabet
    # in the given string
    for alphabet in string:

        # If alphabet is present
        # in set vowel
        if alphabet in vowel:
            count+=1

    # print(count)
    return count


# # Driver code
# inputString = str(input("Please type a sentence: "))
#
# # Function Call
# vowel_count(inputString)