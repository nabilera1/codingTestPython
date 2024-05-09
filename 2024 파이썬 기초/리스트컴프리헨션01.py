n = [i for i in range(10)]
print(n)

n = []
for i in range(0, 10):
    n.append(i)
print(n)

print([2*x for x in range(1, 11)])


print([2*i for i in range(1,11) if i])

print('=' * 40)
a = [20, 40, 50, 45, 80]
print(sum([i for i in a if i >= 50]))
