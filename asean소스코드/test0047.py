# [문제]
# 간단한 주사위 만들기
#
# 엔터키를 누르면 주사위 숫자가 나옵니다.
# 5
# 엔터키를 누르면 종료합니다.

# import random
# input('엔터키를 누르면 주사위 숫자가 나옵니다.')
# print(random.randint(1,6))
# input('엔터키를 누르면 종료합니다.')

# from random import randint
# input('엔터키를 누르면 주사위 숫자가 나옵니다.')
# print(randint(1,6))
# input('엔터키를 누르면 종료합니다.')

# [문제]
# 엔터키를 누를 때 마다 임의의 주사위 숫자가
# 나오는 프로그램을 만들어보시오.
# 총 반복횟수는 5회로 한다.
from random import randint

for i in range(5):
    input('엔터키를 누르세요')
    print(str(i + 1), '번 째 :', randint(1, 6))
