from turtle import *
import math
import time


def drawTriangle(x, y, tri_base, tri_height, color):
    # Calculate all the measurements and angles needed to draw the triangle
    side_length = math.sqrt((0.5*tri_base)**2 + tri_height**2)
    base_angle = math.degrees(math.atan(tri_height/(tri_base/2)))
    top_angle = 180 - (2 * base_angle)

    # Lift pen to prevent stray lines
    penup()

    # Go to some x and y coordinates
    goto(x, y)
    setheading(0)

    # Fill the triangle with some color
    fillcolor(color)
    begin_fill()
    pendown()

    # Draw the triangle
    forward(tri_base)
    left(180 - base_angle)
    forward(side_length)
    left(180 - top_angle)
    forward(side_length)

    # Stop filling and lift pen
    end_fill()
    penup()



def drawRectangle(x, y, rec_width, rect_height, color):


    # Lift pen to prevent stray lines
    penup()

    # Go to some x and y coordinates
    goto(x, y)
    setheading(0)

    # Set fill color, put pen back onto canvas
    pendown()
    fillcolor(color)
    begin_fill()

    # Draw the rectangle
    for side in range(2):
        forward(rec_width)
        left(90)
        forward(rect_height)
        left(90)

    # Stop filling and lift pen
    end_fill()
    penup()



def drawCircle(x, y, radius, color):

    # Lift pen to prevent stray lines
    penup()

    # Go to some x and y coordinates
    goto(x, y)
    setheading(0)
    setpos(x, (y-radius))

    # Put pen down, then start filling
    pendown()
    fillcolor(color)
    begin_fill()

    # Draw the circle
    circle(radius)

    # Stop filling and lift pen
    end_fill()
    penup()


# drawTriangle(60, 60, 25, 40, "blue")
# drawTriangle(100, -100, 70, 20, "pink")
#
# drawRectangle(60, -60, 60, 40, "yellow")
# drawRectangle(-100, 100, 25, 60, "green")
#
# drawCircle(-60, 60, 15, "green")
# drawCircle(150, 120, 30, "purple")

input()
