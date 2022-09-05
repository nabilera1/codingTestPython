#[레이아웃 관리자로 위젯 배치하기]
# pack(), grid(), place()에 대해 알아봅니다.
# pack()은 왼쪽, 오른쪽, 위쪽, 아래쪽 위치로 제한된
# 수평 및 수직 상자에 위젯을 구성합니다.
# 각 상자는 서로에 대해 상대적입니다.

# grid()는 행, 열 절대 좌표를 사용하여
# 2차원 그리드에서 버튼, 레이블 위젯을 배치합니다.
from tkinter import *
w = Tk()
Label(text="1", width=20).grid(row=0, column=0)
Label(text="2", width=20).grid(row=0, column=1)
Label(text="3", width=20).grid(row=1, column=0)
Label(text="4", width=20).grid(row=1, column=1)
w.mainloop()