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
        else:
            for one_ingredient in one_recipe['extendedIngredients']:
                for one_spell in spellbook:
                    if one_ingredient['id'] == one_spell.api_ingredient_id:
                        one_ingredient['isSpell'] = True
                        # This is an if/else statement that checks to see if the unit types match
                        if one_ingredient['unit'] != one_spell.charge_unit and one_ingredient['unit'] != (f"""{one_spell.charge_unit}s"""):
                            # Finding that the ingredient is a spell, and the conversion units do not match, we put in the values of the ingredient as the {unit} and {amount} and the {charge_unit} we wish to convert to, then returns the value of the new unit.
                            if one_ingredient['unit'] != "":
                                one_ingredient['charge_amount'] = ingredient.Ingredient.convert_amounts(one_ingredient['id'],one_spell.charge_amount, one_spell.charge_unit, one_ingredient['unit'])
                                one_ingredient['charge_unit'] = one_ingredient['unit']
                            # If the unit types match, we just do the math an pass in the values for the charges needed
                            elif one_ingredient['unit'] == "":
                                one_ingredient['charge_amount'] = ingredient.Ingredient.convert_amounts(one_ingredient['id'],one_spell.charge_amount, one_spell.charge_unit, "serving")
                                one_ingredient['charge_amount'] = float(one_ingredient['amount']) / float(one_spell.charge_amount)
                            # Now we return all four values: the {amount} and {unit} the recipe calls for, and the {charge_amount} and {charge_unit} of one charge. These are static values.
                        else:
                            if one_ingredient['unit'] != "":
                                one_ingredient['charge_amount'] = ingredient.Ingredient.convert_amounts(one_ingredient['id'],one_spell.charge_amount, one_spell.charge_unit, one_ingredient['unit'])
                            one_ingredient['charge_unit'] = one_spell.charge_unit
                            one_ingredient['charges_needed'] = float(one_ingredient['amount']) / float(one_spell.charge_amount)
                    else:
                        # If the spell isn't found, we pass in that the spell is False, set the charge to "" and set the unit to whatever the ingredient unit is.
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
