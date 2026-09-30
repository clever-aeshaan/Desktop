import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(600,700)
square = turtle.Turtle()

sides=4
sidel = 67
angle = 360 / sides

for i in range(sides):
    square.forward(sidel)
    square.left(angle)

turtle.done