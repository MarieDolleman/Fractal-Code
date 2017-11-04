
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
layer = 2
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
        elif letter == 'g':
            instructions[index] = 'h'

    flattened_instructions = [item for sublist in instructions for item in sublist]
    instructions = flattened_instructions

print(instructions)
for letter in instructions:
    if letter == 'a':
        myTurtle.forward(10)
    if letter == 'b':
        # powered coeff
        myTurtle.left(66)
    if letter == 'c':
        myTurtle.left(-114)
    if letter == 'd':
        myTurtle.right(120)
    # first and third bend
    if letter == 'e':
        myTurtle.left(48)
    if letter == 'f':
        myTurtle.right(132)
    if letter == 'i':
        myTurtle.left(102)
    if letter == 'g':
        g = 180 - ((9 * 2 * layer) + 60)
        myTurtle.left(g)
    if letter == 'h':
        g = 180 - ((18 * layer) + 60)
        myTurtle.left(g)


ts.exitonclick()
