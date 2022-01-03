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


import math
def isprime(num):
    a=2
    while a<=math.sqrt(num):
        if num%a<1:
            return False
        a=a+1
    return num>1
print(isprime(14))
print(isprime(7))


# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# # define a flag variable
# flag = False
#
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
#
# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")