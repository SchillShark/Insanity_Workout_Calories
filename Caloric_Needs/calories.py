# Determine maintanence calories for Insanity Program
# Import math libary for later
import math

# Introduction
print("\n\nHello! Welcome to the Caloric Needs program.\nThis program will help you determine the right amount of fuel your body\nwill need on the Insanity Program!")

print("Please choose the most accurate fitness lifestyle you have in addition to the program...\n\n 1. Sedentary (You do little to no physical activity outside the program)\n 2. Moderately Active (You exercise 3 -5 times per week in addition to Insanity\n 3. Highly Active (You have a highly active job or workout 6 -7 times per week in addition to Insanity")

multiply_weight_by = 0

# Get user input for fitness level
while True:
	# Check users input is correct and within scope
	print("\nPlease enter 1 , 2 or 3")
	user_fitness_level = input("\n: ")

	if user_fitness_level == "1":
		multiply_weight_by = 12
		break
	elif user_fitness_level == "2":
		multiply_weight_by = 13
		break
	elif user_fitness_level == "3":
		multiply_weight_by = 14
		break
	else:
		print("\nError! Please enter the numbers 1 , 2  or 3")
		continue
print("Loading....")

# Get users weight
user_weight = int(input("Please enter your current weight (Examples: 150, 174, 223)\n: "))

# Maintenence Caloric needs 
maintenence_caloric_needs = round(user_weight * multiply_weight_by, -2)
print("Thank you! One moment.")
print("Your current Maintenance Caloric Needs are: " + str(maintenence_caloric_needs))
print("\nNext let's figure out your weight goals...")
# Adjust caloric needs for Insanity Workouts
insanity_caloric_needs = maintenence_caloric_needs + 600

# Determine Weight Goals
while True: 
	print("1 = Weight Loss\n2 = Weight Maintenance\n3 = Weight Gain\n")
	print("Please enter 1 , 2 or 3 for your final caloric needs for the Insanity Workout Program!")
	user_goals = input(": ") 
	if user_goals == "1":
		insanity_caloric_needs = insanity_caloric_needs - 500
		insanity_caloric_needs = round(insanity_caloric_needs, -2)
		break
	elif user_goals == "2": 
		insanity_caloric_needs = round(insanity_caloric_needs, -2)
		break
	elif user_goals == "3": 
		insanity_caloric_needs = insanity_caloric_needs + 500
		insanity_caloric_needs = round(insanity_caloric_needs, -2)
		break
	else:
		print("Error!")
		continue

print("Loading....")
print("Your resuls are in!") 
print("Your caloric needs for this program are: " + str(insanity_caloric_needs) + " calories per day!")

