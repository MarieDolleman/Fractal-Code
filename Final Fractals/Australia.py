
import turtle

# three terms in model, so we start with triangle
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
ts = turtle.Screen()
print(myTurtle.position())
print(ts.window_width())
print(ts.window_height())
myTurtle.speed(3)

instructions = ['a']
final_instructions = []
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
            instructions[index] = 'g'
        elif letter == 'g':
            instructions[index] = 'h'
        elif letter == 'h':
            instructions[index] = 'g'
        else:
            raise RuntimeError('Letter \'%s\' not defined in rules' % letter)
    flattened_instructions = [item for sublist in instructions for item in sublist]
    instructions = flattened_instructions
final_instructions += instructions

print(flattened_instructions)
#ne = list('abacaba')
one_side = ['a', 'b', 'a', 'c', 'a', 'b', 'a', 'e', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'f', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'e', 'a', 'b', 'a', 'c', 'a', 'b', 'a']
base = ['a', 'b', 'a', 'c', 'a', 'b', 'a', 'd', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'd', 'a', 'b', 'a', 'c', 'a', 'b', 'a']
#flattened_instructions = list('abacabaeabacabafabacabaeabacabagabacabaeabacabafabacabaeabacabagabacabaeabacabafabacabaeabacabag')
flattened_instructions = [  'a', 'b', 'a', 'c', 'a', 'b', 'a', 'e', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'f', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'e', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'g',
                            'a', 'b', 'a', 'c', 'a', 'b', 'a', 'e', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'f', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'e', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'g',
                            'a', 'b', 'a', 'c', 'a', 'b', 'a', 'e', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'f', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'e', 'a', 'b', 'a', 'c', 'a', 'b', 'a']
layers = [flattened_instructions]
size = 100
colors = ['yellow', 'blue']
n = 0
for l in layers:
    for letter in l:
        if letter == 'a':
            myTurtle.forward(size)
        if letter == 'b':
            # powered coeff
            myTurtle.left(153)
        if letter == 'c':
            # -140
            myTurtle.left(-27)
        # make it a triangle
        if letter == 'd':
            myTurtle.right(159)
            #myTurtle.pencolor(colors[0+n])
            n += 1
        # tight corner
        if letter == 'e':
            myTurtle.right(126)
        # middle turn
        if letter == 'f':
            myTurtle.left(54)
        # around the triangle
        if letter == 'g':
            g = (159 + (139.5 * layer)) - 360 
            myTurtle.right(g)
        if letter == 'h':
            h = (159 + (139.5 * layer)) - 360
            myTurtle.left(h)
            #myTurtle.pencolor(colors[0+n])
            n += 1

    #size = 20


ts.exitonclick()
