'''
[미션]
아래 단계대로 실행하여 결과를 보여주시오.

빈 리스트 arr을 생성한다.
‘대구’를 입력받아 arr에 넣는다.
‘부산’,’서울’을 차례대로 입력 받아 arr에 넣는다.

arr에 있는 내용을 차례대로 출력한다.
'''

arr=list()
print(type(arr))
print(arr)

# arr.append()
data=input().split()
# data=map(int, input().split())
arr.extend(data)
print(arr)
print(*arr)
for i in arr:
    print(i, end=' ')
