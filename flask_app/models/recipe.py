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

class Recipe:
    db = "kitchenquest"
    def __init__(self, data):
        [
            id, 
            title, 
            image, 
            imageType, 
            servings, 
            readyInMinutes, 
            license, 
            sourceName, 
            sourceURL, 
            creditsText, 
            extendedIngredients, 
            summary] = data
        self.id = id
        self.title = title
        self.image = image
        self.image_type = imageType
        self.servings = servings
        self.ready_in_minutes = readyInMinutes
        self.license = license
        self.source_name = sourceName
        self.source_url = sourceURL
        self.credits_text = creditsText
        self.extended_ingredients = extendedIngredients
        self.summary = summary
        
        
        

    # Read Recipe
    @classmethod
    def get_recipe_by_api_recipe_id(cls, api_recipe_id):
        res = requests.get(
                            'https://api.spoonacular.com/recipes/' +
                            str(api_recipe_id) +
                            '/information?includeNutrition=false&apiKey=' + 
                            API_KEY)
        expected_data = res.json()
        print(expected_data)
        new_data = {
            'id' : expected_data['id'], 
            'title' : expected_data['title'], 
            'image' : expected_data['image'], 
            'image_type' : expected_data['imageType'], 
            'servings' : expected_data['servings'], 
            'ready_in_minutes' : expected_data['readyInMinutes'], 
            'license' : expected_data['license'], 
            'source_name' : expected_data['sourceName'], 
            'source_url' : expected_data['sourceURL'], 
            'credits_text' : expected_data['creditsText'], 
            'ingredients' : expected_data['extendedIngredients'],
            'summary' : expected_data['summary']
        }
        one_recipe = cls(new_data)
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