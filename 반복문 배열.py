a=[]*6
print(a)
a=[0,2,3,4,5,1]
print(a)
for i in range(1,6):
    a[i]=a[a[i]]
print(a)
for i in range(1,6):
    a[i]=a[a[i]]
print(a)
#인덱스 간접 참조, 어떤 의미
#즉 해당 값 위치로 가라는 의미
# []
# [0, 2, 3, 4, 5, 1]
# [0, 3, 4, 5, 1, 3]
# [0, 5, 1, 3, 5, 3]