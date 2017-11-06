

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
        myTurtle.forward(40)
    if letter == 'b':
        # powered coeff
        myTurtle.left(-114)
    if letter == 'c':
        myTurtle.left(66)
    if letter == 'd':
        myTurtle.right(120)
    # first and third bend
    if letter == 'e':
        myTurtle.left(48)
        #myTurtle.left(150)
        #myTurtle.pencolor('blue')
    # middle bend
    if letter == 'f':
        myTurtle.right(132)
        #myTurtle.left(30)
        #myTurtle.pencolor('red')
    if letter == 'i':
        myTurtle.left(42)
    # triangle level 2
    if letter == 'g':
        myTurtle.right(156)
        #myTurtle.left(0)
        #myTurtle.pencolor('yellow')

#myTurtle.right(80)
#myTurtle.forward(100)

ts.exitonclick()

