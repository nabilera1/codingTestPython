# 리스트 컴프리헨션
# [ <표현식> for <변수> in <시퀀스>]
# result = []
# for 변수명 in 시퀀스:
#     if 조건:
#         result.append(표현식)
# a = [ x * x for x in s if x > 0 ] # 파이썬
# a = { x^2 | x ∈ s, x > 0 }         # 수학
# https://wikidocs.net/84393

li = [1, 2, 3, 4, 5, 6, 7]
licom = [2 * i for i in li]  # 새 리스트 생성
print(li)
print(licom)
# 리스트 내용을 3배 증가시킨 값들의 총합은?
print(sum([3 * i for i in li]))

# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print([nn for n in range(1,10)])
# nn=[x for x in range(10)]
# print(nn)
# print([x for x in range(10)])

# lst=['Apple','Banana','Orange']
# print([f'{x}s' for x in lst])
print([f'{x}s' for x in ['A','B','C']])