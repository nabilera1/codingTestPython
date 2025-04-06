import tkinter as tk
import math

def rotate_squares():
    global angle

    # canvas에서 이전 사각형 지우기
    canvas.delete("square")

    # 각 사각형에 대해 새로운 좌표 계산 및 그리기
    for i, (cx, cy) in enumerate(centers):
        rad = math.radians(angle + i * 90)  # 각 사각형은 90도 차이를 둠
        new_coords = []
        for x, y in square_coords:
            new_x = cx + (x - cx) * math.cos(rad) - (y - cy) * math.sin(rad)
            new_y = cy + (x - cx) * math.sin(rad) + (y - cy) * math.cos(rad)
            new_coords.append((new_x, new_y))

        # 사각형 그리기
        canvas.create_polygon(new_coords, fill="blue", tags="square")

    # 각도 증가 및 반복 호출
    angle += 5  # 5도씩 회전
    root.after(50, rotate_squares)  # 50ms마다 반복

# GUI 초기화
root = tk.Tk()
root.title("Rotating Squares")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# 사각형 중심 좌표 및 초기 사각형 좌표 설정
centers = [
    (150, 150),
    (160, 160),
    (170, 170),
    (180, 180)
]
size = 20  # 사각형 한 변의 길이
square_coords = [
    (-size, -size),
    (size, -size),
    (size, size),
    (-size, size),
]

# 초기 각도 설정
angle = 0

# 회전 시작
rotate_squares()

# 메인 루프 실행
root.mainloop()
