from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, spell, recipe
from flask import flash, session
from flask_app.api_key import API_KEY
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
        self.extendedIngredients = data['extendedIngredients']

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
            'extendedIngredients' : one_recipe['extendedIngredients'],
        }
        one_recipe = cls(data)
        return one_recipe

        # Read Recipe

    
    @classmethod
    def recipe_to_boss_conversion_handler(cls, api_recipe_id):
        one_recipe = recipe.Recipe.get_recipe_by_api_recipe_id_raw_data(api_recipe_id)
        spellbook = spell.Spell.get_spellbook_by_user_id(session['user_id'])
        cls.convert_ingredients(one_recipe, spellbook)
    
    @classmethod
    def spell_check(cls, df, spellbook):
        for x in range(0, len(df.index)):
            for one_spell in spellbook:
                if df.loc[x]['id'] == one_spell.api_ingredient_id:
                    df.loc[x]['isSpell'] = True
                    break
                else:
                    df.loc[x]['isSpell'] = False
        returned_dict = df.to_dict(orient='records', index=True)
        print(returned_dict)
        return returned_dict
    
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
    
    @classmethod
    def convert_amounts(cls, one_ingredient, one_spell):
        if one_ingredient['unit'] != one_spell.charge_unit and one_ingredient['unit'] != (f"""{one_spell.charge_unit}s"""):
            if one_ingredient['unit'] != "":
                one_ingredient['charge_amount'] = ingredient.Ingredient.convert_amounts(one_ingredient['id'],one_spell.charge_amount, one_spell.charge_unit, one_ingredient['unit'])
                one_ingredient['charge_unit'] = one_ingredient['unit']
            elif one_ingredient['unit'] == "":
                one_ingredient['charge_amount'] = ingredient.Ingredient.convert_amounts(one_ingredient['id'],one_spell.charge_amount, one_spell.charge_unit, "serving")
                one_ingredient['charge_amount'] = float(one_ingredient['amount']) / float(one_spell.charge_amount)
        else:
            if one_ingredient['unit'] != "":
                one_ingredient['charge_amount'] = ingredient.Ingredient.convert_amounts(one_ingredient['id'],one_spell.charge_amount, one_spell.charge_unit, one_ingredient['unit'])
            one_ingredient['charge_unit'] = one_spell.charge_unit
            one_ingredient['charges_needed'] = float(one_ingredient['amount']) / float(one_spell.charge_amount)
    

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
