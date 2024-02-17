
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
        self.isFrozen = data['isFrozen']
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
                    expiration_date,
                    isFrozen
                ) 
            VALUES 
                (
                    %(user_id)s,
                    %(ingredient_id)s,
                    %(current_hp)s,
                    %(max_hp)s,
                    %(expiration_date)s,
                    %(isFrozen)s
                )
            ;
            """
        if not connectToMySQL(cls.db).query_db(query, data):
            return False
        return True
    

    # Read Pantry Ingredient Models
    
    
    
    @classmethod
    def get_pantry_ingredient_by_pantry_ingredient_id(cls,pantry_ingredient_id):
        data = {
            'id' : pantry_ingredient_id
        }
        query = """
        SELECT *
        FROM pantry_ingredients
        WHERE pantry_ingredients.id = %(id)s
        ;
        """
        one_pantry_ingredient = connectToMySQL(cls.db).query_db(query, data)
        if not one_pantry_ingredient:
            return False
        return one_pantry_ingredient
    
    @classmethod
    def get_pantry_deck_by_user_id(cls, user_id):
        data = {
            'user_id' : user_id
        }
        query = """
        SELECT *
        FROM pantry_ingredients
        WHERE user_id = %(user_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_pantry_deck = []
        for row in results:
            one_pantry_deck.append(cls(row))
        return one_pantry_deck

    # Update Users Models
    @classmethod
    def reduce_hit_points(cls,hits,pantry_ingredient_id):
        data = {
            'id' : pantry_ingredient_id,
            'hits' : hits
        }
        query = """
        UPDATE pantry_ingredients
        SET current_hp = (current_hp - %(hits)s)
        WHERE id = %(id)s
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    @classmethod
    def freeze_or_defrost_ingredient(cls, pantry_ingredient_id, isFrozen):
        data = {
            'id' : pantry_ingredient_id
        }
        query = """
        UPDATE pantry_ingredients
        SET isFrozen = 1
        WHERE id = %(id)s
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return


    # Delete Users Models
    @classmethod
    def delete_pantry_ingredient_by_pantry_ingredient_id(cls,pantry_ingredient_id):
        query = """
        DELETE FROM pantry_ingredients
        WHERE id - %(id)s
        ;
        """
        data = {
            'id' : pantry_ingredient_id
        }
        connectToMySQL(cls.db).query_db(query, data)

    # Validation Methods
    @staticmethod
    def validate_new_pantry_ingredient(data):
        isValid = True
        if data['max_hp'] <= 0:
            flash("Your ingredient needs at least one hit point before you can add it to your pantry deck. Try again.","new_ingredient")
            isValid = False
        if data['expiration_date'] < date.today():
            flash("Expiration date cannot be in the future.","new_ingredient")
            isValid = False
        return isValid
    
    
        
        