import user


print("Welcome to KitchenQuest!")
print("Are you a new user?")
new_user_check = input("Y/N")

if new_user_check == "Y":
    print("Welcome to the kitchen!")
    print("KitchenQuest is designed by Luke Thayer.")
    print("KitchenQuest was developed to help you move ingredients through your kitchen so they don't spoil.")
    print("The more ingredients you use in a recipe, the more experience you get. Gain enough experience and you level up!")
    print("Here are a few helpful commands to help you get around.")
    print(f'''DECK: Takes you to the deck editor.''')
    print(f'''CALENDAR: Takes you to the calendar where you can plan your meals.''')
    print(f'''RECIPES: Check out your current recipe box''')