import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(600,700)

polygon = turtle.Turtle()

side = 10
sidel = 67
angle = 360 / side

for i in range(side):
    polygon.forward(sidel)
    polygon.right(angle)
    polygon.forward(sidel)
    polygon.right(angle)
    polygon.forward(sidel)
    polygon.right(angle)
    polygon.forward(sidel)
    polygon.right(angle)

turtle.done