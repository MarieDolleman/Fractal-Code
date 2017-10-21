
import turtle

# three terms in model, so we start with triangle
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
#myTurtle.setx(-360)
#myTurtle.sety(-50)
ts = turtle.Screen()
print(myTurtle.position())
print(ts.window_width())
print(ts.window_height())
myTurtle.speed(0)

instructions = ['ababa']
for depth in range(5):
    for index, letter in enumerate(instructions):
        if letter == 'a':
            instructions[index] = list('abacafafacaba')
    flattened_instructions = [item for sublist in instructions for item in sublist]
    instructions = flattened_instructions

for letter in flattened_instructions:
    if letter == 'a':
        myTurtle.forward(5)
    if letter == 'b':
        # powered coeff
        myTurtle.left(-148)
    if letter == 'c':
        # -140
        myTurtle.left(36)
    
    #if letter == 'd':
        #myTurtle.left(6)

    #if letter == 'e':
        #myTurtle.left(4)

    if letter == 'f':
        myTurtle.left(84)
    


ts.exitonclick()
