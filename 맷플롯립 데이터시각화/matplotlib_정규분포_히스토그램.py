'''
normal(loc=0.0, scale=1.0, size=None)

Draw random samples from a normal (Gaussian) distribution.
The probability density function of the normal distribution,
first derived by De Moivre and 200 years later by both Gauss and
Laplace independently [2], is often called the bell curve because of
its characteristic shape (see the example below).
The normal distributions occurs often in nature.
For example, it describes the commonly occurring distribution of
samples influenced by a large number of tiny,
random disturbances, each with its own unique distribution
'''
# 평균 0, 표준편차 10, 데이터개수 100개인 랜덤 값을 히스트로그램으로 나타내기

import numpy as np
# import random
import matplotlib.pyplot as plt

data = np.random.normal(0, 10, 100)
print(data)
m = data.mean()
print(m)


plt.text(14, 14, 'mean=' + '%.2f' % m)
plt.hist(data, bins=10, label='random.normal')
plt.legend()
plt.show()
