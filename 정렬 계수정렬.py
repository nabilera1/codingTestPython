#모든 원소의 값이 0이상의 정수일 때 아래 숫자를 정렬하는 코드를 작성하시오.
#입력 값 : 4,8,9,3,4,1,6,0,3,0,4,11
arr=list(map(int,input().split(",")))
count=[0]*(max(arr)+1)
for i in range(len(arr)):
    count[arr[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')#i의 개수만큼 출력

