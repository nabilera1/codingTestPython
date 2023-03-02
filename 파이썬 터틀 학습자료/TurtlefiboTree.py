import turtle as t
def drawfib(n, len_ang):
    t.forward(2 * len_ang)
    if n == 0:
        pass
    elif n == 1:
        pass
    else:
        t.left(len_ang)
        drawfib(n - 1, len_ang)
        t.right(2 * len_ang)
        drawfib(n - 2, len_ang)
        t.left(len_ang)
    t.backward(2 * len_ang)
# 6개의 다른 출발 위치
start_points = [[-300, 250], [-150, 250],[-300, 110], [-80, 110],[-300, -150], [50, -150]]

# n은 1 and 6, len_ang은 30.
n = 0
for start_point in start_points:
    x, y = start_point
    n = n + 1
    t.penup()
    t.setpos(x, y)
    t.pendown()
    drawfib(n, 30)

t.done()