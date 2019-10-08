
# Import required packages
from PIL import Image, ImageStat, ImageColor
import numpy as np
import sys

# open the image file and show the grayscale image
image_name = "mars.png"
img = Image.open("./Images/" + image_name)
img = img.convert("L")
# img.show()

#####################################################
# Name: color_to_temp()
# Description: takes the rgb value from the grayscale and returns the temperature of the input pixel
# Parameters: x (the x coordinate of the pixel), y (the y coordinate of the pixel)
# Returns: the resulting temperature
def color_to_temp(x, y):
    pix_color = pix_list[y][x]
    pix_temp = (pix_color*34)/255
    # pix_temp = '{0:.3g}'.format(abs(34-pix_temp))
    return pix_temp

#####################################################
# Name: temp_to_color()
# Description: takes the temperature of the input pixel and returns the rgb value assosciated with that temperature
# Parameters: x (the x coordinate of the pixel), y (the y coordinate of the pixel)
# Returns: the resulting temperature
def temp_to_color(x, y):
    pix_temp = pix_list[y][x]
    pix_color = (pix_temp*255)/34
    pix_color = int(pix_color)
    return colors[pix_color]

#####################################################
# accesses the color map file and reads it to a list of values
colors = []
line_count = 0

try:
    # open file for reading
    infile = open( "cmap.txt", "r")

except:
    # quits if error in accessing file
    print ("error in accessing file")
    sys.exit()

# read the first line
line = infile.readline()

# for each line in the list
while line:
    # break up each line into color variable lists
    line = line.replace(',', '')
    line = line.split()
    for each in range(len(line)):
        line[each] = int(line[each])
    colors.append(line)
    line = infile.readline()

########################################################

# convert the image into a numpy array, then to a standard list
pix = np.array(img)
pix_list = pix.tolist()

########################################################

for y in range(len(pix_list)):
    for x in range(len(pix_list[y])):
        pix_list[y][x] = color_to_temp(x, y)

# run the program for 100 timesteps and print each step
count = 0
for each in range(10):
    count += 1
    print("Timestep:", count)
    timestep_changes = []
    # for each pixel, check it's neighbors and average the values
    for y in range(len(pix_list)):
        for x in range(len(pix_list[y])):
            try:
                # each of each pixel's neighbors
                above = pix_list[y - 1][x]
                below = pix_list[y + 1][x]
                right = pix_list[y][x + 1]
                left = pix_list[y][x - 1]

                if pix_list[y][x] == 0:
                    raise KeyError()

                # accounts for boundaries of the box
                if x-1 < 0 or y-1 < 0:
                    raise IndexError()

                # takes the average
                before = pix_list[y][x]
                pix_list[y][x] = (0.5*pix_list[y][x]) + ((above + below + left + right)/8)
                after = pix_list[y][x]
                change = before - after
                timestep_changes.append(change)

            except IndexError:
                # This is an edge cell.
                pix_list[y][x] = 34

            except KeyError:
                pix_list[y][x] = 0

    timestep_changes.sort()
    print('Max Cell Change:', timestep_changes[-1])
    # print(get_color_temp(0, 0))
########################################################

print(color_to_temp(100, 100))
# print(color_to_temp(2, 2))

# takes each pixel value and converts it to an rgb value based on the color map
for y in range(len(pix_list)):
    for x in range(len(pix_list[y])):
        pix_list[y][x] = temp_to_color(x, y)

# turns the list back into a numpy array
pix = np.asarray(pix_list, dtype=np.uint8)

# creates an image from the numpy array
newImage = Image.frombytes('RGB', img.size, pix)

# show final image
newImage.show()
