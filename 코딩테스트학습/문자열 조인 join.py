# mydata = ['Hello,', 'I', 'like', 'Python', 'Coding']
#
# lst = list(map(lambda x: x.replace('Coding', 'Programming'), mydata))
#
# print(lst)
# lst = ' '.join(lst)
# print(lst)
mydata = ['Hello,', 'I', 'like', 'Python', 'Coding']

lst = list(map(lambda x: x.replace('Coding', 'Programming'), mydata))

print(lst)
lst = '\n'.join(lst)
print(lst)
