#이분탐색
#자료는 정렬이 되어 있어야 한다.

def binary_search(target, data):
    data.sort()
    start=0
    end=len(data)-1
    while(start<=end):
        mid=(start+end)//2
        if data[mid]==target:
            return mid
        elif data[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

if __name__=="__main__":
    li=[i**2 for i in range(11)]
    target=9
    idx=binary_search(target,li)
    if idx:
        print('index=',idx,',value=',li[idx])
    else:
        print("No target")
