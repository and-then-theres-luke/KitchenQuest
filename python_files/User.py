class User:
    def __init__(self, name):
        self.name = name
        self.pantry = []
        self.leftovers = []
        self.xp = 0
        self.level = 1
        self.recipe_box = []
    
    def gain_xp(self, amount):
        self.xp += amount
        return self

    def add_to_pantry(self, ingredient_dictionary, index):
        
        self.pantry.append(Ingredient([ingredient_dictionary][index]))

    







