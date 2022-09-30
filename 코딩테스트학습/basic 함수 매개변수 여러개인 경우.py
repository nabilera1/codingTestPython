def add_mul(*args):
    if args[0] == "add":
        result = 0
        for i in args[1:]:
            result = result + i
    elif args[0] == "mul":
        result = 1
        for i in args[1:]:
            result = result * i
    return result


print(add_mul('add', 1, 2, 3))
print(add_mul('add', 1, 2, 3, 4, 5))
