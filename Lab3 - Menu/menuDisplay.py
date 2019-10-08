import sys
def main():
    #Welcome
    print("Welcome to the Online Menu!")

    #Check for allergies
    vegetarian = input("Are you a vegetarian?(yes or no)\n").lower()
    kosher = input("Do you eat kosher?(yes or no)\n").lower()
    eggAllergy = input("Do you have an egg allergy?(yes or no)\n").lower()

    bCanEatMeat = (vegetarian != ("yes" or "y"))
    bKosher = (kosher == ("yes" or "y"))
    bEggAllergy = (eggAllergy ==("yes" or "y"))

    print("Can eat meat: " + str(bCanEatMeat))
    print("Can eat Kosher food: " + str(bKosher))
    print("Cannot eat Eggs: " + str(bEggAllergy))

     #food choices
    A = '$7.50 chicken and biscuits'
    B = '$8.25 pulled pork sandwich'
    C = '$8.00 blackened redfish'
    D = '$7.50 shrimp and grits'
    E = '$6.00 cheesy potato soup'
    F = '$6.50 southwest omelette'
    G = '$6.50 eggplant parmesan'
    H = '$8.25 ham benedict sliders'
    I = '$3.00 orange juice'
    J = '$2.50 sweet tea'
    K = '$1.25 bottled water'

    vegList=[E,F,G]
    vegAndKosher=[E,F,G]
    vegAndEggallergy=[E,G]
    kosherList=[A,C,E,F,G]
    eggAllergyList=[A,B,C,D,E,G]
    eggAllergyAndKosher=[A,C,E,G]
    vegEggallergyAndKosher=[E,G]
    defaultList=[A,B,C,D,E,F,G,H]
    drinkList = [I,J,K]

    if (bCanEatMeat == True) and (bKosher==True) and (bEggAllergy==True):
        for food in eggAllergyAndKosher:
            print(food)
    elif (bCanEatMeat==True) and (bKosher==True) and (bEggAllergy==False):
        for food2 in defaultList:
            print(food2)
    elif (bCanEatMeat==True) and (bKosher==False) and (bEggAllergy==True):
        for food3 in eggAllergyList:
            print(food3)
    elif (bCanEatMeat==True) and (bKosher==False) and (bEggAllergy==False):
        for food4 in defaultList:
            print(food4)
    elif (bCanEatMeat==False) and (bKosher==True) and (bEggAllergy==True):
        for food5 in vegEggallergyAndKosher:
            print(food5+"\n")
    elif (bCanEatMeat==False) and (bKosher==True) and (bEggAllergy==False):
        for food6 in vegAndKosher:
            print(food6)
    elif (bCanEatMeat==False) and (bKosher==False) and (bEggAllergy==True):
        for food7 in vegAndEggallergy:
            print(food7)
    elif (bCanEatMeat==False) and (bKosher==False) and (bEggAllergy==False):
        for food8 in vegList:
            print(food8)
    else:
        print("please enter a valid input")
    #User

    #Display drink menu
    # for drinks in drinkList:
    #     print(drinks)

    #Print total value of the meal
    #Exit program
    sys.exit()

main()
