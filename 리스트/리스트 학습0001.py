'''
#짝수 리스트 출력하기
even_numbers = []
for n in range(1, 10 + 1):
    if n % 2 == 0:
        even_numbers.append(n)

print(even_numbers)

# 다음 문장 차이 이해하기
e = [n for i in range(1, 11) if i % 2 == 0]
#NameError: name 'n' is not defined
print(e)

e = [i for i in range(1, 11) if i % 2 == 0]
print(e)

e = [n for n in range(1, 11) if n % 2 == 0]
print(e)

e = [n*2 for n in range(1, 11) if n % 2 == 0]
print(e)

e = [[n]*2 for n in range(1, 11) if n % 2 == 0]
print(e)



'''

# print([(x, z, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피'] for z in ['배달 시키기', '가서 먹기']])
#
#
# for x in ['쌈밥', '치킨', '피자']:
#     for y in ['사과', '아이스크림', '커피']:
#         for z in ['배달 시키기', '가서 먹기']:
#             print(x, z, y)
e = [n for i in range(1, 11) if i % 2 == 0]
print(e)

e = [i for i in range(1, 11) if i % 2 == 0]
print(e)

e = [n for n in range(1, 11) if n % 2 == 0]
print(e)

e = [n*2 for n in range(1, 11) if n % 2 == 0]
print(e)

e = [[n]*2 for n in range(1, 11) if n % 2 == 0]
print(e)