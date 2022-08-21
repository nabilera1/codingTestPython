
#1차 회귀식
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5, 6]
# y = [1, 3, 6, 8, 11, 19]
#
# print(np.polyfit(x, y, 1))
#
# coef, intercept = np.polyfit(x, y, 1)
#
# y_pred = np.array(x) * coef + intercept
#
# plt.figure(figsize=(4, 9))
# plt.plot(x, y_pred, color='b')
#
# plt.scatter(x, y, c='r')
# plt.show()


#2차 회귀식
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 3, 6, 8, 11, 19]
poly = np.polyfit(x, y, 2) # 2차, 1차, 상수항 계수가 순서대로 들어있는 배열
X = np.linspace(1, 6, 100) # 곡선을 완만하게 그리기 위한 linspace 객체 선언
print(X.shape, type(X))
y_pred = X ** 2 * poly[0] + X * poly[1] + poly[2]

plt.plot(X, y_pred, color ='b')
plt.scatter(x, y, color = 'r')
plt.show()
