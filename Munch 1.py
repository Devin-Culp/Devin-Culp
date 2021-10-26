'''Build everything out in notes so you can stay on track!!!
Lable out what your function are going to be
lable out what your lists are going to be
Lable out what your app is suppose to do, break it down and be specific
'''

'''
Munch App MVP
v0.1
By C&C
The purpose of Munch is to produce a dinner menu from favourite dishes,
and produce a shopping list of ingredients if required.
'''

# -------- Imports ---------

from random import choice

# ----- A. Functions -----

# A1. Choose dishes

def chooseDishes(dinners):
    while len(myMenu) < int(dinners):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done!, Here's your menue...")
    print()
    for dish in myMenu:
        print(dish)
    print()
    print("Out of all these dishes, my favourite has to be... " + choice(myMenu))

    '''
    1. Choose random dish from foodWeLike - Done!!
    2. Check dish hasn't been choosen. If not, add to meMenu - Done!
    3. Repeat untill we have required number of dishes in myMenu - Done!
    '''


# A2. Build shopping list

def buildShoppingList():
    myShoppingList = []
    if "Pizza" in myMenu:
        myShoppingList.append(pizza)
    if "Burgers" in myMenu:
        myShoppingList.append(burgers)
    if "Pork Stir Fry" in myMenu:
        myShoppingList.append(porkStirFry)
    if "Chicken Fajitas" in myMenu:
        myShoppingList.append(chickenFajitas)
    if "Honey Glazed Salmon" in myMenu:
        myShoppingList.append(fishWater)
    if "Tacos" in myMenu:
        myShoppingList.append(spainDoBeThiccTho)
    print()
    for dish in myShoppingList:
        for ingredient in dish:
            print(ingredient)
    print()
    print("Enjoy!")


# ---- B. Lists ----

foodWeLike = ["Pizza", "Burgers", "Pork Stir Fry", "Chicken Fajitas", "Honey Glazed Salmon", "Tacos"]

pizza = ["Frozen Pizza"]
burgers = ["Beef", "Buns", "Ketchup", "Mustard", "Salt", "Pepper", "Onions", "Garlic Powder"]
porkStirFry = ["Pork", "Stir", "Fry"]
chickenFajitas = ["Chicken", "Tortilla Shells", "Salsa", "Sour Cream", "Lettuce", "Tomatoes"]
honeyGlazedSalmon = ["Salmon", "Honey", "Garlic", "Soy Sauce"]
tacos = ["Beef", "Garlic", "Onion", "Taco Seasoning", "Tomatoe", "Sour Cream", "Salsa"]

myMenu = []


# 1. How many days to plan?

print("Hello, I'm Munch! I'll help you to plan your dinner menu!")

answer = input("How many days would you like me to plan? ")

print("Ok, I'm going to plan " + answer + " of your favorite dinners!")

# 2. Choose dishes

chooseDishes(answer)


# 3. Build shopping list?

answer = input("Would you like a shopping list for this menu? ")

if answer == "y":
    buildShoppingList()
    
    
else:
    print("You got it! See ya!")

