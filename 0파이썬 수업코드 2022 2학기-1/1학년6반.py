def add_mul(*args):
    if args[0] == 'add':
        r = 0
        for i in args:
            r = r + i
    elif args[0] == 'mul':
        r = 1
        for i in args:
            r = r * i
    return r

print(add_mul('add', 1, 2, 3))
print(add_mul('add', 1, 2, 3, 4, 5))

