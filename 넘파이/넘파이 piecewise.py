'''
numpy.piecewise
numpy.piecewise(x, condlist, funclist, *args, **kw)
Evaluate a piecewise-defined function.

Given a set of conditions and corresponding functions,
evaluate each function on the input data
wherever its condition is true.

'''
# (Python) Numpy piecewise , linspace, arange 비교 학습
# https://blog.naver.com/nabilera1/222861521972
import numpy as np

# x = np.linspace(-2.5, 2.5, 6)
# print(x)
x = np.linspace(-5, 5, 11)
print(x)
# Define the sigma function, which is -1 for x < 0 and +1 for x >= 0.
print(np.piecewise(x, [x < 0, x >= 0], [-1, 1]))

# Define the absolute value, which is -x for x <0 and x for x >= 0.
f = np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])
print(f, type(f))

y = -2 #스칼라 값에 적용해보기기
 print(np.piecewise(y, [y < 0, y >= 0], [lambda x: -x, lambda x: x]))
f = np.piecewise(y, [y < 0, y >= 0], [lambda x: -x, lambda x: x])
print(f, type(f))

# [-5. -4. -3. -2. -1.  0.  1.  2.  3.  4.  5.]
# [-1. -1. -1. -1. -1.  1.  1.  1.  1.  1.  1.]
# [5. 4. 3. 2. 1. 0. 1. 2. 3. 4. 5.] <class 'numpy.ndarray'>
# 2
