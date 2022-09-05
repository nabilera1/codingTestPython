#입력을 2개 받아 연산하기

#흔히 하는 실수에 대하여
# a=input() #5 문자열
# b=input() #3
# print(a+b) #53 ?? 문자열

#문자열을 숫자로 변환 : int()함수
a=int(input())
b=int(input())
print(a+b)
print("몫 :",a//b)
print("나머지 :",a%b)

print("몫 :",a//b,"나머지 :",a%b)