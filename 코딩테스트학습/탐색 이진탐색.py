

#재귀함수
def binary_search_recur(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid] > target:
        return binary_search_recur(array, target, start, mid-1)
    else:
        return binary_search_recur(array, target, mid+1, end)

n,target=10,7
array = [1,3,5,7,9,11,13,15,17,19]
result = binary_search_recur(array, target, 0,n-1)
if result==None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


'''
# 반복문
def binary_search_iter(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end = mid -1
        else:
            start = mid + 1
    return None

n,target=10,7
array = [1,3,5,7,9,11,13,15,17,19]
result = binary_search_iter(array, target, 0,n-1)
if result==None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

재귀함수의 방식 : 종료조건으로 start > end 추가
반복문의 방식 : start <= end동안만 탐색하도록 함

'''