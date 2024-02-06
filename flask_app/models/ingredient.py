
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re


class Ingredient:
    db = "kitchenquest" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.category_id = data['category_id']
        self.quantity_type_id = data['quantity_type_id']
        self.name = data['name']
        self.days_to_expire = data['days_to_expire']
        self.max_hp = data['max_hp']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?
        # When a new pantry ingredient is created, we construct it using the same information from ingredients        


    # Create Ingredient Models 
    @classmethod
    def create_ingredient(cls):
        query = """
        INSERT INTO ingredients
        (
            category_id,
            quantity_type_id,
            name,
            days_to_expire,
            max_hp
        )
        VALUES 
        (
            %(category_id)s,
            %(quanitity_type_id)s,
            %(name)s,
            %(days_to_expire)s,
            %(max_hp)s
        )
        ;
        """
        if not connectToMySQL(cls.db).query_db(query):
            return False
        return True

    # Read ingredients Models
    @classmethod
    def get_all_ingredients(cls):
        query = """
            SELECT * 
            FROM ingredients
            ;
            """
        results = connectToMySQL(cls.db).query_db(query)
        ingredients = []
        for row in results:
            ingredients.append(cls(row))
        return ingredients
    
    @classmethod
    def get_ingredient_by_category(cls, category_id):
        data = {
            'category_id' : category_id
        }
        query = """
        SELECT *
        FROM ingredients
        WHERE category_id = %(category_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        ingredients_by_category = []    
        for row in results:
            ingredients_by_category.append(cls(row))
        return ingredients_by_category
    
    @classmethod
    def ingredient_search(cls, search_string):
        search_string = search_string.lower()
        all_ingredients = cls.get_all_ingredients()
        search_results = []
        for one_ingredient in all_ingredients:
            result = re.search(search_string, one_ingredient.name)
            if result == False:
                pass
            else:
                search_results.append(one_ingredient)
        return search_results
    
    @classmethod
    def get_ingredient_by_name(cls, ingredient_name):
        data = {
            'name' : ingredient_name
        }
        query = """
        SELECT *
        FROM ingredients
        WHERE name = %(name)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_ingredient = cls(results[0])
        return one_ingredient
            

    @classmethod
    def get_ingredient_by_id(cls, id):
        data = {
            'id' : id
        }
        query = """
            SELECT *
            FROM ingredients
            WHERE id = %(id)s
            ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        one_ingredient = cls(results[0])
        return one_ingredient
    



    # Update ingredients Models
    @classmethod
    def update_ingredient(cls, data):              # Returns nothing
        query = """
            UPDATE ingredients
            SET first_name = %(first_name)s, 
            last_name = %(last_name)s, 
            email = %(email)s,
            password = %(password)s,
            WHERE id = %(id)s
            ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return


    # Delete ingredients Models
    @classmethod
    def delete_ingredient(cls, data):     # Returns nothing
        query = """
            DELETE FROM ingredients
            WHERE id = %(id)s;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    # Validation Methods
    