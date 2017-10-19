import turtle

def koch(t, order, step):
    if order == 0:
        t.forward(step)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, int(step/3))
            t.left(angle)

# three terms in model, so we start with triangle
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
ts = turtle.Screen()
myTurtle.speed(0)
koch(myTurtle, 10, 20)
print(myTurtle.position())
ts.exitonclick()
