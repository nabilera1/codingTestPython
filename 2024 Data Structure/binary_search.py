def b_search(arr, n):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1

arr = [1,2,3,4,5,6,7,8,9]
n = 4
print(b_search(arr,n))