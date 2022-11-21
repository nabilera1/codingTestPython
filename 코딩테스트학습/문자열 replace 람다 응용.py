# 리스트의 내용을 바로 변경해보자.
mydata = ['Hello,', 'I', 'like', 'Python', 'Coding']

lst = list(map(lambda x: x.replace('Coding', 'Programming'), mydata))

print(lst)
lst = ' '.join(lst)
print(lst)
