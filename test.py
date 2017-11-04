import turtle

# three terms in model, so we start with triangle
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
ts = turtle.Screen()
print(myTurtle.position())
print(ts.window_width())
print(ts.window_height())
myTurtle.speed(3)

myTurtle.forward(40)
myTurtle.left(90)
myTurtle.forward(40)
myTurtle.right(90)
myTurtle.forward(40)
myTurtle.right(298.5)
myTurtle.forward(40)
#myTurtle.right(306)
myTurtle.forward(40)

ts.exitonclick()