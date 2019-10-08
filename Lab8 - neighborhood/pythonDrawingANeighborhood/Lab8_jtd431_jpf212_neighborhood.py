from turtle import *
import math
import time

setup(1000,1000)
goto(0,0)
penup()

###########################################
# drawTriangle()
#       Draw a triangle depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# tri_base : int
#     the length of the triangle base
# tri_height : int
#     the height of the triangle
# color : str
#     the color of the triangle
#
# Returns
# -------
# none

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


###########################################
# drawRectangle()
#       Draw a rectangle depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# rec_width : int
#     the length of the rectangle base
# rect_height : int
#     the height of the rectangle
# color : str
#     color of the rectangle
#
# Returns
# -------
# none

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


###########################################
# drawCircle()

#       Draw a circle depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# radius : int
#     radius of the circle
# color : str
#     color of the circle
#
# Returns
# -------
# none

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


###########################################
# drawTree()
#       Draw a tree depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# tree_height : int
#     height of the tree
# color : str
#     color of the canopy of the tree
#
# Returns
# -------
# none

def drawTree(x, y, tree_height, color):

    # Draw the trunk of the tree, it will always be sandy brown
    drawRectangle((x-(tree_height * 0.1)), y, (tree_height * 0.2), tree_height * 0.5, "sandy brown")

    # Draw the leafy part of the tree, make it some color
    drawCircle(x, (y + (tree_height * 0.75) - 10), (tree_height * 0.25), color)


###########################################
# drawHouse()
#       Draw a house depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# house_width : int
#     width of the hosue
# house_height : int
#     height of the house
# primary_color : str
#     color of the building
# secondary_color : str
#     color of the roof
#
# Returns
# -------
# none

def drawHouse(x, y, house_width, house_height, primary_color, secondary_color):

    # Define some variables that will be useful for house construction
    roof_height = house_height * 0.2
    building_height = house_height * 0.8

    # Draw the building
    drawRectangle(x, y, house_width, building_height, primary_color)

    # create the variables needed to draw the door
    door_width = house_width / 8
    door_height = house_height / 4

    # Draw the door relative to the height of the building, it will be brown
    door_x = x+(house_width * 0.75)
    door_y = y
    drawRectangle(door_x, door_y, door_width, door_height, "brown")

    # Draw the doorknob, it will be gold
    drawCircle(door_x + door_width*3/4, door_y + door_height/2, 3, "gold")

    # Draw roof, it will be the secondary color
    overhang = 20
    drawTriangle(x-(overhang / 2), (y + building_height), (house_width + overhang), roof_height, secondary_color)

    # Set the pen color to brown, this will make the window frame look nice
    pencolor("brown")
    pensize(2)

    # Draw the window, fill with light blue
    window_size = building_height / 2
    window_x = (x+(house_width * 0.2))
    window_y = y + (building_height / 3)
    drawRectangle(window_x, window_y, window_size, window_size/2, "light blue")

    # Divide the window into 4 sections
    goto(window_x + window_size/2, window_y)
    pendown()
    goto(window_x + window_size/2, window_y + window_size/2)
    penup()
    goto(window_x, window_y + window_size/4)
    pendown()
    goto(window_x + window_size, window_y + window_size/4)

    # Change the pencolor back to black, the size back to 1, then lift the pen
    pencolor("black")
    pensize(1)
    penup()


###########################################
# drawTownSign
#       Draw a sign with the town name depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# text : str
#     text to be printed on the sign
#
# Returns
# -------
# none

def drawTownSign(x, y, text):

    # Find out the length of the letters and set the sign length accordingly
    letters = len(list(text))
    sign_width = (letters*10)+10

    # Draw the rectangular feet of the sign
    drawRectangle((x+sign_width/2-5), y, 10, 75, "brown")
    drawRectangle((x-sign_width/2-5), y, 10, 75, "brown")

    # Make sure "Welcome to" fits inside the sign, if not, change the sign width
    if letters < 10:
        sign_width = 120

    # Draw the sign that we will place the text on
    drawRectangle(x-(0.5*sign_width), y+15, sign_width, 60, "light grey")

    # Draw the text that tells the name of the neighborhood
    setpos(x, y+50)
    write("Welcome to", align="center", font=("Monaco", 12, "normal"))
    setpos(x, y+20)
    write(text, align="center", font=("Monaco", 12, "normal"))


################################################################################
# Start Drawing the Neighborhood


# Read each file
infile = open("input_file.txt")
text_array = []

# read the first line
line = infile.readline()

# Add each line of the text file to text_array
while line:

    # remove newline
    line = line.rstrip('\n')

    # append the line to text_array
    text_array.append(line)

    # read the next line
    line = infile.readline()


# Look at each segment of text in the text array, and figure out what to do with it
for text in text_array:
    print(text) # debugging

    # Make the string into an array of smaller strings
    text = text.split()

    # Replace underscores with spaces
    for i in range(len(text)):
        if "_" in text[i]:
            text[i] = text[i].replace("_", " ")

    # If the first word is house, draw a house
    if text[0] == "house":
        drawHouse(int(text[1]), int(text[2]), int(text[3]), int(text[4]), text[5], text[6])

    # If the first word is tree, draw a tree
    elif text[0] == "tree":
        drawTree(int(text[1]), int(text[2]), int(text[3]), text[4])

    # If the first word is not one of the things above, print an error message
    else:
        print("ERROR, CANNOT DRAW: " + '"'+ text[0] +'"')


# Draw the town sign last
drawTownSign(0, -300, text_array[0])

input()
