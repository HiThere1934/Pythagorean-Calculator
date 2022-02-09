import math #Importing math module to do mathematics

keepGoing = '' #Make sure while loop starts
print("Pythagorean Theorem is a method of discovering the side length of any side in a right triangle!\n") #Introduction message

while keepGoing == '': #While loop to keep on looping
	side1 = 0 # Make sure side1 variable isn't the answer of before
	side2 = 0 # Same as above
	hypotenuse = 0 # Same as above
	solution = '' # Same as above
	sideToSolve = int(input("Would you like to find 1. The length of a leg of the triangle (a shorter side), or 2. Find the hypotenuse (Longest side)? \nUse the Corresponding Number (1 or 2): "))
	if sideToSolve == 1:
		print("You have chosen option 1, find the length of a leg of the triangle. When entering your values in the below field, make sure your units are consistent.")
		side1 = int(input("What is the defined side?: "))
		hypotenuse = int(input("What is the hypotenuse?: "))
		side2 = math.sqrt(hypotenuse**2-side1**2) #Solve
		print("Your defined side is", str(side1) + ", and your hypotenuse is", str(hypotenuse) + ". Therefore, your missing side is", str(side2) + "!")
		solution = input("Show Solution?(Yes or No): ")
		#Failsafes Start
		solution = solution.lower() #Lowercase
		if solution == 'yes': #Change all answers to y or n
			solution = 'y'
		elif solution == 'no':
			solution = 'n'
		#Failsafes End
		if solution == 'y': #Show solution if they want
			print("Let a = Leg A's length -->", side1, "\nLet b = Leg B's length \nLet c = Hypotenuse length -->", hypotenuse)
			print("a^2 + b^2 = c^2 \nb^2 = c^2 - a^2")
			print("IF a =", str(side1) + ", c =", str(hypotenuse)+ "; THEN") #Switching to s-strings because they'll make coding the next print statement easier
			print("b^2 = %s^2 - %s^2 \nb^2 = %s - %e \nb^2 = %r \nb = sqrt(%r) \nb = %s" %(hypotenuse, side1, hypotenuse ** 2, side1*side1, hypotenuse**2-side1**2, hypotenuse**2-side1**2, math.sqrt(hypotenuse**2-side1**2)))
		elif solution == 'n':
			print("Okay")
		else: #Make sure python doesn't throw error and end code
			print("PUT IN GOOD VALUE")
	elif sideToSolve == 2:
		print("You have chosen to solve for the hypotenuse! Remember to keep your units consistent!")
		side1 = int(input("What is the length of the first side?: "))
		side2 = int(input("What is the length of the second side?: "))
		hypotenuse = math.sqrt(side1**2 + side2**2) #Solve
		print("Your first side is", str(side1) + ", and your second side is", str(side2) + ". Therefore, your hypotenuse is", str(hypotenuse) + "!")
		solution = input("Show Solution?(Yes or No): ")
		#Insert failsafes here
		solution = solution.lower()
		if solution == 'yes':
			solution = 'y'
		elif solution == 'no':
			solution = 'n'
		#END FAILSAFES
		if solution == 'y': #Show solution if they want
			print("Let a = Leg A's length -->", side1, "\nLet b = Leg B's length -->", side2, " \nLet c = Hypotenuse length")
			print("a^2 + b^2 = c^2")
			print("IF a =", str(side1) + ", b =", str(side2)+ "; THEN") #Switching to s-strings because they'll make coding the next print statement easier
			print("%s^2 + %s^2 = c^2 \n%s + %s = c^2 \n%s = c^2 \nsqrt(%s) = c \n%s = c" %(side1, side2, side1 ** 2, side2*side2, side2**2+side1**2, side2**2+side1**2, math.sqrt(side2**2+side1**2)))
		elif solution == 'n':
			print("Whatever you say...")
		else: #Be calmer than before
			print("Put in yes or no next time...")
	else: #Making sure error isn't thrown when number above 2 is eneteres
		print("We are sorry, but an error occured, please try again.\n")
	keepGoing = input("Would you like to continue using this Pythagorean Theorem Calculator? \nPress [ENTER] to continue, any other key and [ENTER] to quit: ")
	if keepGoing != '': #Ending message before quitting
		print("Thank you for using this calculator, we hope you use it again soon for any of your math needs. \n \n(C) Raghav Singh 2022, All Rights Reserved")