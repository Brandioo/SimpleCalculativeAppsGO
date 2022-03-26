a = [1, 2, 3]
b = [4, 8, 9]
c = [4, 8, 9]
s = []
for nr in a:
    for nr2 in b:
        for nr3 in b:
            s.append(nr + nr2 + nr3)
print(s)
