#정수 정렬
#5 7 3 9 0 4 1
# arr=list(map(int,input().split(" ")))
arr=map(int,input().split(" "))
# print(list(arr))
sort_arr=sorted(arr)
for i in range(len(sort_arr)):
    print(sort_arr[i], end=' ')