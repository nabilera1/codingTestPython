'''
matplotlib.pyplot 모듈의 text() 함수는 그래프의 적절한 위치에 텍스트를 삽입하도록 합니다.

text() 함수를 사용해서 그래프 영역에 텍스트를 삽입하고, 다양하게 꾸미는 방법에 대해 소개합니다.

'''

import matplotlib.pyplot as plt
import numpy as np

a = 2.0 * np.random.randn(10000) + 1.0
#a는 표준편차 2.0, 평균 1.0을 갖는 정규분포
b = np.random.standard_normal(10000)+3
#b는 표준정규분포

c = 20.0 * np.random.rand(5000) - 10.0
#c는 -10.0에서 10.0 사이의 균일한 분포를 갖는 5000개의 임의의 값

plt.hist(a, bins=100, density=True, alpha=0.7, histtype='step')#stepfilled
plt.text(1.0, 0.35, '2.0*np.random.randn(10000)+1.0')
plt.hist(b, bins=50, density=True, alpha=0.5, histtype='step')
plt.text(2.0, 0.20, 'np.random.standard_normal(10000)')
plt.hist(c, bins=100, density=True, alpha=0.9, histtype='step')
plt.text(5.0, 0.08, 'np.random.rand(5000)-10.0')
plt.show()


#내 블로그 검색하면 설명이 나옴.
