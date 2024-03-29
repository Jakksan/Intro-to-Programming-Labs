from random import randint
from turtle import *
from time import time

######################
# matrix[row(y)][column(x)]
# eg. matrix[1][3]:
# X X X X X X X X
# X X X O X X X X
# X X X X X X X X
# X X X X X X X X
######################

def glider(x, y):
    matrix[y][x+2] = 1
    matrix[y+1][x+2] = 1
    matrix[y+2][x+2] = 1
    matrix[y+2][x+1] = 1
    matrix[y+1][x] = 1

def block(x, y):
    matrix[y][x] = 1
    matrix[y+1][x] = 1
    matrix[y][x+1] = 1
    matrix[y+1][x+1] = 1

def spinner(x, y):
    matrix[y][x] = 1
    matrix[y+1][x+1] = 1
    matrix[y+2][x+2] = 1

# create a matrix the size provided by x_len and y_len
# assign each variable in the matrix a random number, 0 or 1, to read from
x_len = int(input("Columns: "))
y_len = int(input("Rows: "))

matrix = [[0 for l in range(x_len)] for p in range(y_len)]

glider(30, 2)

# make a hard copy of matrix for the rest of the program to write to
temp_matrix = [row[:] for row in matrix]
dot_size = 8

# set animation to false
tracer(False)
ht()

round_count = 0

# draw a new matrix of life and compute the next round
framecount = 2
for frame in range(framecount):
    start_time = time()
    clear()

    square_size = dot_size

    width_squares = x_len
    height_squares = y_len

    width = square_size * width_squares
    height = square_size * height_squares


    for each in range(int((width/square_size)/2)+1):
        if width_squares%2 == 1:
            each = each + 0.5
        penup()
        setpos(((each)*square_size)-(0.5*dot_size), (height/2)-(0.5*dot_size))
        pendown()
        setpos(((each)*square_size)-(0.5*dot_size), (-height/2)-(0.5*dot_size))
        penup()
        setpos(-((each)*square_size)-(0.5*dot_size), (height/2)-(0.5*dot_size))
        pendown()
        setpos(-((each)*square_size)-(0.5*dot_size), (-height/2)-(0.5*dot_size))

    for each in range(int((height/square_size)/2)+1):
        if height_squares%2 == 1:
            each = each + 0.5
        penup()
        setpos((width/2)-(0.5*dot_size), ((each)*square_size)-(0.5*dot_size))
        pendown()
        setpos(-(width/2)-(0.5*dot_size), ((each)*square_size)-(0.5*dot_size))
        penup()
        setpos((width/2)-(0.5*dot_size), -((each)*square_size)-(0.5*dot_size))
        pendown()
        setpos(-(width/2)-(0.5*dot_size), -((each)*square_size)-(0.5*dot_size))
        penup()


    # setup for turtle's position and clear the board
    penup()
    setpos(-x_len*(0.5*dot_size), y_len*(0.5*dot_size))


    # draw a dot in a position for every int in matrix
    # runs for each row
    for i in range(y_len):
        # runs for each column
        print("")
        for j in range(x_len):

            # test the int at the matrix current position, and draw a dot according to the reading
            if matrix[i][j] == 1:
                print()
                pencolor("black")
                dot(dot_size)
            else:
                pass

            # move the turtle incrementally to the right each round
            setx(xcor()+dot_size)

        # reset turtle x and move turtle down to the next line to draw
        setx(-x_len*(0.5*dot_size))
        sety(ycor()-dot_size)

    # checks the surroundings of all matrix items and adjusts matrix to predefined rules
    # runs for each row
    for i in range(y_len):
        #runs for each column
        for j in range(x_len):
            # set the surrounding live tile count to 0
            pos_count = 0
            # test each tile surrounding the tile
            # runs for each row
            for y in range(3):
                # runs for each column
                for x in range(3):
                    # try to test each position surrounding the tile, from top-left to bottom-right
                    # try in case of out of index error
                    try:
                        if matrix[(i + y-1)%y_len][(j + x-1)%x_len] == 1:
                            pos_count = pos_count + 1
                    except IndexError:
                        pass

            # corrects for the above test function checking the tile for liveness
            if matrix[i][j] == 1:
                pos_count = pos_count - 1

            # covers rule 1 and rule 3
            if pos_count < 2 or pos_count > 3:
                temp_matrix[i][j] = 0

            # covers rule 2
            elif (pos_count == 3 or pos_count == 2) and matrix[i][j] == 1:
                pass

            # covers rule 4
            elif pos_count == 3:
                temp_matrix[i][j] = 1

    # make a hard copy of temp_matrix for the rest of the program to read from
    matrix = [row[:] for row in temp_matrix]

    # update the turtle drawing after making sure at least some time has passed since last update
    time_bool = True
    while time_bool:
        end_time = time()
        if (end_time - start_time) > 0.5:
            time_bool = False
    update()

    # print info on round number
    round_count = round_count + 1
    print("round", round_count)
