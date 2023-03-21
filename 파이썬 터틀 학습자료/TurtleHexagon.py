# Python program to draw hexagon
import turtle
poly=turtle.Turtle()

num_sides=6
side_length=70
angle=360.0/num_sides

for i in range(num_sides):
    poly.forward(side_length)
    poly.right(angle)
turtle.done()



