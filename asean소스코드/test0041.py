# 함수와 모듈 사용하기

# print("Hello")

# def Hello():
#     print("HELLO KIM")
#
# Hello()

#매개변수를 사용
def HelloName(name):
    print(f'Hello,{name}')

HelloName('KIM')

def HelloMyName(name):
    print('Hello,',name)

HelloName('Nguyen')

# [문제]
# 자신의 취미를 출력하는 myHobby함수를 만들고 실행해 보세요.
# 매개변수명은 hobby이다.
def myHobby(hobby):
    print('제 취미는',hobby)

myHobby('soccer')
