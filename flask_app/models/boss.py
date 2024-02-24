from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, spell, user, recipe
from datetime import date, timedelta
from flask import flash, session
from flask_app.api_key import API_KEY
import re



## ATTENTION
# This is an SQL class, it's responsible for storing information in our database and converting them from API classes

class Boss:
    db = "kitchenquest"
    def __init__(self, data):
        [id, user_id, api_recipe_id, xp_value, created_at, updated_at] = data
        self.id = id
        self.user_id = user_id
        self.api_recipe_id = api_recipe_id
        self.xp_value = xp_value
        self.spells_needed = []
        self.created_at = created_at
        self.updated_at = updated_at
    
    
    
    # Create Boss Method
    
    @classmethod
    def convert_recipe_to_boss(cls, api_recipe_id):
        one_recipe = recipe.Recipe.get_recipe_by_api_recipe_id(api_recipe_id)
        one_boss = None
        data = {}
        xp_value = 0
        for ingredient in one_recipe.extendedIngredients:
            data.spells
            xp_value += 25
            
        
        
    
    @classmethod
    def create_boss(cls, data):
        query = """
        INSERT INTO bosses
        (
            user_id,
            api_recipe_id,
            xp_value
        )
        VALUES
        (
            %(user_id)s,
            %(api_recipe_id)s,
            %(xp_value)s
        )
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    # Read Boss
    
    @classmethod
    def get_one_boss_by_id(cls, boss_id):
        data = {
            'id' : boss_id
        }
        query = """
        SELECT *
        FROM bosses
        WHERE id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_boss = cls(results[0])
        recipe_model = recipe.Recipe.get_recipe_by_api_recipe_id(one_boss.api_recipe_id)
        for ingredient in recipe_model.extended_ingredients:
            one_boss.spells_needed.append(recipe.Recipe(ingredient))
        print(one_boss.spells_needed)
        return one_boss
        
    @classmethod
    def get_all_bosses_by_user_id(cls, user_id):
        data = {
            'id' : user_id
        }
        query = """
        SELECT *
        FROM bosses
        WHERE id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        all_bosses = []
        for boss in results:
            all_bosses.append(cls(boss))
        return all_bosses