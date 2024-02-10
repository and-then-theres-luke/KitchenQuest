
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, user
from datetime import date, timedelta
from flask import flash, session




class Pantry_Ingredient:
    db = "kitchenquest" 
    def __init__(self, data):
        self.id = data['id']                        # ID for an ingredient in the pantry
        self.user_id = data['user_id']              # ID for the user whose pantry that ingredient is in
        self.ingredient_id = data['ingredient_id']  # ID for the actual ingredient data
        self.current_hp = data['current_hp']
        self.max_hp = data['max_hp']
        self.expiration_date = data['expiration_date'] # created_at(day) minus expiration I know it's pseudo code, shut up.
        self.ingredient_model = None                # When we create the pantry_ingredient we will as part of the creation process be attaching a model of the "ideal" ingredient to the one in the pantry. This is where we will get our unit type, max hp, etc. 
        self.expires = None
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Create Pantry Ingredients Model 
    @classmethod
    def add_ingredient_to_pantry_by_id(cls, data):                 # Returns TRUE or FALSE
        query = """
            INSERT INTO pantry_ingredients 
                (
                    user_id, 
                    ingredient_id,
                    current_hp,
                    max_hp,
                    expiration_date
                ) 
            VALUES 
                (
                    %(user_id)s,
                    %(ingredient_id)s,
                    %(current_hp)s,
                    %(max_hp)s,
                    %(expiration_date)s
                )
            ;
            """
        model_ingredient = ingredient.Ingredient.get_ingredient_by_id(data['ingredient_id'])
        new_data = {
            'user_id' : data['user_id'],
            'ingredient_id' : data['ingredient_id'],
            'current_hp' : model_ingredient.max_hp,
            'max_hp' : model_ingredient.max_hp,
            'expiration_date' : date.today() + timedelta(model_ingredient.days_to_expire)
        }
        if not connectToMySQL(cls.db).query_db(query, new_data):
            return False
        return True
    

    # Read Users Models
    
    @classmethod
    def get_pantry_ingredient_by_id(cls,pantry_ingredient_id):
        data = {
            'id' : pantry_ingredient_id
        }
        query = """
        SELECT *
        FROM pantry_ingredients
        JOIN ingredients
        ON pantry_ingredients.ingredient_id = ingredients.id
        WHERE pantry_ingredients.id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        one_pantry_ingredient = cls(results[0])
        one_pantry_ingredient_data = {
            'id' : results[0]['pantry_ingredients.id'],
            'user_id' : results[0]['user_id'],
            'ingredient_id' : results[0]['pantry_ingredients.id'],
            'current_hp' : results[0]['current_hp'],
            'max_hp' : results[0]['pantry_ingredients.max_hp'],
            'expiration_date' : results[0]['expiration_date'],
            'created_at' : results[0]['pantry_ingredients.created_at'],
            'updated_at' : results[0]['pantry_ingredients.updated_at']
        }
        
        return one_pantry_ingredient
    
    @classmethod
    def get_pantry_deck_by_user_id(cls, user_id):
        data = {
            'user_id' : user_id
        }
        query = """
        SELECT *
        FROM pantry_ingredients
        WHERE pantry_ingredients.user_id = %(user_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_pantry_deck = []
        for row in results:
            one_pantry_deck.append(cls(row))
        return one_pantry_deck

    # Update Users Models
    @classmethod
    def reduce_hit_points(cls,hit_points,pantry_ingredient_id):
        current_hp = (cls.get_pantry_ingredient_by_id(pantry_ingredient_id)).current_hp - hit_points
        data = {
            'id' : pantry_ingredient_id,
            'current_hp' : current_hp
        }
        query = """
        UPDATE pantry_ingredients
        SET current_hp = %(current_hp)s
        WHERE id = %(id)s
        """
        connectToMySQL(cls.db).query_db(query, data)
        return

    @classmethod
    def update_pantry_ingredient_by_id(cls, pantry_ingredient_id):
        data = {
            'pantry_ingredient_id' : pantry_ingredient_id
        }
        query = """
        SELECT *
        FROM pantry_ingredients
        WHERE id = %(pantry_ingredient_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_pantry_ingredient = cls(results[0])
        return one_pantry_ingredient


    # Delete Users Models
    @classmethod
    def delete_user(cls, data):     # Returns nothing
        query = """
            DELETE FROM users
            WHERE id = %(id)s;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return

    # Validation Methods
