import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# x1 =[1, 2, 3, 4, 5, 6, 7]
# print(x1.shape)
# AttributeError: 'list' object has no attribute 'shape'

# x1 = np.array([1, 2, 3, 4], [5, 6, 7])
# print(x1.shape)
# TypeError: Field elements must be 2- or 3-tuples, got '5'

# 운동 횟수, <class 'numpy.ndarray'>
x1 = np.array([1, 2, 3, 4, 5, 6, 7])
print(x1.shape)
# 행복 호르몬 양
y1 = np.array([1, 3, 5, 9, 15, 20, 26])
print(type(x1))
plt.scatter(x1, y1)
plt.show()

'''
# x , <class 'numpy.ndarray'>
x = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
print(x.shape) #(7, 1)
y = np.array([1, 3, 5, 9, 15, 20, 26]).reshape(-1, 1)
model = LinearRegression().fit(x, y)
plt.scatter(x, y)
plt.xlabel('number of exercises')  # 운동 횟수
plt.ylabel('happy hormone amount')  # 행복 호르몬 양
b0 = model.intercept_[0]  # 절편
print(b0) # -5.71428571428571
b1 = model.coef_[0][0]  # 기울기
print(b1)
print(b1.ndim) # 0
print(b1.shape) # ()
plt.plot(x, b0 + b1 * x, 'r')  # 그래프 그리기
plt.show()
'''
