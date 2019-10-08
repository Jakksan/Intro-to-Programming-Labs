import math
from turtle import *
import random
import time


# Ask the user how many points they want done and  multiply input by 100
total_dots = int(input('How many dots? (*100): '))

start_time = time.time()
total_dots = total_dots*100
inside_circle = 0

setworldcoordinates(-25,-25,310,310)
tracer(False)

penup()
setpos(300, 0)
setheading(90)
pendown()

circle(300, 90)
right(180)
forward(300)
right(90)
forward(300)

penup()


for each in range(total_dots):
    random_x = randint()
    random_y = randint()

    for i in range(2):

    if sqrt(pow(random_x, 2) + pow(random_y, 2)) >= 150:
        color = "red"
    else:
        color = "green"
        inside = inside + 1

    total_dots = total_dots + 1

    setpos(x * 300 for x in randomXY)
    pendown()
    dot(3)
    penup()
update()

print('The final count is ' + str(inside_circle) + '/' + str(total_dots))
print((inside_circle/total_dots)*4)
end_time = time.time()
print("The computations took ", end_time - start_time, "seconds")
input()
