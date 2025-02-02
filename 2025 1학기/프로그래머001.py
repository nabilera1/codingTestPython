arr = ['kim', 'lee', 'park']
h = [hash(a) for a in arr]
# [8283863236792511116, 209450324113990952, -423284808961452044]
print(h)
# 다시 실행하면 숫자 바뀜
# [-1672065755567859576, -3102698606479065750, -6837217048672855572]

answer = ''
temp = 0
dic = {}
arr2 = ['kim', 'park']
for part in arr:
    dic[hash(part)] = part
    temp += int(hash(part))
for com in arr2:
    temp -= hash(com)
answer = dic[temp]

print(answer)


print(arr.count('kim'))

from collections import Counter
inter = (Counter(arr) - Counter(arr2)).elements()
print(inter)
print(list(inter))
print(type(inter))
print(list(inter))