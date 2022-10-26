import numpy as np

arr = np.arange(12)
print(arr) # <class 'numpy.ndarray'>, 벡터
print(type(arr))
arr += 1
#벡터화 연산, 반복문을 사용한 듯한 효과
print(arr)

# [ 0  1  2  3  4  5  6  7  8  9 10 11]
# <class 'numpy.ndarray'>
# [ 1  2  3  4  5  6  7  8  9 10 11 12]



mask = np.ones(len(arr), dtype=bool) #1값에 True
# mask = np.ones(shape=(len(arr),), dtype=bool)
print(mask) # <class 'numpy.ndarray'>
# [ True  True  True  True  True  True  True  True  True  True  True  True]
mask[[0, 2, 4]] = False
print(mask)
# [False  True False  True False  True  True  True  True  True  True  True]
# result = arr[mask, ...] # ... ellipsis 생략, 때로는 pass와 같은 용도
result = arr[mask]
print(result)
# [ 2  4  6  7  8  9 10 11 12]

