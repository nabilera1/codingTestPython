#5개의 숫자를 입력받아서
#그 중 가장 큰 숫자를 알려주는 프로그램

n=[] #n=list()
for i in range(5):
    num=int(input())
    n.append(num)

print('MAX=',max(n))
# 5
# 33
# 12
# 19
# 7
# MAX= 33