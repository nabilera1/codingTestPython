# 나선형 나선 패턴

import turtle
loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
	turtle.circle(5*i)#양의 반지름
	turtle.circle(-5*i)#음의 반지름
	turtle.left(i)

turtle.exitonclick()
