class Ingredient:
    def __init__(self, name, category, quantity, quantity_type, expires):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.quantity_type = quantity_type
        self.expires = expires

    @classmethod
    def construct_ingredient_database(cls, database):
        pass

    # This way it gets implemented as Ingredient.construct_ingredient_database(database)