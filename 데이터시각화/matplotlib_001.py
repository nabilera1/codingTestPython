# matplotlib 라이브러리 사용하기
# import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[2,4,6,8]
# plt.plot(x,y)
# plt.show()
# ctrl + / 가 주석처리 동작이 안되면 한국어 Microsoft 입력기로 바꿀 것.

#축 레이블과 그래프 제목 작성하기
# import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[2,4,6,8]
# plt.plot(x,y)
# plt.title("My graph")
# plt.xlabel("Time")
# plt.ylabel("Score")
# plt.show()

# # 그림 저장하기
# import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[2,4,6,8]
# plt.plot(x,y)
# plt.title("My graph")
# plt.xlabel("Time")
# plt.ylabel("Score")
# plt.savefig("My Score.png")
# # 소스코드와 같은 폴더에 저장
# plt.show()

'''
==========
plot(x, y)
==========

See `~matplotlib.axes.Axes.plot`.
The NumPy linspace function (sometimes called np. linspace)
is a tool in Python for creating numeric sequences.
It's somewhat similar to the NumPy arange function
'''


import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery') #격자 표시

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

