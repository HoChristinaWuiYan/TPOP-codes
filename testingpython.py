#myNUmber.py
import random
computer_number = random.randint (1,100)
def is_same(target, number):
	if target == number:
		result="Win"
	elif target >number:
		result="Low"
	else:
		result="High"
	return result	
#Start the game
print ("Hello.\nI have thought of a number between 1 and 100.")
guess = int(input("Can you guess it ?"))
#Use our function
higher_or_lower=is_same(computer_number, guess)
#Run the game until the user is correct
while higher_or_lower != "Win":
	if higher_or_lower == "Low":
		guess=int(input("Sorry, you are too low. Try again."))
	else:
		guess=int(input("Sorry, you are too high. Try again."))
		
	higher_or_lower=is_same(computer_number, guess)	
#End the game
input ("Correct!\nWell done\n\n\nPress Return to exit.")