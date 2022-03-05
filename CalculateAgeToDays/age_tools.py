def calc_age(n):
    if type(n) not in [float, int]:
        raise TypeError()
    n = round(n)
    if (n < 0):
        return 0
    test = n * 365
    return test
