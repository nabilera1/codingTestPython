import turtle


def draw_wall():
    # 벽을 그립니다.
    turtle.penup()
    turtle.goto(-50, -200)  # 벽의 시작 위치
    turtle.pendown()
    turtle.pensize(20)  # 벽의 두께
    turtle.pencolor('black')  # 벽의 색
    turtle.left(90)  # 세로로 그리기
    turtle.forward(400)  # 벽의 길이
    turtle.penup()


def turn_left():
    turtle.left(90)


def turn_right():
    turtle.right(90)


def drive():
    # 충돌 감지
    if -70 <= turtle.xcor() <= -30:
        print("충돌!")
        return
    turtle.forward(20)


def setup():
    screen = turtle.Screen()
    screen.title('Turtle Maze Runner')

    # 벽 그리기
    draw_wall()

    # 거북이 설정
    turtle.shape('turtle')
    turtle.shapesize(1.5)
    turtle.color('green')
    turtle.speed('normal')

    # 키보드 컨트롤
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(drive, "Up")
    screen.listen()

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


setup()
turtle.mainloop()
