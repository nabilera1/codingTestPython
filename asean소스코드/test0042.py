#함수 리턴
import random

def weather(n):
    if n==1:
        result="rainy"
    elif n==2:
        result="sunny"
    else:
        result="cloudy"
    return result

# print(weather(4))
n=random.randint(1,3)
input("엔터를 치면 오늘의 날씨를 알려줍니다.")
print(weather(n))