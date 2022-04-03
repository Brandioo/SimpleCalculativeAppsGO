pairs = [(1, 10, 3, 4), (2, 12, 0), (3, 25, 8)]

# print(sorted(pairs, key=lambda x: len(x)))
# print(max(pairs, key=lambda x: x[1]))
# print(min(pairs, key=lambda x: sum(x)))
print(sorted(pairs, key=lambda x: x[-1]))

# # python 3.x
# valuesList = [222,333,444,555,2,1]
#
# print(max(valuesList, key=lambda value: int(value)))
#
# # python 3.x
# valuesList = [222,333,444,555, 2, 1]
#
# print(min(valuesList, key=lambda value: int(value)) )