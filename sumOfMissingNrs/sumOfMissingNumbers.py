# Python3 program to Find missing
# integers in list

def find_missing(lst):
    return [x for x in range(lst[0], lst[-1] + 1)
            if x not in lst]


# Driver code
lst = [1, 2, 4, 6, 7, 9, 10, 12]
# print(sum(find_missing(lst)))
print(find_missing(lst))


def sum_missing_numbers(list_of_numbers: list):
    missing_numbers = []
    _min = min(list_of_numbers)
    _max = max(list_of_numbers)
    for number in range(_min, _max + 1):
        if number not in list_of_numbers:
            missing_numbers.append(number)
    return sum(missing_numbers)


var = sum_missing_numbers([4, 3, 8, 1, 2]) == 18
print(var)
