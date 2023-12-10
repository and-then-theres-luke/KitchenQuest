from ingredient_database import dairy_data

class Ingredient:
    def __init__(self, name, category, quantity, quantity_type, expires):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.quantity_type = quantity_type
        self.expires = expires

    @classmethod
    def construct_ingredient_database(cls, database):
        constructed_list = []
        for ingredient in range(0,len(database)):
            constructed_list.append(Ingredient(database[ingredient]['name'],database[ingredient]['category'], database[ingredient]['quantity'], database[ingredient]['quantity_type'], database[ingredient]['expires']))
        return constructed_list

    @classmethod
    def display_ingredient_database(cls):
        for ingredient in range(0,len(MASTER_INGREDIENT_LIST)):
            print(f'''Index: {ingredient} Name: {MASTER_INGREDIENT_LIST[ingredient].name} Category: {MASTER_INGREDIENT_LIST[ingredient].category} Quantity: {MASTER_INGREDIENT_LIST[ingredient].quantity} {MASTER_INGREDIENT_LIST[ingredient].quantity_type} Expires: {MASTER_INGREDIENT_LIST[ingredient].expires}''')
            
    @classmethod
    def ingredient_search(cls, database):
        pass

