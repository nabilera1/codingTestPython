# 소수 판별하기

num = int(input())

if num<=1:
    print('False')
else:
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            print('False')
            break
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


# # include <stdio.h>
#
# int prime(int n){
#    for (int i=2; i * i <= n;i++){
#       if (n % i == 0)
#          return 0;
#    }
#    return 1;
# }
# int main(){
#     int n;
#     scanf("%d", & n);
#     if (prime(n))
#         printf("True");
#     else
#         printf("False");
#     return 0;
# }
