

import turtle

# three terms in model, so we start with triangle
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
ts = turtle.Screen()
print(myTurtle.position())
print(ts.window_width())
print(ts.window_height())
myTurtle.speed(10)

instructions = ['a','d','a','d','a']
layer = 4
for depth in range(layer):
    for index, letter in enumerate(instructions):
        if letter == 'a':
            instructions[index] = list('abacaba')
        elif letter == 'b':
            instructions[index] = 'e'
        elif letter == 'c':
            instructions[index] = 'f'
        elif letter == 'd':
            instructions[index] = 'i'
        elif letter == 'i':
            instructions[index] = 'g'

    flattened_instructions = [item for sublist in instructions for item in sublist]
    instructions = flattened_instructions

print(instructions)
for letter in instructions:
    if letter == 'a':
        myTurtle.forward(10)
    if letter == 'b':
        # powered coeff
        myTurtle.left(45)
    if letter == 'c':
        myTurtle.left(-135)
    if letter == 'd':
        myTurtle.right(120)
    # first and third bend
    if letter == 'e':
        e = 180 - (135 - (2 * 22.5 * (layer - 1)))
        myTurtle.left(e)
    # middle bend
    if letter == 'f':
        f = 180 - (45 + (2 * 22.5 * (layer - 1)))
        myTurtle.right(f)
    # triangle
    if letter == 'i':
        myTurtle.right(75)
    # triangle level 2
    if letter == 'g':
        g = 180 - (60 + (2 * 22.5 * (layer - 1)))
        myTurtle.right(g)
ts.exitonclick()