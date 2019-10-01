# Alan Fitzpatrick
# Rock, Paper, Scissors
# variables
import random

pScore = 0
cScore = 0
ties = 0
computerChoices = ["r", "p", "s"]


# Welcome Message
# Print the message 
print("Welcome to Rock Paper Scissors")
# Promt for player name
pName = input("What is your name? ")

# Final Score
def printScore():
	# Write message
	print("The score is: ")
# Write player score
	print(pName + ": " + str(pScore))
# Write computer score
	print("Computer: " + str(cScore))
# Write amount of ties
	print("Ties " + str(ties))

# Game Loop
# Make a forever loop
while True:
	# Print current score
	printScore()
	# Prompt for a choice (r (rock), p(paper), s(scissors), q(quit))
	pChoice = input("Enter r for (rock), p for (paper), s for (scissors), or q for(quit): ")
	# deal with player entering q
	if pChoice == "q":
		break
	# get computers choice (random)
	cChoice= random.choice(computerChoices)

	# Compare for player entering r
	if pChoice == "r":
		print(pName + "picked Rock")
		# if computer is r
		if cChoice == "r":
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		# if computer is p
		elif cChoice == "p":
			print("Computer picked paper")
			print("Player covers Rock")
			cScore = cScore + 1
		# if computer is s
		else:
			print("Computer picked scissors")
			print("Rock breaks scissors")
			pScore = pScore + 1
	# Compare for player entering p
	elif pChoice == "p":
		print(pName + "picked Paper")
		# if computer is p
		if cChoice == "p":
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1
		# if computer is r
		elif cChoice == "r":
			print("Computer picked Rock")
			print("Player covers Rock")
			pScore = pScore + 1
		# if computer is s
		else:
			print("Computer picked scissors")
			print("Scissors cuts paper")
			cScore = cScore + 1
	# Compare for player entering s
	elif pChoice == "s":
		print(pName + "picked scissors")
		# if computer is r
		if cChoice == "s":
			print("Computer picked Scissors")
			print("This is a tie")
			ties = ties + 1
		# if computer is p
		elif cChoice == "p":
			print("Computer picked paper")
			print("Player cuts paper")
			pScore = pScore + 1
		# if computer is r
		else:
			print("Computer picked Rock")
			print("Rock breaks scissors")
			cScore = cScore + 1
	# deal with player entering anything else
