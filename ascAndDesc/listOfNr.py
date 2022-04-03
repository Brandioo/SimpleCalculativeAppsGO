def reorder_digits(list_of_numbers):
    reorder = map(lambda num: str(num), list_of_numbers)
    order = map(lambda num: sorted(num), reorder)
    rejoin = map(lambda num: int("".join(num)), order)
    print(list(rejoin))
reorder_digits([515, 341, 98, 44, 211])