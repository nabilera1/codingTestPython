k = ('key1', 'key2', 'key3')
v = (1,2,3)
dct1 = dict.fromkeys(k, v)
print(dct1)
# {'key1': (1, 2, 3), 'key2': (1, 2, 3), 'key3': (1, 2, 3)}

k = ['key1', 'key2', 'key3']
v = 1
dct1 = dict.fromkeys(k, v)
print(dct1)