# https://www.unioviedo.es/compnum/labs/new/04_Non_lin_eq2.html

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

# f = lambda x: np.sin(x) - 0.1 * x - 0.1
# df = lambda x: np.cos(x) - 0.1
# x = np.linspace(-1, 20, 1000)
#
# plt.figure(figsize=(10, 4))d
# plt.plot(x, f(x))
# plt.plot(x, 0 * x, 'k-')
# plt.show()


x = np.linspace(2.0, 3.0, num=5)
print(type(x))
print(x.shape)
plt.plot(x, 0 * x, 'k-') #black -
plt.plot(x, 1*x, 'g--') #green 점선
plt.show()


# https://matplotlib.org/2.0.2/api/pyplot_api.html
# [‘solid’ | ‘dashed’, ‘dashdot’, ‘dotted’ | (offset, on-off-dash-seq)
# | '-' | '--' | '-.' | ':' | 'None' | ' ' | '']