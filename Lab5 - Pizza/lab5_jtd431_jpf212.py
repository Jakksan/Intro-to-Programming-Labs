# Imports everything necessary for the program
from turtle import *
from random import uniform
from math import *
from time import sleep

# Speed things a bit
speed(0)

# Setup the screensize and create a variable that is our originself.
screensize(600, 600)

# Draw the crust
pencolor("darkred") # simulate pizza sauce

# This is used in several places throughout the code, it sets the radius of the crust
outerCrustRadius = 300

# The circle function starts drawing at the very bottom of the circle
# We move move the pen to the negative radius so the center of the circle will be at (0,0)
penup()
goto(0, (-outerCrustRadius))
pendown()

# Draw the pizza crust circle
begin_fill()
fillcolor("tan1")
circle(outerCrustRadius)
end_fill()

# Draw the cheese circle inside of the crust circle
innerCrustRadius = outerCrustRadius - 40
penup()
goto(0, (-innerCrustRadius))
pendown()
begin_fill()
fillcolor("lemonchiffon")
circle(innerCrustRadius)
end_fill()

# Outline the pepperonis in dark red
pencolor("darkred")

# Draw range(x) amount of pepperonis
for pepperoni in range(20): # draw some pepperonis

    # Each pepperoni has a radius of 30
    pepperoniRadius = 30

    # Go the center of the pizza
    penup()
    goto(0,0)

    # Set a random orientation and move a random distance forward
    randomDistance = uniform(0, (innerCrustRadius - pepperoniRadius*2))
    randomHeading = uniform(0, 360)
    setheading(randomHeading)
    forward(randomDistance)

    # Draw the pepperoni circle
    pendown()
    begin_fill()
    fillcolor("red")
    circle(pepperoniRadius)
    end_fill()


# Draw mushroomTotal mushrooms
mushroomTotal = 8
for mushroom in range(mushroomTotal):

    # Set the cap radius to 30, this will be used for drawing the mushroom
    capRadius = 60

    # Set the amount the mushrooms should be rotated each time
    angleChange = 360/mushroomTotal
    angleChange = angleChange * mushroom

    # Go to (0, 0)
    penup()
    goto(0,0)

    setheading(angleChange)
    forward(150)

    # Draw the mushroom
    pendown()
    begin_fill()
    fillcolor("beige")
    circle(capRadius, 180)
    left(90)
    forward(capRadius/2)
    right(90)
    forward(capRadius/2)
    left(90)
    forward(capRadius)
    left(90)
    forward(capRadius/2)
    right(90)
    forward(capRadius/2)

    end_fill()


# Slice the pizza into segments
pencolor("darkred")
penup()
goto(0, (-outerCrustRadius))
pendown()
setheading(0)

# Move in short increments of a circle and intermidently draw lines
for slice in range(8):
	circle(outerCrustRadius, 45)
	turtlePos = pos()
	setpos(0, 0)
	setpos(turtlePos)

input()
