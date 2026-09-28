import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)

polygon = turtle.Turtle()

side = 67
sidel = 67
angle = 360 / side

for i in range(side):
    polygon.forward(sidel)
    polygon.right(angle)

turtle.done