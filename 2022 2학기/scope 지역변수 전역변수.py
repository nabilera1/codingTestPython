a = 10
b = 100


def f1():
    b = 50
    print(b)


def f2(a):
    a = 1


def f3():
    global a
    a = 20


f1()
print(b)
print(a)

f2(a)
print(a)

f3()
print(a)
