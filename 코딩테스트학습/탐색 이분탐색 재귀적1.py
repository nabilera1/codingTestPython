#에러 처리 필요

def binarySearch(li, target, left, right):
    mid = (left+right)//2
    # print(mid)
    m = li[mid]
    if target == m:
        return mid
    elif m > target:
        binarySearch(li, target, left, mid - 1)
    elif m < target:
        binarySearch(li, target, mid + 1, right)
    else: 
        return False

target = 250
myList = [30, 14, 27, 92, 21, 37, 25, 47]
length = len(myList)

myList.sort()
left = 0 
right = length-1
print(myList)
sol=binarySearch(myList, target, 0, right)
print(sol)
if(sol):
    print('{}번째 있음'.format(sol+1))