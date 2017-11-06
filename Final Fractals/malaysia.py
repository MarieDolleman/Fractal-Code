
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
        myTurtle.left(72)
    if letter == 'c':
        myTurtle.left(-108)
    if letter == 'd':
        myTurtle.right(120)
    # first and third bend
    if letter == 'e':
        # 72 - (18 * 2) at l2
        e = 72 - (18 * 2 * (layer - 1))
        myTurtle.left(e)
    # middle bend
    if letter == 'f':
        # 180 - (18+36) at l2
        f = 180 - ((18 * (layer - 1)) + 36)
        myTurtle.right(f)
    if letter == 'i':
        myTurtle.left(84)
    # triangle level 2
    if letter == 'g':
        # 180 - (18 * 5) + 60 at l2
        g = 180 - ((18 * 2 * (layer + 1)) + 60)
        myTurtle.right(156)


ts.exitonclick()