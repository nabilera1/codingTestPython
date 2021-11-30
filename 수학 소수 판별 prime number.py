# 소수 판별하기

num = int(input())

if num<=1:
    print('False')
else:
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            print('False')
            break;
        if i==int(num**0.5):
            print('True')


# if num <= 1:
#     print('False')
# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if not num % i: # 나누어지면 소수가 아니므로
#             print('False')
#             exit(0) # 종료
#
#     print('True')