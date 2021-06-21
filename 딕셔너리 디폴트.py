#https://medium.com/swlh/python-collections-defaultdict-dictionary-with-default-values-and-automatic-keys-305540540d2a
# So What exactly is DefaultDict?
# defaultdict is a dict for all practical purpose.
# You don’t need to learn new syntax
# or understand anything special to start using dict.
#일반적인 경우
# dct={}
# #v1=dct['a1'] #keyError : 'a1'
# if  'a1' not in dct:
#     print("1. key error")
# try:
#     v1=dct['a1']
# except KeyError:
#     print("2. key error")
# dct.update({'a1':50})
# print(dct)
# dct.update({'a2':60})
# print(dct)
# try:
#     v1=dct['a1']
#     print(v1)
# except KeyError:
#     print("2. key error")

from collections import defaultdict
dct=defaultdict(lambda :100)
v1=dct['a1']
print(v1)
