from math import sqrt

################################################################################
# name:         isEquilateral
# parameters:   sideA, sideB, sideC  --- triangle side lengths
# returnValues: boolean - True if triangle is equilateral
# purpose:  	Checks if triangle with given sides a,b,c is equilateral
def isEquilateral(sideA, sideB, sideC):
    # return whether or not all of the side lengths are equal
    return sideA == sideB and sideB == sideC

################################################################################
# name:         isIsosceles
# parameters:   sideA, sideB, sideC  --- triangle side lengths
# returnValues: boolean - True if triangle is isoscelese
# purpose:  	Checks if triangle with given sides a,b,c is isoscelese
def isIsosceles(sideA, sideB, sideC):
    # create a list of sides from the parameters
    sides = [sideA, sideB, sideC]

    # sort the sides to make them easier to work with
    sides.sort()

    # return whether or not two of the sides are equal, but not the third
    return((sideA == sideB and sideA != sideC) or (sideA==sideC and sideA != sideB)) or (sideB == sideC and sideB != sideA )


################################################################################
# name:         isRight
# parameters:   sideA, sideB, sideC  --- triangle side lengths
# returnValues: boolean - True if triangle is right
# purpose:  	Checks if triangle with given sides a,b,c is right
def isRight(sideA, sideB, sideC):
    # create a list of sides from the parameters
    sides = [sideA, sideB, sideC]

    # sort the side lengths to make them easier to work with
    sides.sort()

    # return whether or not leg1^2 + leg2^2 is almost equal to hypotenuse^2
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < epsilon

################################################################################
# name:         triangleClassifier
# parameters:   sideA, sideB, sideC  --- triangle side lengths
# returnValues: string --- type(s) of triangle (equilateral, right, isoscelese, or scalene)
# purpose:  	returns the type of triange given sides a,b,c
def triangleClassifier(sideA, sideB, sideC):
    # Is the triangle equlateral?
    if isEquilateral(sideA, sideB, sideC):
        return 'equilateral'

    # Is the triangle a right triangle? If so, what kind?
    elif isRight(sideA, sideB, sideC):
        if isIsosceles(sideA, sideB, sideC):
            return 'right and isoscelese'
        else:
            return 'right and scalene'

    # Is the triangle an Isosceles
    elif isIsosceles(sideA, sideB, sideC):
        return 'isoscelese'
    else:
        return 'scalene'

################################################################################
# All of our functions are now defined, below is the main program


# use this number as our machine epsilon
epsilon = 10 ** -14


# Below we create a list of triangle length lists
triangles = [
            [2.5, 2.5, 2.5],
            [5.82, 5.82, 3],
            [1.1, 2, 7],
            [3, 4, 5],
            [1, 1, sqrt(2)]]


# for each triangle defined above, print the side lengths and the classification

for triangle in range(len(triangles)): # for each triangle in the triangles list

    # The sides variable is a list of the side lengths in the current triangle
    sides = triangles[triangle]

    # Output should look something like this ---> (1, 2, 3)         scalene
    print("(" + str(sides[0]) + ", "+ str(sides[1]) + ", "+ str(sides[2])+ ")" + "\t\t" + triangleClassifier(sides[0], sides[1], sides[2]))
