# 시간 속의 숫자 찾기 (몇개의 숫자 3이 있나)
# 00시 00분 00초부터 N시 59분 59초까지의 시각 중에서
# 3이 포함된 숫자의 개수 출력 (0<=N<=23)
# 하루는 86,400초 =24*60*60
# 24시 60분 60초
# print(24*60*60)
# brute force 완전 탐색
# 매 시각을 문자열로 바꾼 다음 '3'이 포함되었는지 검사
# 입력 : 5
# 출력 : 11475
# h=int(input())
# count=0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i)+str(j)+str(k):
#                 count+=1
# print(count)
#
# 1 입력시
# 0시 0분 0초 ~ 1시 59분 59초
##########응용 . 총 횟수 구하기

h=int(input())
count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            ss=str(i)+str(j)+str(k)
            if '3' in ss:
                count+=ss.count('3')
print(count)