# while True:
#     a=input('Y/N : ')
#     if a=='Y' or a=='y':
#         print("다시 시작합니다.")
#     else:
#         print("종료합니다.")
#         break

# for i in range(5):
#     print(i, end=' ')
# print()
# for i in range(1,5):
#     print(i, end=' ')
#
# print()
# for i in range(1,9,2):
#     print(i, end=' ')
# color=['red','orange','yellow']
# for i in color:
#     print(i, end=' ')

# 문제)
# 1에서 100까지의 총합을 구하는 프로그램을 만드시오.
# 1에서 100까지의 총합= 5050
sum=0
for i in range(1,101):
    sum+=i
print('1에서 100까지의 총합=',sum)