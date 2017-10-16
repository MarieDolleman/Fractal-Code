
import turtle

def malaysia(step, rule, angle, depth, t):
    if depth > 0:
        a = lambda: malaysia(step, "a", angle, depth - 1, t)
        b = lambda: malaysia(step, "b", angle, depth - 1, t)
        left = lambda: t.left(angle)
        right = lambda: t.right(608)
        forward = lambda: t.forward(step)
        #back = lambda: t.back(step)
        if rule == "a":
            for i in range(16):
                left(); forward(); b(); left; forward(); #back
        if rule == "b":
            for i in range(6):
                left(); forward(); a(); left; forward();

myTurtle = turtle.Turtle()
myTurtle.speed(0)
malaysia(10, "a", 256, 5, myTurtle)