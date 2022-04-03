names = ["sokol", "blerta", "asllan", "muhamet"]

upperCase_names = list(map(lambda name: name.upper(), names))
filter_name = list(filter(lambda name: len(name)==5, names))

new_list = [name.upper() for name in names]
new_tuple = (name.upper() for name in names)
new_set = (name.upper() for name in names)
print(new_list, new_tuple, new_set)

print(filter_name)
