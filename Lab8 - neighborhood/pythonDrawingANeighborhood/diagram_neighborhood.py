from turtle import *
import math
import time

setup(1000,1000)
goto(0,0)
penup()

def drawTriangle(x, y, tri_base, tri_height, color):

    # Calculate all the measurements and angles needed to draw the triangle
    side_length = math.sqrt((0.5*tri_base)**2 + tri_height**2)
    base_angle = math.degrees(math.atan(tri_height/(tri_base/2)))
    top_angle = 180 - (2 * base_angle)

    # Draw the triangle using the calculations from above
    penup()
    goto(x, y)
    pendown()
    setheading(0)

    fillcolor(color)
    begin_fill()

    forward(tri_base)
    left(180 - base_angle)
    forward(side_length)
    left(180 - top_angle)
    forward(side_length)

    end_fill()
    penup()

def drawRectangle(x, y, rec_width, rect_height, color):
    penup()
    goto(x, y)

    pendown()
    setheading(0)

    fillcolor(color)
    begin_fill()

    for each in range(2):
        forward(rec_width)
        left(90)
        forward(rect_height)
        left(90)

    end_fill()

    penup()

def drawCircle(x, y, radius, color):
    penup()

    setheading(0)
    setpos(x, (y-radius))

    pendown()

    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

    penup()

def drawTree(x, y, tree_height, color):


    drawRectangle((x-(tree_height * 0.1)), y, (tree_height * 0.2), tree_height * 0.5, "sandy brown")

    drawCircle(x, (y + (tree_height * 0.75)), (tree_height * 0.25), color)

def drawHouse(x, y, house_width, house_height, primary_color, secondary_color):

    # Define some variables that will be useful for house construction
    roof_height = house_height * 0.2
    building_height = house_height * 0.8

    # Draw building
    drawRectangle(x, y, house_width, building_height, primary_color)

    # create variables needed for drawing the door
    door_width = house_width / 8
    door_height = house_height / 4

    # Draw door
    door_x = x+(house_width * 0.75)
    door_y = y
    drawRectangle(door_x, door_y, door_width, door_height, "brown")
    drawCircle(door_x + door_width*3/4, door_y + door_height/2, 3, "gold")

    # Draw roof
    overhang = 20
    drawTriangle(x-(overhang / 2), (y + building_height), (house_width + overhang), roof_height, secondary_color)

    # Draw window
    window_size = building_height / 2
    window_x = (x+(house_width * 0.2))
    window_y = y + (building_height / 3)
    drawRectangle(window_x, window_y, window_size, window_size/2, "light blue")

    # Draw the window sections
    goto(window_x + window_size/2, window_y)
    pendown()
    goto(window_x + window_size/2, window_y + window_size/2)
    penup()
    goto(window_x, window_y + window_size/4)
    pendown()
    goto(window_x + window_size, window_y + window_size/4)

    penup()

def drawPumpkin(x, y, radius):
    drawRectangle(x, y+radius-3, radius/4, radius/2, "orange")
    begin_fill()
    fillcolor("white")
    drawCircle(x, y, radius)
    end_fill()

def drawTownSign(x, y, text):
    letters = len(list(text))
    sign_width = (letters*10)+10

    # Draw the rectangular feet of the sign
    drawRectangle((x+sign_width/2-5), y, 10, 75, "brown")
    drawRectangle((x-sign_width/2-5), y, 10, 75, "brown")


    if letters < 10:
        sign_width = 120

    drawRectangle(x-(0.5*sign_width), y+15, sign_width, 60, "light grey")

    setpos(x, y+50)
    write("Welcome to", align="center", font=("Monaco", 12, "normal"))
    setpos(x, y+20)
    write(text, align="center", font=("Monaco", 12, "normal"))


drawRectangle(-300, 250, 40, 80, "light grey")

drawTriangle(-250, 250, 40, 40, "light blue")
#
drawCircle(-180, 270, 20, "pink")
#
drawTree(-150, 230, 70, "green")

input()
