import random

# 2차원 리스트 생성
rows = 5
cols = 3
a = [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]
print(a)

mlist = []
for row in a:
    m = 0
    for i in row:
        if m < i:
            m = i
    mlist.append(m)

print(*mlist)


import numpy

print(numpy.random.rand(2,2))

print(numpy.random.random(5))