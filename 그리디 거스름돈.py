#500, 100, 50, 10원 동전 무한히 존재
#손님에게 줘야할 돈이 N일 때, 최소 동전의 개수
#단, N은 10의 배수

# 거스름돈 문제는 최적의 해를 구하기 위해 큰 단위 돈부터 거슬러주면 된다.
n=int(input()) # 돈 입력
coins=[500,100,50,10]
cnt=0
for coin in coins:
    cnt+=int(n/coin) #1260  500 500
    print(coin,':',n//coin)
    n%=coin
print(cnt)
#사용한 동전의 개수
#1260
#500: 2
#100: 2
#50: 1
#10: 1
#6