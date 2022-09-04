'''
참고
https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html
numpy.cumsum(a, axis=None, dtype=None, out=None)[source]
Return the cumulative sum of the elements along a given axis.
누적합
'''

import numpy as np

a = np.array(([1, 2, 3],
              [4, 5, 6]))
print(a)
print(a.shape)  # (2, 3)

print(a[0])  # [1,2,3]
print(a[-1])  # [4 5 6]
print(np.cumsum(a))  # 누적합 구하기
# [ 1  3  6 10 15 21]
print(np.cumsum(a).shape)  # (6,)

print(np.cumsum(a))  # 누적합 구하기
# [ 1  3  6 10 15 21]
print(a.cumsum())  # 누적합 구하기, 위와 동일함.
# [ 1  3  6 10 15 21]

print(np.cumsum(a, dtype=float))
# [ 1.  3.  6. 10. 15. 21.]

# 3개의 열 각각에 대한 행의 누적합 구하기
# axis=0, axis=1에 대한 이해 필요
print(np.cumsum(a, axis=0))
# [[1 2 3]
#  [5 7 9]]
# 각 열에 대한 누적합이 구해짐.

print(np.cumsum(a, axis=1))
# [[ 1  3  6]
#  [ 4  9 15]]
# 원 데이터 a와 비교해 보세요.

