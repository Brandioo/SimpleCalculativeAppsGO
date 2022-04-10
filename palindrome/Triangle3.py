def palindromic_generator(n):
    number = 1
    numbers = ""
    while number <= n:
        numbers += str(number)
        pal_numbers = numbers + numbers[::-1][1:]
        yield pal_numbers
        number += 1
palindromic = palindromic_generator(5)
for num in palindromic:
    print(num)