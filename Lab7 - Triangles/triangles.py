from math import *
from turtle import *
from time import *

def isEquilateral(a,b,c):
    return(a == b and a == c)

def isIsosolece(a,b,c):
    return((a == b and a != c) or (a==c and a != b)) or (b == c and b != a )

def isRight(a,b,c):
    sideLengthsArray = [a,b,c]
    sideLengthsArray.sort()

    difference = sqrt(pow(sideLengthsArray[0], 2)+pow(sideLengthsArray[1],2)) - sideLengthsArray[2]
    return(abs(difference) < .000000000001)


def triangleClassifier(a,b,c):
    if isEquilateral(a,b,c):
        return("equilateral")
    elif isRight(a,b,c):
        if(isIsosolece(a,b,c)):
            return("right and isosolece")
        return("right and scalene")
    elif isIsosolece(a,b,c):
        return("isosolece")
    else:
        return("scalene")


sidesArray = []

a = float(1)
b = float(2)
c = float(3)
d = float(4)
e = float(5)
f = sqrt(2)

sidesArray.extend([a,b,c,d,e,f])


arrayLength = len(sidesArray)
for i in range(arrayLength):
    side1 = sidesArray[i]
    for j in range(arrayLength):
        side2 = sidesArray[j]
        for k in range(arrayLength):
            side3 = sidesArray[k]

            print("( "+format(side1, ".2f")+"/"+format(side2, ".2f")+"/"+format(side3, ".2f")+" ) " + triangleClassifier(side1, side2, side3))






print()
print(isRight(e,d,c))
print()
print(sqrt(pow(c, 2)+pow(d,2)))
print(e)
