import numpy as np

#zeros
print('********** zeros **************')
arr=np.zeros(shape=(10,), dtype=np.int8)
print(arr, arr.size, arr.shape, arr.ndim, arr.dtype)
#[0 0 0 0 0 0 0 0 0 0] 10 (10,) 1 int8
arr=np.zeros(shape=(5), dtype=np.int32)
print(arr, arr.size, arr.shape , arr.ndim,arr.dtype)
#[0 0 0 0 0] 5 (5,) 1 int32

#ones
print('********** ones **************')
arr=np.ones(shape=(10,), dtype=np.int8)
print(arr, arr.size, arr.shape, arr.ndim,  arr.dtype)

arr=np.ones(shape=(5,2)) #np.ones((5,2))
print(arr, arr.size, arr.shape, arr.ndim, arr.dtype)

#empty
print('********** empty **************')
arr=np.empty(shape=(10,), dtype=np.int8) #현 시점 쓰레기값이 아닌 숫자가 나옴
print(arr, arr.size, arr.shape, arr.ndim, arr.dtype)

arr=np.empty(shape=(5,2))
print(arr, arr.size, arr.shape ,arr.ndim, arr.dtype)

# ____like
print('********** ones_like **************')
arr=np.ones_like(np.arange(10).reshape(-1,2))
print(arr, arr.size, arr.shape ,arr.dtype)
print('********** empty_like **************')
print(np.empty_like(arr)) #현 시점 쓰레기값이 아닌 숫자가 나옴

