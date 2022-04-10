import timeit

solution2 = ""
def is_decreasing(list_of_numbers) -> bool:
    is_desc = True

    i = list_of_numbers[0]

    for number in list_of_numbers[1:]:
        if not number <= i:
            return False
        i = number

    return is_desc

def is_increasing(list_of_numbers) -> bool:
    is_desc = True

    i = list_of_numbers[0]

    for number in list_of_numbers[1:]:
        if not number >= i:
            return False
        i = number

    return is_desc

def check(list_of_numbers):
    if is_decreasing(list_of_numbers):
        return "Decreasing"

    if is_increasing(list_of_numbers):
        return "Increasing"

    return "Neither"

check([1, 2, 3])

print(timeit.timeit(solution2, number = 200000))