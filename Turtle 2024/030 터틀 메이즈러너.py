import turtle

# https://chatgpt.com/c/126393e6-f1fb-4356-aa60-50b5386b06cc

def draw_road():
    # 도로의 경계선을 그립니다.
    road_width = 400
    turtle.speed('fastest')  # 그리기 속도를 가장 빠르게 설정
    turtle.penup()
    turtle.goto(-road_width / 2, -100)  # 도로의 시작점으로 이동
    turtle.pendown()
    turtle.forward(road_width)  # 아래쪽 경계선 그리기
    turtle.penup()
    turtle.goto(-road_width / 2, 100)
    turtle.pendown()
    turtle.forward(road_width)  # 위쪽 경계선 그리기
    turtle.penup()


def turn_left():
    # 왼쪽으로 90도 회전
    turtle.left(90)


def turn_right():
    # 오른쪽으로 90도 회전
    turtle.right(90)


def drive():
    # 앞으로 20만큼 이동
    turtle.forward(20)


def setup():
    # 화면 설정
    screen = turtle.Screen()
    screen.title('Turtle Maze Runner')

    # 도로 그리기
    draw_road()

    # 거북이 설정
    turtle.shape('turtle')
    turtle.shapesize(1.5)
    turtle.color('green')
    turtle.speed('normal')

    # 키보드 컨트롤
    screen.onkey(turn_left, "Left")  # 왼쪽 화살표 키를 누르면 turn_left 호출
    screen.onkey(turn_right, "Right")  # 오른쪽 화살표 키를 누르면 turn_right 호출
    screen.onkey(drive, "Up")  # 위쪽 화살표 키를 누르면 drive 호출
    screen.listen()  # 키보드 입력을 기다립니다.

    turtle.penup()  # 펜을 들어서 이동 시 선을 그리지 않도록 합니다.
    turtle.goto(0, 0)  # 중앙에서 시작
    turtle.pendown()


setup()
turtle.mainloop()  # 이벤트 루프 시작
