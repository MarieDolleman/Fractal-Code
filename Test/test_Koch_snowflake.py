import turtle

myTurtle = turtle.Turtle()
myTurtle.hideturtle()
#myTurtle.setx(-360)
#myTurtle.sety(-34)
ts = turtle.Screen()
print(myTurtle.position())
print(ts.window_width())
print(ts.window_height())
myTurtle.speed(0)
#original_shape(100, "a", 256, 5, myTurtle)


# a = -
# b = angle leftwards

instructions = ['acaca']
for depth in range(5):
    for index, letter in enumerate(instructions):
        if letter == 'a':
            instructions[index] = list('abacaba')
    flattened_instructions = [item for sublist in instructions for item in sublist]
    instructions = flattened_instructions

for letter in flattened_instructions:
    if letter == 'a':
        myTurtle.forward(5)
    if letter == 'b':
        myTurtle.left(60)
    if letter == 'c':
        myTurtle.left(-120)


ts.exitonclick()