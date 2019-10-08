from turtle import *
from random import randint, choice
from math import *
from time import *

# Disable animation
tracer(n=0)

# Save the starting time to a variable
start_time = time()

# draw unit circle
penup()
goto(0, -150)
pendown()
circle(150)

# draw box to throw darts in
penup()
goto(-150, -150)
sideLength = 300
pendown()
for side in range(4):
    forward(sideLength)
    left(90)

# Create the variables that keep track of whether or not the dart hit inside of the circle
inside = 0
outside = 0

# throw a large amount of darts
for dart in range(10000000):

    # Find out the width and height of our box, then divide by two so we can use them with the cardesian cooridinates system
    boxSize = int(sideLength / 2)

    # Choose random x and y values that will fall within our window
    xValue = randint(-boxSize, boxSize )
    yValue = randint(-boxSize, boxSize )

    # Move the turtle to somewhere random inside of the window
    penup()
    goto(xValue, yValue)
    pendown()

    # Decide if the dot falls inside of the circle or not
    if sqrt(pow(xValue, 2) + pow(yValue, 2)) > 150:
        color = "red"
        outside = outside + 1
    else:
        color = "blue"
        inside = inside + 1

    # Create a variable that is the sum of the darts inside and outside the circle
    total_dots = inside + outside

    # Draw the darts
    begin_fill()
    pencolor(color)
    fillcolor(color)
    goto(xcor(), ycor()-1)
    circle(.2) # Veeeery small
    end_fill()

    # Display the darts 50 at a time.
    if (dart % 50 == 0):
        update()
        print("Number of Darts:", total_dots)                                   # Print how many darts have been thrown
        print("Darts inside:", inside)                                          # Print how many darts are inside the circle
        print('Approximate Pi: '+ format(((inside / total_dots)*4), ".7f"))     # Print what the program currently thinks pi is
        current_time = time()                                                   # Print the computation line (line below does this)
        print("Computation time: ", format((current_time - start_time), ".3e"), "seconds\n")
