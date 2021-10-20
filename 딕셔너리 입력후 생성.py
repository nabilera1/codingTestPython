# 딕셔너리?
# [키, 값] 쌍을 담아두는 자료구조이다.
# 키는 원소를 찾기 위한 식별자이다.
# 딕셔너리와 해시는
# 유일한 값(반복되지 않는 값)만 저장한다.

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