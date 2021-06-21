dict={}
dict['a']='apple'
dict['b']='banana'
dict['c']='cocoa'
print(dict)
print(dict['a'])
dict['a']=5
print('a' in dict)
print(dict['a'])
if 'a' in dict:
    print(dict['b'])
print(dict.get('a'))

for key in dict:
    print(key)
print(dict.keys())
print(dict.values())

for key in sorted(dict.keys()):
    print(key, dict[key])