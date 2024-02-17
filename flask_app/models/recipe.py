from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, user, pantry_ingredient
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
        self.comments = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # Create Recipe Models
    @classmethod
    def create_recipe(cls, data):
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
    
    def create_recipe_no_image(cls, data):
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
        data = {
            'recipe_id' : recipe_id
        }
        query = """
        SELECT *
        FROM recipes
        WHERE id = %(recipe_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_recipe = cls(results[0])
        return one_recipe
    
    @classmethod
    def get_all_recipes(cls):
        query = """
        SELECT *
        FROM recipes
        ;
        """
        all_recipes = []
        results = connectToMySQL(cls.db).query_db(query)
        for row in results:
            all_recipes.append(cls(row))
        return all_recipes
    
    @classmethod
    def get_all_recipes_by_user_id(cls, user_id):
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