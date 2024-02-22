from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, spell, user
from datetime import date, timedelta
from flask import flash, session
from flask_app.api_key import API_KEY
import requests
import re


class Recipe:
    db = "kitchenquest"
    def __init__(self, data):
        self.name = data['name']
        self.image_url = data['image_url']
        self.instructions = data['instructions']
        self.recipe_ingredients = []
        self.optional_ingredients = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
        
        
        

    
    ## DATABASE QUERIES
    # Create Recipe Models
    @classmethod
    def create_custom_recipe(cls, data):
        query = """
        INSERT INTO recipes
        (
            name,
            image_url,
            instructions,
        )
        VALUES
        (
            %(name)s,
            %(image_url)s,
            %(instructions)s
        )
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    # Read Recipe Models
    @classmethod
    def get_recipe_by_id(cls, recipe_id):
        res = requests.get(
                            'https://api.spoonacular.com/recipes/' +
                            str(recipe_id) +
                            '/information?includeNutrition=false&apiKey=' + 
                            API_KEY)
        recipe_object = res.json()
        return recipe_object
    
    # Read Recipe Models
    @classmethod
    def get_all_custom_recipes_by_user_id(cls, user_id):
        data = {
            'id' : user_id
        }
        query = """
        SELECT *
        FROM recipes
        WHERE id = %(id)s
        ;
        """
        all_recipes = []
        results = connectToMySQL(cls.db).query_db(query, data)
        for row in results:
            all_recipes.append(cls(row))
        return all_recipes
    
    @classmethod
    def get_all_saved_recipes_by_user_id(cls, user_id):
        data = {
            'id' : user_id
        }
        query = """
        SELECT 
            recipes.id,
            recipes.name,
            recipes.image_url,
            recipes.instructions,
            recipes.created_at,
            recipes.updated_at
        FROM users
        LEFT JOIN saved_recipes
        ON users.id = saved_recipes.user_id
        LEFT JOIN recipes
        ON saved_recipes.recipe_id = recipes.id
        WHERE users.id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        all_saved_recipes = []
        if not results:
            return all_saved_recipes
        for row in results:
            all_saved_recipes.append(cls(row))
        return all_saved_recipes
    
    # Update Recipe Models
    @classmethod
    def update_custom_recipe(cls, recipe_id):
        pass
    
    ## API QUERIES
    
    
    
    
    
    
    
    
    
    
    
    
    

    @classmethod
    def recipe_search_by_ingredients(cls, search_string):
        search_string.replace(" ", "+")
        res = requests.get("""
                            https://api.spoonacular.com/recipes/findByIngredients
                            ?ingredients=" + {search_string} +
                            "&apiKey=" + {API_KEY}
                            """ )
        search_results = res.json()
        return search_results
    
    # Update Recipe Methods
    
    @classmethod
    def update_recipe(cls,data):
        pass
    
    # Delete Recipe Methods
    
    @classmethod
    def delete_recipe_by_id(cls,id):
        pass