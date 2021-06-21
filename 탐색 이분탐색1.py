target = 56
li = [30, 94, 56, 87, 34, 25, 64]
l = len(li)
# li.sort()
li = sorted(li)
print(li)
left = 0
right = l - 1
while left <= right:
    mid = (left + right) // 2
    if li[mid] == target:
        print(mid + 1, '번 째 있음')
        break
    elif li[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

if(left>right):
    print("No target")