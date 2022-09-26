l1 = [1, 2, 3, 4, 5, 6, 3, 4, 5]
s1 = set(l1)
l2 = [4, 5, 6, 3, 4, 5, 6, 7]
s2 = set(l2)
# 교집합, intersection, &
print(s1 & s2)
print(s1.intersection(s2))

# 합집합, union, |
print(s1 | s2)

# 차집합, difference, -
print(s1 - s2)

print(s1)
s1.add(7)
print(s1)

s1.update([7, 8, 9])
print(s1)

s1.remove(2)
print(s1)

s1.discard(7)
print(s1)
#
# s1.clear()
#
# del s1
