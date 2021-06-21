# 큰 수 만들기
# 배열의 요소들을 M번 더하여 가장 큰 수를 만들어보자. 이 때 배열의 특정 인덱스가 연속해서 K번 초과할 수는 없다. 하지만 다른 인덱스에 같은 값이 있을 경우는 다르게 처리한다.
#
# 배열 2 4 5 4 6
# M이 8 K가 3이라면
# 6+6+6+5+6+6+6+5=46
#
# 배열 3 4 3 4 3
# M이 7 K 2라면
# 서로 다른 인덱스에 4가 있으므로 계속 사용하면 된다.
# 4+4+4+4+4+4+4=28
#
# 입력
# 5 8 3
# 2 4 5 4 6
# 출력
# 46

#가장 큰 수와 두번째로 큰 수를 저장하여 사용하면 된다.
#
n,m,k=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
first=data[n-1]
second=data[n-2]

result=0
while True:
    for i in range(k):
        if m==0:
            break
        result+=first
        m-=1

    if m==0:
        break
    result+=second
    m-=1

print(result)










# n,m,k=map(int, input().split())
# data=list(map(int, input().split()))
# data.sort()
# first=data[n-1]
# second=data[n-2]
# count=int(m/(k+1))*k
# count+=m%(k+1)
#
# result=0
# result+=(count)*first
# result+=(m-count)*second
# print(result)