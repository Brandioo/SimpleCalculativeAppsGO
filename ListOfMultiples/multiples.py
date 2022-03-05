def list_of_multiples_version2(num: int, length: int) -> list:
    multiples = []

    if type(length) != int:
        raise TypeError()

    if length <= 0:
        raise ValueError()

    for m in range(1, length + 1):
        multiples.append(m * num)
    return multiples