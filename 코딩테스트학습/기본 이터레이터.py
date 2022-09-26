li =[1,2,3,4]
lii = iter(li)
print(type(lii)) # <class 'list_iterator'>
for i in range(len(li)):
    print(lii.__next__(), end=' ')

