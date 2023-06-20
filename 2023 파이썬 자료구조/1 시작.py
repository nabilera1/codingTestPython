'''
구글 코랩 링크
https://colab.research.google.com/drive/1ouqyG3q92C1d-Dh0ORFXQPnJdtuJGPUf
구글 클래스룸
https://classroom.google.com/c/NTgzNjc4MjI0NzQ1
'''

# 1.1 정수
'''
파이썬에서 정수는 int로 나타내며 immutable형이다.
불편형 객체는 변수와 객체 참조 간에 차이가 없다.
999 정수를 나타내는 데 필요한 바이트 수를 확인해보자.
파이썬 정수 크기는 적어도 32비트이다.
'''

n = 999
print(n.bit_length())


s='11'
print(int(s))
print(int(s,2))
# ctrl + d
# 실행 : shift + f10
# 실행 : ctrl + shift + f10
print(int(s,8))
print(int(s,16))
# 5진수도 될까? 한번 해보자.
print(int(s,5))

# 1.2 부동소수점

