import tkinter as tk
import random
import math

def rotate_squares():
    global angle

    # canvas에서 이전 사각형 지우기
    canvas.delete("square")

    # 각 사각형에 대해 새로운 좌표 계산 및 그리기
    for cx, cy in centers:
        rad = math.radians(angle)
        new_coords = []
        for x, y in square_coords:
            new_x = cx + x * math.cos(rad) - y * math.sin(rad)
            new_y = cy + x * math.sin(rad) + y * math.cos(rad)
            new_coords.append((new_x, new_y))

        # 사각형 그리기
        canvas.create_polygon(new_coords, fill="blue", tags="square")

    angle += 5  # 각도를 5도씩 증가
    root.after(50, rotate_squares)

def move_ball():
    global ball_dx, ball_dy

    # 공 이동
    canvas.move(ball, ball_dx, ball_dy)

    # 공의 현재 위치 가져오기
    ball_coords = canvas.coords(ball)
    ball_x1, ball_y1, ball_x2, ball_y2 = ball_coords

    # 벽 충돌 체크 (캔버스 경계)
    if ball_x1 <= 0 or ball_x2 >= 400:
        ball_dx = -ball_dx
    if ball_y1 <= 0 or ball_y2 >= 400:
        ball_dy = -ball_dy

    # 사각형과 충돌 체크
    for rect_id in rectangles:
        rect_coords = canvas.coords(rect_id)
        if (ball_x2 > rect_coords[0] and ball_x1 < rect_coords[2] and
            ball_y2 > rect_coords[1] and ball_y1 < rect_coords[3]):
            ball_dx = -ball_dx
            ball_dy = -ball_dy

    # 반복 호출
    root.after(20, move_ball)

def start_ball_movement(event):
    global ball_dx, ball_dy
    ball_dx = random.choice([-3, 3])
    ball_dy = random.choice([-3, 3])

# GUI 초기화
root = tk.Tk()
root.title("Rotating Squares and Ball Physics")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# 사각형 생성
rectangles = []
centers = [
    (100, 100),
    (300, 100),
    (300, 300),
    (100, 300)
]
size = 40  # 사각형 한 변의 절반 길이
square_coords = [
    (-size, -size),
    (size, -size),
    (size, size),
    (-size, size),
]
for cx, cy in centers:
    rect = canvas.create_rectangle(
        cx - size, cy - size, cx + size, cy + size, fill="blue"
    )
    rectangles.append(rect)

# 공 생성
ball = canvas.create_oval(190, 190, 210, 210, fill="red")
ball_dx, ball_dy = 0, 0  # 공의 초기 이동 방향

# 초기 각도 설정
angle = 0

# 키보드 이벤트 바인딩
root.bind("<space>", start_ball_movement)

# 사각형 회전 시작
rotate_squares()

# 공 이동 시작
move_ball()

# 메인 루프 실행
root.mainloop()
