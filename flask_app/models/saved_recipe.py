from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, spell, user
from datetime import date, timedelta
from flask import flash, session
from flask_app.api_key import API_KEY
import requests
import re



## ATTENTION
# This is an API class, it only contains methods for returning JSON objects from the API.
# Users cannot delete, update, or create recipes as the API database is READ ONLY.

class Saved_Recipe:
    def __init__(self, data):
        [
            id,
            user_id,
            api_recipe_id,
            created_at,
            updated_at
        ] = data
        self.id = id
        self.user_id = user_id
        self.api_recipe_id = api_recipe_id
        self.created_at = created_at
        self.updated_at = updated_at
        
        # CREATE Saved_Recipe Method
        @classmethod
        def create_new_favorite(cls, data):
            query = """
            INSERT INTO saved_recipes 
            (
                user_id,
                api_recipe_id
            )
            VALUES
            (
                %(user_id)s,
                %(api_recipe_id)s
            )
            ;
            """
            connectToMySQL(cls.db).query_db(query, data)
            return
        
        
        # R
        
        @classmethod
        def get_one_saved_recipe(cls, id):
            data = {
                'id' : id
            }
            query = """
            SELECT *
            FROM saved_recipes
            WHERE id = %(id)s
            ;
            """
            one_recipe = connectToMySQL(cls.db).query_db(query, data)
            return one_recipe
        
        @classmethod
        def get_all_saved_recipes_by_user_id(cls, user_id):
            data = {
                'user_id' : user_id
            }
            query = """
            SELECT *
            FROM saved_recipes
            WHERE saved_recipes.user_id = %(user_id)s
            ;
            """
            all_saved_recipes = []
            results = connectToMySQL(cls.db).query_db(query, data)
            for row in results:
                all_saved_recipes.append(cls(row))
            return all_saved_recipes
            
        # U
        
        
        # D
        @classmethod
        def delete_saved_recipe_by_id(cls, recipe_id):
            data = {
                'id' : recipe_id
            }
            query = """
            DELETE FROM saved_recipes
            WHERE id = %(id)s
            ;
            """
            connectToMySQL(cls.db).query_db(query, data)
            return