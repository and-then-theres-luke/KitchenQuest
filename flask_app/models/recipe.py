from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, spell, recipe
from flask import flash, session
from flask_app.api_key import API_KEY
import pandas as pd
import requests



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
        # Here is where I could potentially parse out each individual ingredient.
        one_recipe = cls(data)
        return one_recipe

    # Read Recipe
    
    @classmethod
    def create_recipe_table(cls, one_recipe, spellbook):
        res = requests.get(
                            'https://api.spoonacular.com/recipes/' +
                            str(one_recipe.id) +
                            '/information?includeNutrition=false&apiKey=' + 
                            API_KEY)
        the_box = res.json()
        df_box = pd.json_normalize(the_box['extendedIngredients'])
        df_spellbook = pd.DataFrame(spellbook)
        for i in df_box.index: # Gonna start a loop here... it will check to see if the spell is in the table one by one
            if df_box['id'][i] % 2 == 0:
                df_box['Blangus'][i] == 'Spell'
                print(df_box['Blangus'][i])
            else:
                df_box['Blangus'][i] == 'Not Spell'
                print(df_box['Blangus'][i])
        print(df_spellbook.info())
        
        
        return
        
    
    @classmethod
    def recipe_to_boss_conversion_handler(cls, api_recipe_id):
        one_recipe = recipe.Recipe.get_recipe_by_api_recipe_id(api_recipe_id)
        spellbook = spell.Spell.get_spellbook_by_user_id(session['user_id'])
        return one_recipe, spellbook
    
    @classmethod
    def convert_ingredients(cls, one_recipe, spellbook):
        for one_ingredient in one_recipe['extendedIngredients']:
            cls.convert_ingredient(one_ingredient, spellbook)
    
    @classmethod
    def convert_ingredient(cls, one_ingredient, spellbook):
        if not spellbook:
            one_ingredient['isSpell'] = False
        else:
            for one_spell in spellbook:
                if one_ingredient['id'] == one_spell.api_ingredient_id:
                    one_ingredient['isSpell'] = True
                    cls.convert_amounts(one_ingredient, one_spell)
                    break
                else:
                    one_ingredient['isSpell'] = False
                    one_ingredient['charge_amount'] = ""
                    one_ingredient['charge_unit'] = one_ingredient['unit']
    
    # @classmethod
    # def convert_amounts(cls, one_ingredient, one_spell):
    #     if one_ingredient['unit'] != one_spell.charge_unit and one_ingredient['unit'] != (f"""{one_spell.charge_unit}s"""):
    #         if one_ingredient['unit'] != "":
    #             one_ingredient['charge_amount'] = ingredient.Ingredient.convert_amounts(one_ingredient['id'],one_spell.charge_amount, one_spell.charge_unit, one_ingredient['unit'])
    #             one_ingredient['charge_unit'] = one_ingredient['unit']
    #         elif one_ingredient['unit'] == "":
    #             one_ingredient['charge_amount'] = ingredient.Ingredient.convert_amounts(one_ingredient['id'],one_spell.charge_amount, one_spell.charge_unit, "serving")
    #             one_ingredient['charge_amount'] = float(one_ingredient['amount']) / float(one_spell.charge_amount)
    #     else:
    #         if one_ingredient['unit'] != "":
    #             one_ingredient['charge_amount'] = ingredient.Ingredient.convert_amounts(one_ingredient['id'],one_spell.charge_amount, one_spell.charge_unit, one_ingredient['unit'])
    #         one_ingredient['charge_unit'] = one_spell.charge_unit
    #         one_ingredient['charges_needed'] = float(one_ingredient['amount']) / float(one_spell.charge_amount)
    

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