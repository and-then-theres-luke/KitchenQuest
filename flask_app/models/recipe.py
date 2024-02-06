from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, user, pantry_ingredient
from datetime import date, timedelta
from flask import flash, session
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
    def recipe_search(cls, search_string):
        search_string = search_string.lower()
        all_recipes = cls.get_all_recipes()
        search_results = []
        for one_recipe in all_recipes:
            result = re.search(search_string, one_recipe.name)
            if result == False:
                pass
            else:
                search_results.append(one_recipe)
        return search_results
    
    # Update Recipe Methods
    
    @classmethod
    def update_recipe(cls,data):
        pass
    
    # Delete Recipe Methods
    
    @classmethod
    def delete_recipe_by_id(cls,id):
        pass