import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# 풍차 날개 그리기
def draw_windmill(ax, angle):
    ax.clear() # 축 내용 지우기, 이전 그래프를 지우는 역할
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal') # 'equal' box
    #ax.axis('off')

    # 풍차 날개 설정
    for i in range(4):
        rad = np.radians(angle + i * 90)
        x = np.cos(rad)
        y = np.sin(rad)
        ax.plot([0, x], [0, y], lw=4)  # 날개


# 애니메이션 업데이트 함수
def update(fr):
    angle = fr * 10  # 각 프레임마다 10도씩 회전
    draw_windmill(ax, angle)


fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=200)
plt.show()
