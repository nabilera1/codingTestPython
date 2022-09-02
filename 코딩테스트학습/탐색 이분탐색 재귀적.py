def binary_search(target, start, end, li):
    if start > end:
        return None
    mid = (start + end) // 2
    if li[mid] == target:
        return mid
    elif li[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(target, start, end, li)


li = [i * 3 for i in range(11)]
target = 66
idx = binary_search(target, 0, 10, li)
print(li)
if (str(idx).isdigit()):
    print(idx + 1, '번 째 있음')
else:
    print("없음")
