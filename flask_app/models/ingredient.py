
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
        [
            id, 
            original, 
            originalName, 
            name, 
            amount, 
            unit, 
            possibleUnits, 
            shoppingListUnits, 
            aisle, 
            image, 
            categoryPath
            ] = data
        self.api_ingredient_id = id
        self.original = original
        self.originalName = originalName
        self.name = name
        self.amount = amount
        self.unit = unit
        self.possible_units = possibleUnits
        self.shopping_list_units = shoppingListUnits
        self.aisle = aisle
        self.image = image
        self.category_path = categoryPath



    # Read ingredients Model
    
    @classmethod
    def get_ingredient_by_api_ingredient_id(cls, id):
        res = requests.get("https://api.spoonacular.com/food/ingredients/" + id + "/information?apiKey=" + API_KEY)
        one_ingredient = res.json()
        cls(one_ingredient)
        return one_ingredient