#완전수 구하기
#6은 1,2,3이 약수,
#자신을 제외한 약수의 합이 자신이 되는 수
def isPerfect(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n / i
        i += 1
    return (True if sum == n and n != 1 else False)

print("Below are all perfect numbers till 10000")
n = 2
for n in range(10000):
    if isPerfect(n):
        print(n, " is a perfect number")
