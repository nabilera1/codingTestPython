#filter(function, iterator)
#map과 filter

def is_even(x):
    if x%2==0:
        return True
    return False

arr1=[]
for val in range(1,11):
    if is_even(val):
        arr1.append(val)
print(f'arr1 function : {arr1}')

arr2=list(filter(is_even,range(1,11)))
print(f'arr2 function : {arr2}')

arr3=list(filter(lambda n:n%2!=0, range(1,11)))
print(f'arr3 function : {arr3}')
