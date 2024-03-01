from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, spell, user, recipe, boss
from datetime import date, timedelta
from flask import flash, session
from flask_app.api_key import API_KEY
import requests
import re



## ATTENTION
# This is an API class, it only contains methods for returning JSON objects from the API.
# Users cannot delete, update, or create recipes as the API database is READ ONLY.

class Recipe:
    db = "kitchenquest"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.image = data['image']
        self.imageType = data['imageType']
        self.servings = data['servings']
        self.readyInMinutes = data['readyInMinutes']
        self.extendedIngredients = data['extendedIngredients']
        self.summary = data['summary']

    # Read Recipe
    @classmethod
    def get_recipe_by_api_recipe_id(cls, api_recipe_id):
        res = requests.get(
                            'https://api.spoonacular.com/recipes/' +
                            str(api_recipe_id) +
                            '/information?includeNutrition=false&apiKey=' + 
                            API_KEY)
        one_recipe = res.json()
        data = {
            'id' : one_recipe['id'], 
            'title' : one_recipe['title'], 
            'image' : one_recipe['image'], 
            'imageType' : one_recipe['imageType'], 
            'servings' : one_recipe['servings'], 
            'readyInMinutes' : one_recipe['readyInMinutes'], 
            'extendedIngredients' : one_recipe['extendedIngredients'],
            'summary' : one_recipe['summary']
        }
        one_recipe = cls(data)
        return one_recipe

        # Read Recipe
    @classmethod
    def get_recipe_by_api_recipe_id_raw_data(cls, api_recipe_id):
        res = requests.get(
                            'https://api.spoonacular.com/recipes/' +
                            str(api_recipe_id) +
                            '/information?includeNutrition=false&apiKey=' + 
                            API_KEY)
        one_recipe = res.json()
        data = {
            'id' : one_recipe['id'], 
            'title' : one_recipe['title'], 
            'image' : one_recipe['image'], 
            'extendedIngredients' : one_recipe['extendedIngredients'],
        }
        return data
    
    @classmethod
    def recipe_boss_conversion_handler(cls, api_recipe_id):
        one_recipe = recipe.Recipe.get_recipe_by_api_recipe_id_raw_data(api_recipe_id)
        spellbook = spell.Spell.get_spellbook_by_user_id(session['user_id'])
        if spellbook == []:
            for one_ingredient in one_recipe['extendedIngredients']:
                one_ingredient['isSpell'] = False
                one_ingredient['charge_amount'] = ""
                one_ingredient['charge_unit'] = one_ingredient['unit']
        for one_ingredient in one_recipe['extendedIngredients']:
            for one_spell in spellbook:
                if one_ingredient['id'] == one_spell.api_ingredient_id:
                    one_ingredient['isSpell'] = "True"
                    if one_ingredient['unit'] != one_spell.charge_unit and one_ingredient['unit'] != (f"""{one_spell.charge_unit}s"""):
                        # Finding that the ingredient is a spell, and the conversion units do not match...
                        # We put in the values of the ingredient as the {unit} and {amount} and the {charge_unit} we wish to convert to, then returns the value of the new unit.
                        one_ingredient['charge_amount'] = ingredient.Ingredient.convert_amounts(one_ingredient['id'],one_spell.charge_amount, one_spell.charge_unit, one_ingredient['unit'])
                        # Now we return all four values: the {amount} and {unit} the recipe calls for, and the {charge_amount} and {charge_unit} of one charge. These are static values.
                    else:
                        one_ingredient['charge_amount'] = one_spell.charge_amount
                        one_ingredient['charge_unit'] = one_spell.charge_unit
                        # Now, if we have a match for units, it looks a little different
                        
                else:
                    one_ingredient['isSpell'] = False
                    one_ingredient['charge_amount'] = ""
                    one_ingredient['charge_unit'] = one_ingredient['unit']
        return one_recipe
    

    @classmethod
    def recipe_search(cls, search_string):
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