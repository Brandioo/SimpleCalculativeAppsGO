def find_in_list(num, list_of_numbers):
    for number in list_of_numbers:
        if num == number:
            return True
    return False

result = find_in_list(num = 7, list_of_numbers = [1,2,3,4])
print(result)