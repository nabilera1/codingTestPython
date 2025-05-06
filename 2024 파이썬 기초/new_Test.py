arr1 = [[10,20,30],[40, 50, 60]]
arr2 = []

for e in arr1:
    arr2.append(e)
print(arr1)
arr2[0][0] = 100
arr1[1][0] = 200

print(arr2)
print(arr1)
print(arr1[0][0] + arr2[1][0])




