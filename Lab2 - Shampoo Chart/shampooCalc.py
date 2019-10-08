# Purpose: tell the user the price per ounce of shampoo and put it into a table along with other provided data
# Ask user for name of shampoo, price of shampoo, and the size of the bottles.
# Repeat previous step 3 times
# Calculate the price per ounce for each shampoo


# Ask for information about shampoo #1
shampooName1 = input("What is the name of Your first shampoo? ")
priceTotal1 = float(input(str("What is the price of "+ shampooName1+ "? ")))
shampooSize1 = float(input(str("How many ounces are in "+ shampooName1+ "? ")))

# Ask for information about shampoo #2
shampooName2= input("What is the name of your second shampoo? ")
priceTotal2 = float(input(str("What is the price of "+ shampooName2+ "? ")))
shampooSize2 = float(input(str("How many ounces are in "+ shampooName2+ "? ")))

# Ask for information about shampoo #3
shampooName3 = input("What is the name of your third shampoo? ")
priceTotal3 = float(input(str("What is the price of "+ shampooName3+ "? ")))
shampooSize3 = float(input(str("How many ounces are in "+ shampooName3+ "? ")))


# Calculate price per Ounce for all three shampoos
pricePerOz1 = priceTotal1 / shampooSize1
pricePerOz2 = priceTotal2 / shampooSize2
pricePerOz3 = priceTotal3 / shampooSize3


# print table titles
print(
    format("Shampoo Name", "15s"), \
    format("Price", "10s"), \
    format("Size", "10s"), \
    format("Price Per Ounce", "10s")
    )

print('------------------------------------------------------------')


# print the data that is inside of our table.
# Note the use of the format inside of another forma tthis is neccessary because
# you cannot add white space to floating point variables, but you can with strings.
print(
    format( shampooName1, "15s"), \
    format("$" + format( priceTotal1, ".2f"), "10s"), \
    format(format( shampooSize1, ".2f" )+" oz", "10s"), \
    format("$" + format( pricePerOz1, ".2f" ), "10s")
    )
print(
    format( shampooName2, "15s"), \
    format("$" + format( priceTotal2, ".2f"), "10s"), \
    format(format( shampooSize2, ".2f" )+" oz", "10s"), \
    format("$" + format( pricePerOz2, ".2f" ), "10s")
    )
print(
    format( shampooName3, "15s"), \
    format("$" + format( priceTotal3, ".2f"), "10s"), \
    format(format( shampooSize3, ".2f" )+" oz", "10s"), \
    format("$" + format( pricePerOz3, ".2f" ), "10s")
    )
