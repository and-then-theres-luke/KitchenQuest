from ingredient import Ingredient
from ingredient_database import dairy_data

class User:
    def __init__(self, name):
        self.name = name
        self.pantry_deck = [] # This will be a one - to - one in the DB
        self.leftovers = [] # Same
        self.xp = 0
        self.xp_to_next_level = 300
        self.level = 1
        self.recipe_box = []
    
    def gain_xp(self, amount):
        self.xp += amount
        self.xp_to_next_level -=amount
        if self.xp_to_next_level <= 0:
            self.gain_level()
        return self

    def gain_level(self):
            self.level+=1
            retained_xp = self.xp_to_next_level * -1
            self.xp_to_next_level = (300 * self.level)
            self.xp_to_next_level -= retained_xp
            print(f'''{self.name} has reached level {self.level}!''')

    
    
    # I'd like a function to add ingredient by some kind of search, how do I make that redundant?
    
    #first method, initiate a search. It should be on ingredients since ingredients has access to the ingredients databaseeeee...
    def add_by_string(self, string):
        pass
        '''submission = input("Which ingredient would you like to add?")
        Ingredient.display_ingredient_database()
        if submission in MASTER_INGREDIENT_LIST.name:
            print(MASTER_INGREDIENT_LIST.name)'''
            
            
    def add_to_pantry(self, index):
        # Make a copy of an ingredient object, append it to the pantry_deck
        x = MASTER_INGREDIENT_LIST[index]
        self.pantry_deck.append(x)
        print(f'''You just added {x.name} to the pantry.''')

    def remove_from_pantry(self, index=0):
        # This is for removing a pantry deck object. Default is to remove the oldest item first.
        self.pantry_deck.pop(index)

MASTER_INGREDIENT_LIST = (Ingredient.construct_ingredient_database(dairy_data))
x = MASTER_INGREDIENT_LIST[1]
print(x.name)
luke = User("Luke")
luke.add_to_pantry(1)







