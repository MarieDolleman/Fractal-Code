
# Original code found at https://gist.github.com/thr0wn/f80eb02b3e25742aece046f075bb0370

import turtle
import math

def mandelbrot(z , c , n=20):
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return mandelbrot((16 * z) + (6.08 * z) + c, c, n - 1) 
    else:
        return (0.0016 * (z ** 2)) + (0.0608 * z) + c

# screen size (in pixels)
screenx, screeny = 800, 600

# complex plane limits
complexPlaneX, complexPlaneY = (-2.0, 2.0), (-1.0, 2.0)

# discretization step
step = 5

# turtle config
turtle.tracer(0, 0)
turtle.setup(screenx, screeny)
turtle.bgcolor("#ffffff")
screen = turtle.Screen()
screen.title("Mandelbrot Fractal (discretization step = %d)" % (int(step)))
mTurtle = turtle.Turtle()
mTurtle.penup()
mTurtle.shape("arrow")

# px * pixelToX = x in complex plane coordinates
pixelToX, pixelToY = (complexPlaneX[1] - complexPlaneX[0])/screenx, (complexPlaneY[1] - complexPlaneY[0])/screeny

# plot
for px in range(int(-screenx/2), int(screenx/2), int(step)):
    for py in range(int(-screeny/2), int(screeny/2), int(step)):
        x, y = px * pixelToX, py * pixelToY
        m =  mandelbrot(0, x + 1 * y)
        if not math.isnan(m.real):
            color = [abs(m.imag) for i in range(3)]
            mTurtle.color(color)
            mTurtle.dot(2.4, color)
            mTurtle.goto(px, py)
    turtle.update()

turtle.mainloop()