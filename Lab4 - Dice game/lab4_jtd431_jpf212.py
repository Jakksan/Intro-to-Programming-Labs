# GAME RULES
# 1) Both players roll a d6
# 2) The winning player takes the pot.
# 3) On a tie that isn’t snake eyes, both players roll 2 more dice. The required bet doubles. Player has the option to back out.
# 4) On a tie where both players get a one, the house takes the pot.

#imports important python libraries
import random
import sys
import time

# Asks player how much money they have
wallet = float(input("How much money do you have in your wallet? "))

# Keep track of how many rounds have been played
roundsPlayed = 0

# Loop though until the user wants to give up
playing = True
while playing:
	# Asks player for bet amount and subtracts it from the wallet
	# The house adds that same amount to the pot
	bet = float(input("What will be your starting bet be? "))
	wallet = wallet - bet
	pot = bet * 2

	# Defines dice roll arrays for each player
	roundInProgress = True
	playerDiceArray = []
	houseDiceArray = []

	# Loop through this until the round is over
	while roundInProgress:

		# Appends a new dice roll to each player
		playerDiceArray.append(random.randint(1, 6))
		houseDiceArray.append(random.randint(1, 6))

		# Adds all dice roll numbers together
		playerRoll = sum(playerDiceArray)
		houseRoll = sum(houseDiceArray)

		# Tell the player the pot size
		print("The pot is ", format((pot), ".2f" ), "\n")
		time.sleep(1) # D R A M A T I C 	F L A R E

		print("##############################")
		# Print out all of the dice rolls the player makes
		for roll in range(len(playerDiceArray)):
			print("You rolled a " + str(playerDiceArray[roll-1]))
			time.sleep(0.5)

		# Print out all of the dice rolls the house makes
		for roll in range(len(houseDiceArray)):
			print("The house rolled a " + str(houseDiceArray[roll-1]))
			time.sleep(0.5)
		print("##############################")


		# Player wins
		if playerRoll > houseRoll:
			print("\nCongrats. You won the round")
			wallet = wallet + pot
			roundInProgress = False

		# House wins
		elif playerRoll < houseRoll:
			print("\nHouse wins, maybe next time.")
			roundInProgress = False

		# Tie (snake eyes)
		elif playerRoll + houseRoll == 2 * len(playerDiceArray):
			print("\nSnake Eyes, house wins.")
			roundInProgress = False

		# Normal tie
		else:
			continueRoundAnswer = input("Would you like to continue? This will double the pot. ")
			if continueRoundAnswer == "y" or continueRoundAnswer == "yes":
				print("Alright, good luck.")
				wallet = wallet - bet
				pot = pot + (bet * 2)
				print("The pot is now  $" + format((pot), ".2f") )

	# Display amount of money the player still has
	print ("You have $" + format((wallet), ".2f") + " in your wallet")
	print( "-----------------------------------")

	# Player wants to keep playing
	continueGameAnswer = input("Would you like to keep playing? ")
	if continueGameAnswer == "yes" or continueGameAnswer == "y":
		roundsPlayed = roundsPlayed + 1
		print("You've played " + str(roundsPlayed)+ " round so far, good luck!")

	# Player decides to walk away
	elif continueGameAnswer == "no" or continueGameAnswer == "n":
		print("Congragulations you're walking away with $" + format((wallet), ".2f" ))
		playing = False

	# Terrible implemention of dealing with invalid input
	else:
		print("Invalid input.")
		sys.exit()
