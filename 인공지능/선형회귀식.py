import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array([1,2,3,4,5,6,7]).reshape(-1, 1)
y = np.array([1,3,5,9,15,20,26]).reshape(-1, 1)
model = LinearRegression().fit(x, y)
plt.scatter(x, y)
plt.xlabel('number of exercises')#운동 횟수
plt.ylabel('happy hormone amount')#행복 호르몬 양
b0 = model.intercept_[0] #절편
print(b0)
b1 = model.coef_[0][0] #기울기
print(b1)
print(b1.ndim)
print(b1.shape)
plt.plot(x, b0 + b1*x, 'r' ) #그래프 그리기
plt.show()