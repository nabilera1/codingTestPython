li =[1,2,3,4]
lii = iter(li)
print(type(lii)) # <class 'list_iterator'>
# for i in range(len(li)):
#     print(lii.__next__(), end=' ')
# 매직 메소드 사용  __next__

for i in range(len(li)):
    print(next(lii))   #위의 코드 실행하면 더 이상 동작안됨.

