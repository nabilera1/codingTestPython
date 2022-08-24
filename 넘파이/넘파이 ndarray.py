import numpy as np

li = [1, 2, 3, 4, 5, 6, 7]
arr = np.array(li)
print('1)', arr)
print(type(arr))
arr = np.array(li, float)
print('2)', arr)
print(type(arr))
# arr = np.array([1, 'k', "t", 3], float)

# li = [1, 'a', True, [3, 4, 5]]
# print(li)
# arr = np.array(li, dtype=object)
# print(arr)


# '''
# C:\Users\user\PycharmProjects\codingTestPython\넘파이\넘파이 ndarray.py:13: VisibleDeprecationWarning:
# Creating an ndarray from ragged nested sequences
# (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated.
# If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
#   arr=np.array(li)
# '''