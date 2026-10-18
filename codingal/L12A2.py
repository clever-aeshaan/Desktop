import turtle

turtle.Screen().bgcolor("red")
turtle.Screen().setup(500,600)

star = turtle.Turtle()
star.pencolor("green")

star.forward(100)
star.left(120)
star.forward(100)
star.left(120)
star.forward(100)
star.left(120)

star.penup()
star.right(120)
star.forward(50)
star.pendown()

star.forward(100)
star.right(120)
star.forward(100)
star.right(120)
star.forward(100)

turtle.done()