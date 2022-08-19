# https://super-master.tistory.com/7
'''
piecewise 함수 : piecewise ( 입력배열 'x'  , 조건 , 출력함수 'y(x)' )
파이썬에서는 piecewise 라는 함수를 이용하면 손쉽게 조건부함수를 만들 수 있다.
numpy 라이브러리에 있는 함수라서 수치데이터를 입력받고 수치데이터로 출력할 수 있다.
https://numpy.org/doc/stable/reference/generated/numpy.piecewise.html


'''
import numpy as np

x = np.linspace(-2.5, 2.5, 6)
# Define the sigma function, which is -1 for x < 0 and +1 for x >= 0.
result1 = np.piecewise(x, [x < 0, x >= 0], [-1, 1])

# Define the absolute value, which is -x for x <0 and x for x >= 0.
result2 = np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])

# Apply the same function to a scalar value.
y = -2
result3 = np.piecewise(y, [y < 0, y >= 0], [lambda x: -x, lambda x: x])

# piecewise 를 이용해 어떤 점을 기준으로 기울기가 변하는 직선을 그리게 하려면
# result4 = np.piecewise(x, [x < x0, x >= x0],
#                        [lambda x: s1 * x - s1 * x0 + y0, lambda x: s2 * x - s2 * x0 + y0])
print(f'result1={result1}')
print(f'result2={result2}')
print(f'result3={result3}, type={type(result3)}')
# print(f'result4={result4}')
