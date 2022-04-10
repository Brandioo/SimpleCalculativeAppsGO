import timeit
solution1 = ""

def is_decreasing(list_of_numbers) -> bool:
    return sorted(list_of_numbers, reverse = True) == list_of_numbers

def is_increasing(list_of_numbers) -> bool:
    return sorted(list_of_numbers) == list_of_numbers

def check(list_of_numbers):
    if is_decreasing(list_of_numbers):
        return "Decreasing"

    if is_increasing(list_of_numbers):
        return "Increasing"

    return "Neither"

check([1, 2, 3])

print(timeit.timeit(solution1, number = 200000))

