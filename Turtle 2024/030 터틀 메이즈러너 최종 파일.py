# https://chatgpt.com/c/126393e6-f1fb-4356-aa60-50b5386b06cc

import turtle

def draw_road():
    # 도로의 양쪽 선을 그립니다.
    turtle.penup()
    turtle.pensize(10)  # 도로 선의 두께
    turtle.pencolor('black')  # 도로 선의 색

    # 왼쪽 선 그리기
    turtle.goto(-100, -200)
    turtle.pendown()
    turtle.left(90)  # 위로 그리기
    turtle.forward(400)
    turtle.penup()

    # 오른쪽 선 그리기
    turtle.goto(100, -200)
    turtle.pendown()
    turtle.forward(400)
    turtle.penup()

def turn_left():
    # 왼쪽으로 30도 회전
    turtle.left(30)

def turn_right():
    # 오른쪽으로 30도 회전
    turtle.right(30)

def drive():
    # 앞으로 20만큼 이동하기 전 충돌 검사
    x_position = turtle.xcor()  # 현재 x 좌표
    if -90 < x_position < 90:
        turtle.forward(20)
    else:
        print("충돌!")
        # 충돌 시, 거북이를 중간으로 되돌림
        turtle.goto(0, turtle.ycor())

def setup():
    screen = turtle.Screen()
    screen.title('Turtle Road Runner')

    draw_road()  # 도로 그리기

    turtle.shape('turtle')
    turtle.shapesize(1.5)
    turtle.color('green')
    turtle.speed('normal')

    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(drive, "Up")
    screen.listen()

    turtle.penup()
    turtle.goto(0, 0)  # 시작 위치는 중앙
    turtle.setheading(90)  # 북쪽을 바라보도록 초기 방향 설정
    turtle.pendown()

setup()
turtle.mainloop()
