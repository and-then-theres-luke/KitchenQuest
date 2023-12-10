# Many to Many
class Recipe:
    def __init__(self, name, picture, required_ingredients, required_ingredients_quantity, steps_in_order, servings, notes):
        self.name = name
        self.picture = picture 
        self.required_ingredients = required_ingredients # Index of required ingredients
        self.required_ingredients_quantity = required_ingredients_quantity # Index of required ingredients quantity
        self.steps_in_order = steps_in_order
        self.notes = notes # This is in case the user wants to add notes to the recipe
        self.is_leftover = False
        self.xp_value = 100
        self.servings = servings
    
    @classmethod
    def construct_recipe_database(cls, database):
        # When the program loads I want to be able to take the database, loop through, and create list of recipe instances that can be used to create recipes for the week
        pass

    def construct_recipe(self, recipe)
        # Constructs an instance of a recipe at full hit points
        pass


