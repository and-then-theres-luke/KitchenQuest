
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, request
import requests
from flask_app.api_key import API_KEY
import re

## ATTENTION
# This is an API class, it only contains methods for returning JSON objects from the API.
# Users cannot delete, update, or create ingredients as the API database is READ ONLY.

class Ingredient:
    db = "kitchenquest" #which database are you using for this project
    def __init__(self, data):
        self.api_ingredient_id = data['api_ingredient_id']
        self.name = data['name']
        self.aisle = data['aisle']
        self.image = data['image']
        self.possibleUnits = data['possibleUnits']



    # Read ingredients Model
    
    @classmethod
    def get_ingredient_by_api_ingredient_id(cls, api_ingredient_id):
        res = requests.get("https://api.spoonacular.com/food/ingredients/" + api_ingredient_id + "/information?apiKey=" + API_KEY)
        one_ingredient = res.json()
        data = {
            'api_ingredient_id' : one_ingredient['id'],
            'name' : one_ingredient['name'],
            'aisle' : one_ingredient['aisle'],
            'image' : one_ingredient['image'],
            'possibleUnits' : one_ingredient['possibleUnits']
        }
        return cls(data)
    
    @staticmethod
    def convert_amounts(api_ingredient_id, charge_amount, charge_unit, target_unit):
        print(api_ingredient_id, charge_amount, charge_unit, target_unit)
        if target_unit == "":
            targetAmount = charge_amount
        else:
            query = """https://api.spoonacular.com/recipes/convert?ingredientName=""" + str(api_ingredient_id) + """&sourceAmount=""" + str(charge_amount) + """&sourceUnit=""" + str(charge_unit) + """&targetUnit=""" + str(target_unit) + """&apiKey=""" + str(API_KEY)
            print("Converting " + str(charge_amount) + " " + str(charge_unit) + "to " + str(target_unit))
            res = requests.get(query)
            results = res.json()
            print(results)
            targetAmount = results['targetAmount']
            print("Result is: " + str(charge_amount) + " " + str(charge_unit) + " is equal to " + str(targetAmount) + " " + str(target_unit))
        return targetAmount