# import turtle
# import time
#
# # 초기 설정
# screen = turtle.Screen()
# screen.title("사각형 그리기와 회전")
# t = turtle.Turtle()
#
# # 사각형 그리기
# for _ in range(4):
#     t.forward(100)  # 한 변의 길이
#     t.right(90)
#
# # 회전 시작
# start_time = time.time()
# while time.time() - start_time < 2:  # 2초 동안 회전
#     t.right(10)  # 작은 각도로 회전
#     time.sleep(0.05)  # 자연스러운 회전 속도 조절
#
# # 프로그램 종료 대기
# turtle.done()


import tkinter as tk
import math

def rotate_square():
    global angle

    # canvas에서 이전 사각형 지우기
    canvas.delete("square")

    # 회전 각도 라디안으로 변환
    rad = math.radians(angle)

    # 중심점을 기준으로 사각형의 새로운 좌표 계산
    new_coords = []
    for x, y in square_coords:
        new_x = center_x + (x - center_x) * math.cos(rad) - (y - center_y) * math.sin(rad)
        new_y = center_y + (x - center_x) * math.sin(rad) + (y - center_y) * math.cos(rad)
        new_coords.append((new_x, new_y))

    # 새 좌표로 사각형 그리기
    canvas.create_polygon(new_coords, fill="blue", tags="square")

    # 각도 증가 및 반복 호출
    angle += 5  # 5도씩 회전
    root.after(50, rotate_square)  # 50ms마다 반복

# GUI 초기화
root = tk.Tk()
root.title("Rotating Square")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# 중심점 및 초기 사각형 좌표 설정
center_x, center_y = 200, 200
size = 50  # 사각형 한 변의 길이
square_coords = [
    (center_x - size, center_y - size),
    (center_x + size, center_y - size),
    (center_x + size, center_y + size),
    (center_x - size, center_y + size),
]

# 초기 각도 설정
angle = 0

# 회전 시작
rotate_square()

# 메인 루프 실행
root.mainloop()