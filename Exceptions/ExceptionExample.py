class MyException(Exception):
    pass


a = 3
b = [1, 0, 2]
for elem in b:
    try:
        result = a / elem
    except ZeroDivisionError:
        continue
    print(f"Result is: {result}")

