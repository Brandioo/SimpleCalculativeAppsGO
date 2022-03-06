def get_zeros(list_of_numbers):
    list_of_count = []
    cnt = 0
    for index, number in enumerate(list_of_numbers):
        if number == 0:
            cnt += 1
        if number != 0 or index + 1 == len(list_of_numbers):
            list_of_count.append(cnt)
            cnt = 0
    return max(list_of_count)
