
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



    # Read ingredients Model
    
    @classmethod
    def get_ingredient_by_api_ingredient_id(cls, api_ingredient_id):
        res = requests.get("https://api.spoonacular.com/food/ingredients/" + api_ingredient_id + "/information?apiKey=" + API_KEY)
        one_ingredient = res.json()
        data = {
            'api_ingredient_id' : one_ingredient['id'],
            'name' : one_ingredient['name'],
            'aisle' : one_ingredient['aisle'],
            'image' : one_ingredient['image']
        }
        return cls(data)