def replace(list_of_elements, el1, el2):
    for index, element in enumerate(list_of_elements[:]):
        if element == el1:
            list_of_elements[index] = el2

    return list_of_elements


print(replace([1, 1, 1, 2], 1, 2))


#
def swap(list_of_elements: list, el1: int, el2: int):
    try:
        value1 = list_of_elements[el1]
        value2 = list_of_elements[el2]
        list_of_elements[el1] = value2
        list_of_elements[el2] = value1
        return list_of_elements
    except:
        return list_of_elements


print(swap([1, 2, 3, 4], 0, 1))
