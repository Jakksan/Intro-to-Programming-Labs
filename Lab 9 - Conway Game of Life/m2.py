survivors = {}

def critterLives(x, y, num):

    try:
        if survivors[(x,y)] is not None:
            print(survivors[(x,y)])
            age = survivors[(x,y)]
            survivors.update({(x,y): int(age + 1)})
    except:
        print("Exception")
        if num > 0:
            survivors.update({(x,y): 0})





critterLives(1, 2, 2)
critterLives(1, 4, 1)
critterLives(3, 2, 1)
critterLives(1, 2, 2)




print(survivors)
