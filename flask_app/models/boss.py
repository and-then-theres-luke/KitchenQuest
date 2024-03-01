from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, spell, user, recipe, required_spells
from datetime import date, timedelta
from flask import flash, session
from flask_app.api_key import API_KEY
import re



## ATTENTION
# This is an SQL class, it's responsible for storing information in our database and converting them from API classes

class Boss:
    db = "kitchenquest"
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.api_recipe_id = data['api_recipe_id']
        self.title = data['title']
        self.xp_value = data['xp_value']
        self.image_url = data['image_url']
        self.spells_needed = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    
    
    # Create Boss Method
    @classmethod
    def create_boss_with_required_spells(cls, inputs):
        cleaned_inputs = []
        for item in inputs:
            cleaned_inputs.append(inputs[item])
        # xp_value = 0
        # for row in inputs:
        #     xp_value += 1
        # xp_value = (xp_value / 6) * 25
        # boss_data = {
        #     'user_id' : session['user_id'],
        #     'api_recipe_id' : inputs['api_recipe_id'], # Index 0
        #     'title' : inputs['title'], # Index 1
        #     'image_url' : inputs['image_url'], # Index 2
        #     'xp_value' : xp_value
        # }
        # boss_id = cls.create_boss(boss_data)
        ingredient_data = {
            'boss_id' : 1,
        }
        index = 3
        while (index < len(cleaned_inputs)-1):
            ingredient_data['api_ingredient_id'] = cleaned_inputs[index]
            ingredient_data['name'] = cleaned_inputs[index+1]
            ingredient_data['amount'] = cleaned_inputs[index+2]
            ingredient_data['unit'] = cleaned_inputs[index+3]
            ingredient_data['charge_unit'] = cleaned_inputs[index+4]
            ingredient_data['charge_amount'] = cleaned_inputs[index+5]
            ingredient_data['charges_needed'] = float(cleaned_inputs[index+2]) / float(cleaned_inputs[index+5])
            index += 6
            required_spells.Required_Spells.create_required_spell(ingredient_data)
        
    
    @classmethod
    def create_boss(cls, data):
        query = """
        INSERT INTO bosses
        (
            user_id,
            api_recipe_id,
            title,
            xp_value,
            image_url
        )
        VALUES
        (
            %(user_id)s,
            %(api_recipe_id)s,
            %(title)s,
            %(xp_value)s,
            %(image_url)s
        )
        ;
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
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
        WHERE user_id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        all_bosses = []
        for row in results:
            all_bosses.append(cls(row))
        return all_bosses
    
    @classmethod
    def get_boss_by_user_match_and_api_recipe_id(cls, user_id,api_recipe_id):
        data = {
            'user_id' : user_id,
            'api_recipe_id' : api_recipe_id
        }
        query = """
        SELECT *
        FROM bosses
        WHERE user_id = %(user_id)s
        AND api_recipe_id = %(api_recipe_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return cls(results[0])