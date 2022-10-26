print(...)  # Ellipsis 생략
print(type(...))  # <class 'ellipsis'>


def Hello():
    ...


def Hello1():
    print('Hello 1번')


print(Hello()) # None
Hello() # 출력없음
Hello1() # Hello 1번

n: tuple[int, ...] # n은 정수값만 가지는 튜플, 어노테이션
n = 1, 2
print(type(n))
print(n)

# 허용
n = ()
print(n)
n = (1,)
print(n)

# 오류, 파이참에서는 오류 없이 변환하여 출력됨
n = (1, 'a') # 문자가 나와서 오류
print(n)

n = [1, 2, 3]
print(n) # 튜플이 아니어서 오류
