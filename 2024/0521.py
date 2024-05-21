plus = lambda x, y: x + y
print(plus(3, 5))


def plus1(x, y):
    return x + y


print(plus1(3, 5))

print((lambda x, y: x + y)(3, 5))  # 8이 나온다.

my_fn = lambda x, a, b=7: a * x + b
print(my_fn(4, 2, 7))
print(my_fn(4, 2))

li = [1, 2, 4, 6, 8, 11, 19]
squares = map(lambda x: x * x, li)
print(squares)
print(list(squares))

li = [1, 2, 4, 6, 8, 11, 19]
squares = list(map(lambda x: x * x, li))
print(squares)  # [1, 4, 16, 36, 64, 121, 361]

arr = [3, 5, 6, 8]
print(list(filter(lambda a: a > 5, arr)))  # [6,8]
print(list(filter(lambda a: a % 2 == 1, arr)))  # [3,5]
