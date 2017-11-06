
import turtle

# three terms in model, so we start with triangle
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
ts = turtle.Screen()
myTurtle.speed(10)

instructions = ['a', 'd', 'a', 'd', 'a']
layer = 3
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

    flattened_instructions = [
        item for sublist in instructions for item in sublist]
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
        e = 180 - (114 + (2 * 9 * (layer - 1)))
        myTurtle.left(e)
        print('e', e)
        # myTurtle.left(48)
    # middle bend
    if letter == 'f':
        f = 180 - (66 - (2 * 9 * (layer - 1)))
        myTurtle.right(f)
        print('f', f)
        # myTurtle.right(132)
    if letter == 'i':
        myTurtle.left(102)
    # triangle level 2
    if letter == 'g':
        # Only valid for layer 3
        myTurtle.left(42)
print(layer)

ts.exitonclick()
