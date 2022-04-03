# Python3 implementation of above idea

# A function to check if n is palindrome
def isPalindrome(n: int) -> bool:
    # Find reverse of n
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10

    # If n and rev are same,
    # then n is palindrome
    return (n == rev)


numbers = list(range(1,7000))

# prints palindrome between min and max
def countPal(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if isPalindrome(i):
            print(i, end=" ")


# Driver Code
if __name__ == "__main__":
    countPal(1, 7000)