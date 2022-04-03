numbers = list(range(1, 7000))

new = filter(lambda n: str(n) == (str(n)[::-1]), numbers)
new_lc = [number for number in numbers if str(number) == (str(number)[::-1])]
print(list(new))
print(list(new_lc))


# Dividing By 5
new_list = [n *    n for n in range(400) if n % 5 == 0]
print(new_list)