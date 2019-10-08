import math
import random
import time



for i in range(4,9):

    dots_under_curve = 0
    total_dots = 10**i
    start_time = time.time()
    random_x_array = []
    random_y_array = []
    for dot in range(total_dots):
        random_x ,random_y = random.random(), random.random()

        if math.sqrt(random_x**2 + random_y**2) <= 1:
            dots_under_curve = dots_under_curve + 1

    # print('The final count is ' + str(dots_under_curve) + '/' + str(total_dots))
    print("Number of Darts: " + format( total_dots, ".0e" ))
    print('Approximate Pi: '+ format(((dots_under_curve / total_dots)*4), ".7f"))
    end_time = time.time()
    print("Computation time: ", format((end_time - start_time), ".3e"), "seconds\n")
