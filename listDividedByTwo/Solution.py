import timeit


solution2 = ""
a= [
  [1, 0, 2],
  [5, 5, 7],
  [9, 4, 3]
]

new_list = []

for element in a:
    evens = list(filter(lambda x: x % 2 == 0, element))
    new_list.extend(evens)

sum(new_list)

print(timeit.timeit(solution2, number = 200000))
