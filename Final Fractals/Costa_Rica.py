
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


    flattened_instructions = [item for sublist in instructions for item in sublist]
    instructions = flattened_instructions

print(instructions)
for letter in instructions:
    if letter == 'a':
        myTurtle.forward(10)
    if letter == 'b':
        # powered coeff
        myTurtle.left(72)
    if letter == 'c':
        myTurtle.left(-108)
    if letter == 'd':
        myTurtle.right(120)
    # first and third bend
    if letter == 'e':
        myTurtle.left(32)
    # middle bend
    if letter == 'f':
        myTurtle.right(126)
    if letter == 'i':
        myTurtle.left(84)
    # triangle level 2
    if letter == 'g':
        myTurtle.left(38)


ts.exitonclick()