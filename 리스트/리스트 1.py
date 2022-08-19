li = []
li.append('BTS')
li.append('Black Pink')
print(li)
# 가수 세 명을 입력 받기
for i in range(0, 3, 1):
    li.append(input('가수 이름을 쓰세요 : '))

print('-' * 20)
print(li)
print(len(li), '개')
# print(f'리스트 개수 {len(li)}개 입니다.')
print('5번째', li[4])
print('6번째 %s' % li[5])
