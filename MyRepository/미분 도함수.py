'''
미분계수는 y=f(x) 의 x=a에서의 접선의 기울기를 의미하는 것이고
도함수는 한 점을 정하지 않고 즉 x좌표가 x인 점에서의 접선의 기울기를 의미합니다.

Python에서 미분(차분)
'''

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 2 * np.pi, 0.1)  # 시간 축 0에 2pi 범위
y1 = np.sin(t)  # 사인함수

plt.figure(figsize=(12, 6))
plt.plot(t, y1)
plt.show()


# 사인 곡선이 보임.

def derivative(f, a, h=0.01):
    return (f(a + h) - f(a))/ h


# https://pinkwink.kr/1233
# math.ubc.ca

dy1dx = derivative(np.sin, t)

plt.figure(figsize=(12, 5))
plt.plot(t, dy1dx, 'r.', label='Calculated Difference')
plt.plot(t, np.cos(t), 'b', label='True Value')
plt.plot(t, y1, 'k', label='Original Value')
plt.legend(loc='best')
plt.show()

#derivative 함수를 이용해서 원함수 y1과 미분한 함수와 sin을 미분하면 cos인걸 아니까 그걸 비교