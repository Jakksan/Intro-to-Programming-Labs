# Purpose: Display a menu suited for the customer
# To Do: Don't allow invalid input on the first three questions.

import sys

def main():
    #Welcome
    print("Welcome to the Online Menu!")

    #Check for allergies
    vegetarian = input("Are you a vegetarian?(yes or no)\n").lower()
    kosher = input("Do you only eat kosher?(yes or no)\n").lower()
    eggAllergy = input("Do you have an egg allergy?(yes or no)\n").lower()

    # Assign answers to boolean variables
    bCanEatMeat = not((vegetarian == ("yes")) or (vegetarian == ("y")))
    bKosher = ((kosher == ("yes")) or (kosher == ("y")))
    bEggAllergy = ((eggAllergy ==("yes")) or (eggAllergy ==("y")))

     # Food and drink choices
    A = 'A) $7.50 chicken and biscuits'
    B = 'B) $8.25 pulled pork sandwich'
    C = 'C) $8.00 blackened redfish'
    D = 'D) $7.50 shrimp and grits'
    E = 'E) $6.00 cheesy potato soup'
    F = 'F) $6.50 southwest omelette'
    G = 'G) $6.50 eggplant parmesan'
    H = 'H) $8.25 ham benedict sliders'
    I = 'A) $3.00 orange juice'
    J = 'B) $2.50 sweet tea'
    K = 'C) $1.25 bottled water'

    # Food and drink prices
    A_price = 7.50
    B_price = 8.25
    C_price = 8.00
    D_price = 7.50
    E_price = 6.00
    F_price = 6.50
    G_price = 6.50
    H_price = 8.25
    I_price = 3.00
    J_price = 2.50
    K_price = 1.25

    # Below are the different possible combinations of food requirements in a list
    # V stands for Vegetarian Items, K stands for Kosher items, E stands for Egg-free items
    V_list=[E,F,G]
    VK_list=[E,F,G]
    VE_list=[E,G]
    K_list=[A,C,E,F,G]
    E_list=[A,B,C,D,E,G]
    EK_list=[A,C,E,G]
    VEK_list=[E,G]
    defaultList=[A,B,C,D,E,F,G,H]

    # Drink list
    drinkList = [I,J,K]


    # a function to get a valid food choice from the user
    def getValidFoodChoice(options):
        foodChoiceValidity = False # a variable to determine if the chosen food is valid.
        while (foodChoiceValidity == False):
            foodChoice = input("What food would you like? ").lower()
            if foodChoice not in options:
                print("Invalid choice. Please try again.")
                foodChoiceValidity = False
            else:
                foodChoiceValidity = True
                return foodChoice


    # Evaluate the user's choices to select the relevant list
    if (bCanEatMeat) and (bKosher) and (not bEggAllergy):
        for food in EK_list:
            print(food)
        foodChoice = getValidFoodChoice(["a","c","e","g"])

    elif (bCanEatMeat) and (bKosher) and (not bEggAllergy):
        for food2 in K_list:
            print(food2)
        foodChoice = getValidFoodChoice(["a","c","e","f","g"])

    elif (bCanEatMeat) and (not bKosher) and (bEggAllergy):
        for food3 in E_list:
            print(food3)
        foodChoice = getValidFoodChoice(["a","b","c","d","e","g"])

    elif (bCanEatMeat) and (not bKosher) and (not bEggAllergy):
        for food4 in defaultList:
            print(food4)
        foodChoice = getValidFoodChoice(["a","b","c","d","e","f","g","h"])

    elif (not bCanEatMeat) and (bKosher) and (bEggAllergy):
        for food5 in VEK_list:
            print(food5)
        foodChoice = getValidFoodChoice(["e","g"])

    elif (not bCanEatMeat) and (bKosher) and (not bEggAllergy):
        for food6 in VK_list:
            print(food6)
        foodChoice = getValidFoodChoice(["e","f","g"])

    elif (bCanEatMeat == False) and (not bKosher) and (bEggAllergy):
        for food7 in VE_list:
            print(food7)
        foodChoice = getValidFoodChoice(["e","g"])

    elif (not bCanEatMeat) and (not bKosher) and (not bEggAllergy):
        for food8 in V_list:
            print(food8)
        foodChoice = getValidFoodChoice(["e","f","g"])

    # User makes food choices
    if foodChoice == 'a':
        foodPrice = A_price
    elif foodChoice == 'b':
        foodPrice = B_price
    elif foodChoice == 'c':
        foodPrice = C_price
    elif foodChoice == 'd':
        foodPrice = D_price
    elif foodChoice == 'e':
        foodPrice = E_price
    elif foodChoice == 'f':
        foodPrice = F_price
    elif foodChoice == 'g':
        foodPrice = G_price
    elif foodChoice == 'h':
        foodPrice = H_price

    #Display drink menu
    for drinks in drinkList:
        print(drinks)


    # Find out which drink the user wants. Only take valid input.
    drinkChoiceValidity = False # a variable to determine if the chosen food is valid.
    while (drinkChoiceValidity == False):
        drinkChoice = input("What drink would you like? ").lower()
        if drinkChoice not in ["a","b","c"]:
            print("Invalid choice. Please try again.")
            drinkChoiceValidity = False
        else:
            drinkChoiceValidity = True

    # Set the price of the selected drink
    if drinkChoice == 'a':
            drinkPrice = I_price
    elif drinkChoice == 'b':
            drinkPrice = J_price
    elif drinkChoice == 'c':
            drinkPrice = K_price


    #Print total value of the meal
    print(
    format("Your drink price is $" + format((drinkPrice + foodPrice), ".2f" )))
    #Exit program
    sys.exit()

main()
