numbers = [515, 341, 98, 44, 211]

list(map(lambda x: int("".join(sorted(str(x)))),numbers ))