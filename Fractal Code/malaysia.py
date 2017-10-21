
import turtle

# three terms in model, so we start with triangle
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
#myTurtle.setx(-360)
#myTurtle.sety(-34)
ts = turtle.Screen()
print(myTurtle.position())
print(ts.window_width())
print(ts.window_height())
myTurtle.speed(0)

instructions = ['ababa']
for depth in range(5):
    for index, letter in enumerate(instructions):
        if letter == 'a':
            instructions[index] = list('abacaba')
    flattened_instructions = [item for sublist in instructions for item in sublist]
    instructions = flattened_instructions

for letter in flattened_instructions:
    if letter == 'a':
        myTurtle.forward(20)
    if letter == 'b':
        # powered coeff
        myTurtle.left(80)
    if letter == 'c':
        # -140
        myTurtle.left(-140)


ts.exitonclick()
