# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# i = 0
# # draw a star
# turtle.done()


# import turtle
#
# t = turtle.Turtle()
# t.shape('turtle')  # 터틀 모듈의 커서를 거북이 모양으로 설정
#
# # 별 모양을 그리기 위한 루프
# for i in range(5):
#     t.forward(100)  # 100 픽셀만큼 직진
#     t.right(144)    # 오른쪽으로 144도 회전
#
# turtle.done()  # 그림 그리기 완료


import turtle

t = turtle.Turtle()
t.shape('turtle')  # 터틀 모양을 거북이로 설정

# 색상 설정: 선 색과 채우기 색
t.color('red', 'yellow')  # 선은 빨간색, 채우기는 노란색

t.begin_fill()  # 채우기 시작

# 별 모양을 그리기 위한 루프
for i in range(5):
    t.forward(100)  # 100 픽셀만큼 직진
    t.right(144)    # 오른쪽으로 144도 회전

t.end_fill()  # 채우기 완료

turtle.done()  # 그림 그리기 완료