# mydata = ['Hello,', 'I', 'like', 'Python', 'Coding']
#
# lst = list(map(lambda x: x.replace('Coding', 'Programming'), mydata))
#
# print(lst)
# lst = ' '.join(lst)
# print(lst)
mydata = ['Hello,', 'I', 'like', 'Python', 'Coding']
print(f'(1) :{mydata}')

lst = list(map(lambda x: x.replace('Coding', 'Programming'), mydata))

print(lst)
lst = '\n'.join(lst)
print(lst)

# 차이점 이해하기
mydata1 = 'Hello,' + ' I' + ' like' + ' Python' + ' Coding'
temp = str(mydata1)
print(f'(1-1) : {temp}')
aa = temp.replace('Coding', 'Programming')
print(f'(1-2) : {aa}')

print(f'(2) :{mydata1}')
mydata2 = ' '.join(mydata1)
print(f'(3) :{mydata2}')
lst = list(map(lambda x: x.replace('Coding', 'Programming'), mydata))
# 그냥 문자열 전체에서 replace할 것 변환해도 될 듯.
print(lst)
lst = '\n'.join(lst)
print(lst)
