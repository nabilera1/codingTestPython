#
# # 1차 회귀식
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = [1, 3, 6, 8, 11, 15, 20, 24, 28]
#
# print(np.polyfit(x, y, 1))
#
# coef, intercept = np.polyfit(x, y, 1)
#
# y_pred = np.array(x) * coef + intercept
#
# plt.figure(figsize=(10, 20))
# plt.plot(x, y_pred, color='b', label='Goal')
#
# plt.text(5, 22, f'coef :{coef}')
# plt.text(5, 23, f'intercept:{intercept}')
# plt.legend()
# plt.scatter(x, y, c='r')
# plt.show()


#2차 회귀식
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 3, 6, 8, 11, 15, 20, 24, 28]
poly = np.polyfit(x, y, 2) # 2차, 1차, 상수항 계수
print(type(poly)) #<class 'numpy.ndarray'>
X_ = np.linspace(1, 9, 100) # 100을 넣어 곡선 완만하게 그리기
print(X_.shape, type(X_))
y_pred = X_ ** 2 * poly[0] + X_ * poly[1] + poly[2]

plt.plot(X_, y_pred, color ='b')
plt.scatter(x, y, color = 'r')
plt.show()
