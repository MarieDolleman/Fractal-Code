
import turtle

def original_shape(step, rule, angle, depth, t):
    t.forward(step)
    t.left(120)
    t.forward(step)
    t.left(120)
    t.forward(step)
    #fractal(step, rule, angle, depth, t)

def fractal(step, rule, angle, depth, t):
    if depth > 0:
        a = lambda: fractal(step, "a", angle, depth - 1, t)
        b = lambda: fractal(step, "b", angle, depth - 1, t)
        left = lambda: t.left(angle)
        right = lambda: t.right(608)
        forward = lambda: t.forward(step)
        #back = lambda: t.back(step)
        if rule == "a":
            forward();
        if rule == "b":
            a(); 

# three terms in model, so we start with triangle
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
myTurtle.setx(-360)
ts = turtle.Screen()
print(myTurtle.position())
print(ts.window_width())
print(ts.window_height())
myTurtle.speed(0)
#original_shape(100, "a", 256, 5, myTurtle)


# a = -
# b = angle leftwards

instructions = ['a']
for depth in range(5):
    for index, letter in enumerate(instructions):
        if letter == 'a':
            instructions[index] = list('abacaba')
    flattened_instructions = [item for sublist in instructions for item in sublist]
    instructions = flattened_instructions

for letter in flattened_instructions:
    if letter == 'a':
        myTurtle.forward(10)
    if letter == 'b':
        myTurtle.left(60)
    if letter == 'c':
        myTurtle.left(-120)


ts.exitonclick()