def palindrome_generator(n):

    for i in range(1, n + 1):
          yield  (int('1' * i)**2)


letter = palindrome_generator(int(input()))
print(next(letter))
print(next(letter))
print(next(letter))
print(next(letter))
print(next(letter))