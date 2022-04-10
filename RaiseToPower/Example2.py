import timeit
solution1 = ""
def raise_to_power(list_of_numbers):
    temp_list = []
    for number in list_of_numbers:
        temp_list.append(number ** 3)
    return temp_list
raise_to_power(range(1,999))

solution2 = ""
def raise_to_power_v2(list_of_numbers):
    return [number ** 3 for number in list_of_numbers]
raise_to_power_v2(range(1,999))

print(timeit.timeit(stmt= solution1, number= 20))
print(timeit.timeit(stmt= solution2, number = 20))