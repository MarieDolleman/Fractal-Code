
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

    flattened_instructions = [item for sublist in instructions for item in sublist]
    instructions = flattened_instructions

print(instructions)
for letter in instructions:
    if letter == 'a':
        myTurtle.forward(10)
    if letter == 'b':
        # powered coeff
        myTurtle.left(54)
    if letter == 'c':
        myTurtle.left(-126)
    if letter == 'd':
        myTurtle.right(120)
    # first and third bend
    if letter == 'e':
        e = 180 - (126 - (2 * 9 * (layer - 1)))
        #myTurtle.left(72)
        print('e', e)
        myTurtle.left(e)
    # middle bend
    if letter == 'f':
        f = 180 - (54 + (2 * 9 * (layer - 1)) + 6)
        #myTurtle.right(102)
        myTurtle.right(f)
        print('f', f)
    if letter == 'i':
        myTurtle.right(102)
    # triangle level 2
    if letter == 'g':
        g = 180 - (60 + (2 * 9 * layer) - 6)
        print('g', g)
        #myTurtle.right(90)
        myTurtle.right(g)


ts.exitonclick()

