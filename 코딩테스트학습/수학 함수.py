import math
n=sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
print(n) #0.9999999999999999
n=math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
print(n)

#math.fsum(iterable)
#이터러블(iterable)에 있는 값의 정확한(accurate) 부동 소수점 합을 반환합니다.
# 여러 중간 부분 합을 추적하여 정밀도 손실을 방지합니다:

print(math.gcd(4, 22))#2
#math.gcd(*integers)
#지정된 정수 인자의 최대 공약수를 반환합니다.
