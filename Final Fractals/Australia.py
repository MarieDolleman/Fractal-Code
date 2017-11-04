
import turtle

# three terms in model, so we start with triangle
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
ts = turtle.Screen()

myTurtle.speed(10)

instructions = ['a', 'd', 'a', 'd', 'a']
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
        elif letter == 'h':
            instructions[index] = 'g'
        elif letter == 'e' or 'f':
            continue
        else:
            raise RuntimeError('Letter \'%s\' not defined in rules' % letter)
    flattened_instructions = [item for sublist in instructions for item in sublist]
    instructions = flattened_instructions

print(instructions)
size = 100
for letter in instructions:
        if letter == 'a':
            myTurtle.forward(100)
        elif letter == 'b':
            # powered coeff
            myTurtle.left(153)
        elif letter == 'c':
            myTurtle.left(-27)
        # make it a triangle
        elif letter == 'd':
            myTurtle.right(120)
        elif letter == 'i':
            myTurtle.right(159)
        # tight corner
        elif letter == 'e':
            myTurtle.right(126)
        # middle turn
        elif letter == 'f':
            myTurtle.left(54)
        # around the triangle
        elif letter == 'g':
            g = (159 + (139.5 * layer)) - 360
            if layer == 2:
                assert (g == 78)
            myTurtle.right(78)
        elif letter == 'h':
            h = (159 + (139.5 * layer)) - 360
            h = 180 - (h % 180)
            if layer == 3:
                print(h)
                assert (h == 142.5)
            myTurtle.right(h)
            myTurtle.pencolor('red')
        else:
            raise RuntimeError('Letter \'%s\' not defined in instructions' % letter)

    #size = 20


ts.exitonclick()
