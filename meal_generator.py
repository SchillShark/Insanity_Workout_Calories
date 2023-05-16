# This application will give the user his/her meals for the week 
import random

# List of meal titles
meal1 = ["Pro-Oatmeal", "Fruit and Cottage Cheese", "Berry Protein Smoothie", "Bagel and Lox", "Egg White and Fruit Plate", "Egg White Breakfast Wrap", "Bowl of Cereal", "Peanut Butter Toast", "Veggie Omlet"]
meal2 = ["Mexican Style Eggs", "Protein Pancakes", "Warm Cereal Bowl", "Egg Sandwhich", "Protein Omlet", "Vanilla-Berry Protein Shake", "Yogurt Bowl", "Nutrition Bar", "Deli Sandwich", "Turkey BLT"]
meal3 = ["Grilled Chicken Salad", "Sushi Roll", "Black Bean Soup and Half Sandwich", "Roast Beef Sandwich", "Teriyaki Grilled Tuna", "Chicken Ranch Wrap", "Lean Burger", "Whole Wheat Pasta With Vegtables and Feta", "Salmon Nicoise Plate"]
meal4 = ["Sashimi", "Cold Cut Platter", "Peanut Butter and Jelly", "Tuna Salad In A Tomato", "Turkey Lettuce Wrap and Bean Salad", "Turkey Chili", "Protein Pizza Muffin", "Shrimp Cocktail Platter", "Rotisserie Chicken And Salad", "Roast Beef Wrap"]
meal5 = ["Baked Cod With Steamed Carrots, Corn, and Cauliflower", "Dinner Omlet", "Steak With Broccoli", "Chicken Meatballs", "Grilled Salmon With Asparagus", "Citrus Baked Chicken With Glazed Carrots", "Brown Rice Bowl", "Turkey Burger", "Chicken Stir Fry With Broccoli, Mushrooms, And Snow Peas", "Pasta With Seafood Marinara"]

print("########################################")
def meals_for_the_week():
# Print the meals randomly
    for meal in meal1:
        r = random.randint(0, len(meal1)-1)
        print("Meal 1 is: " + meal1[r] )
        break
    for meal in meal2:
        r = random.randint(0, len(meal2)-1)
        print("Meal 2 is: " + meal2[r] )
        break
    for meal in meal3:
        r = random.randint(0, len(meal3)-1)
        print("Meal 3 is: " + meal3[r] )
        break
    for meal in meal4:
        r = random.randint(0, len(meal4)-1)
        print("Meal 4 is: " + meal4[r] )
        break
    for meal in meal5:
        r = random.randint(0, len(meal5)-1)
        print("Meal 5 is: " + meal5[r] )
        break

meals_for_the_week()