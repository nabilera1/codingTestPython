# https://codetorial.net/numpy/functions/numpy_where.html

'''
numpy.where 함수는

첫번째 인자인 조건식만 주어질 때, 조건에 맞는 요소의 인덱스를 반환합니다.

조건식과 함께 두세번째 인자로 어레이가 함께 주어질 때,
조건식이 참인 경우 두번째 인자의 요소를,
조건식이 거짓인 경우 세번째 인자의 요소를 반환합니다.

'''
# https://colab.research.google.com/drive/1MIA1VhL3ygtw7LihL_BUmXwFzFYhL29w?pli=1&authuser=1#scrollTo=4QmLte-2N-H3

import numpy as np

a = np.array([2, 5, 1, 3, 0])
b = np.where(a < 3)

print(b)  # 어래이 반환 (array([0, 2, 4], dtype=int64),)
print(*b)  # [0 2 4]
print(a[b])  # [2 1 0]
print(a[np.where(a < 3)])  # [2 1 0]

a = np.arange(5)
print(a)  # [0 1 2 3 4]

# b = np.where(a < 3)
b = np.where(a < 3, a, -a)
print(b)  # [ 0  1  2 -3 -4]

c = np.where(a < 3, a, a ** 2)
print(c)  # [ 0  1  2  9 16]
