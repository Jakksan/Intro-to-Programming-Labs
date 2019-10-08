# Import required packages
from PIL import Image, ImageStat, ImageColor
import numpy as np
import sys

# open the image file and show the grayscale image
image_name = "handprint.png"
img = Image.open("./Images/" + image_name)
img = img.convert("L")
img.show()

#####################################################
# Name: get_color_temp()
# Description: takes the rgb value from the grayscale and prints out the temperature of the input pixel
# Parameters: x (the x coordinate of the pixel), y (the y coordinate of the pixel)
# Returns: None
def get_color_temp(x, y):
    pix_color = pix_list[y][x]
    pix_temp = (pix_color*34)/255
    pix_temp = '{0:.3g}'.format(abs(34-pix_temp))
    print('\nXY (', x, ",", y, ")")

    # print("Grayscale value:", pix_color)
    # print('Temperature:', pix_temp, 'degrees Celsius')

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

# run the program for 100 timesteps and print each step




# hand_pixels = []
# for y in range(len(pix_list)):
#     for x in range(len(pix_list[y])):
#         if pix_list[y][x] == 0: # This is a part of the hand. Never let these values change.
#             hand_pixels.append((x,y))




count = 0
for each in range(10000):
    count += 1
    print("\nTimestep:", count)
    pixel_change = []
    # for each pixel, check it's neighbors and average the values
    for y in range(len(pix_list)):
        for x in range(len(pix_list[y])):
            # coords = (x,y)
            try:
                # if coords not in hand_pixels: # uncomment hand_pixels = []
                if pix_list[y][x] != 0:
                    # each of each pixel's neighbors
                    above = pix_list[y - 1][x]
                    below = pix_list[y + 1][x]
                    right = pix_list[y][x + 1]
                    left = pix_list[y][x - 1]

                    # accounts for boundaries of the box
                    if x-1 < 0 or y-1 < 0:
                        raise IndexError()


                    prev_val = pix_list[y][x]

                    # heat equation
                    pix_list[y][x] = (pix_list[y][x]/2)+((above + below + left + right)/8)


                    delta_t = prev_val - pix_list[y][x]
                    pixel_change.append(delta_t)

                    # Make sure only the actual hand values can ever be true zero
                    if pix_list[y][x] == 0:
                        pixel_list[y][x] = pixel_list[y][x] + 0.00000000000000000000000001
            except:
                # This is an edge cell.
                pix_list[y][x] = 255


    if count % 100 == 0:
        ########################################################

        get_color_temp(100, 70)

        # takes each pixel value and converts it to an rgb value based on the color map
        for y in range(len(pix_list)):
            for x in range(len(pix_list[y])):
                if pix_list[y][x] > 255:
                    pix_list[y][x] = 255
                elif pix_list[y][x] < 0:
                    pix_list[y][x] = 0

                pix_list[y][x] = colors[int(pix_list[y][x])]


        # Test what happens when we try to get the color vals at various grayscale values
        test = 0
        test_color = colors[test]
        print(test_color)

        # turns the list back into a numpy array
        pix = np.asarray(pix_list, dtype=np.uint8)

        # creates an image from the numpy array
        newImage = Image.frombytes('RGB', img.size, pix)

        # show final image
        newImage.show()

        input()

    
