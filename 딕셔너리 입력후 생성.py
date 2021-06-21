d = {1: "one", 2: "two"}

d.clear()
print('d =', d)
#d = {}
original = {1:'one', 2:'two'}
new = original.copy()

print('Orignal: ', original)
print('New: ', new)
# Orignal:  {1: 'one', 2: 'two'}
# New:  {1: 'one', 2: 'two'}

#딕셔너피 카피와 = 연산차의 차이
original = {1:'one', 2:'two'}
new = original

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)
# new:  {}
# original:  {}

original = {1:'one', 2:'two'}
new = original.copy()

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)
# new:  {}
# original:  {1: 'one', 2: 'two'}