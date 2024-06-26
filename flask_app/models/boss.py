from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, required_spell, spell, user, recipe
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
        self.required_spells = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    
    
    # Create Boss Method
    @classmethod
    def create_boss_with_required_spells(cls, api_recipe_id):
        one_recipe = recipe.Recipe.get_recipe_by_api_recipe_id(api_recipe_id)
        xp_value = 0
        for _ in one_recipe.extendedIngredients:
            xp_value += 1
        xp_value = (xp_value / 6) * 25
        boss_data = {
            'user_id' : session['user_id'],
            'api_recipe_id' : api_recipe_id,
            'title' : one_recipe['title'],
            'image_url' : one_recipe['image_url'],
            'xp_value' : xp_value
        }
        boss_id = cls.create_boss(boss_data)
        for ingredient in one_recipe.extendedIngredients:
            data = {
                "boss_id" : boss_id,
                "api_ingredient_id" : ingredient.id,
                "name" : ingredient.name,
                "amount" : ingredient.amount,
                "unit" : ingredient.unit
            }
            print(data)
            # required_spell.Required_Spell.create_required_spell(data)
        return
        
    
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
        LEFT JOIN required_spells
        ON bosses.id = required_spells.boss_id
        WHERE bosses.id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        boss_data = {
            'id' : boss_id,
            'title' : results[0]['title'],
            'user_id' : results[0]['user_id'],
            'api_recipe_id' : results[0]['api_recipe_id'],
            'xp_value' : results[0]['xp_value'],
            'image_url' : results[0]['image_url'],
            'created_at' : results[0]['created_at'],
            'updated_at' : results[0]['updated_at']
        }
        one_boss = cls(boss_data)
        list_of_required_spells = []
        if results[0]['required_spells.id'] == None:
            return one_boss
        for row in results:
            required_spell_data = {
                'id' : row['required_spells.id'],
                'boss_id' : boss_id,
                'api_ingredient_id' : row['api_ingredient_id'],
                'name' : row['name'],
                'amount' : row['amount'],
                'unit' : row['unit'],
                'created_at' : row['required_spells.created_at'],
                'updated_at' : row['required_spells.updated_at']
            }
            list_of_required_spells.append(required_spell.Required_Spell(required_spell_data))
        spellbook = spell.Spell.get_spellbook_by_user_id(session['user_id'])
        list_of_required_spells = cls.check_for_required_spells(spellbook, list_of_required_spells)
        one_boss.required_spells = list_of_required_spells
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
        all_bosses = []
        for row in results:
            all_bosses.append(cls(row))
        return all_bosses
    
    # Update Methods
    
    
        
    # Delete Methods
        
    @classmethod
    def delete_boss(cls, id):
        data = {
            'id' : id
        }
        boss_query = """
        DELETE FROM bosses
        WHERE id = %(id)s
        ;"""
        required_spells_query = """
        DELETE FROM required_spells
        WHERE boss_id = %(id)s
        """
        connectToMySQL(cls.db).query_db(boss_query, data)
        connectToMySQL(cls.db).query_db(required_spells_query, data)
        return
    
    # Misc Methods
    
    @classmethod
    def check_for_required_spells(cls, spellbook, list_of_required_spells):
        for one_required_spell in list_of_required_spells:
            isSpell = False
            isEnoughCharges = False
            for one_spell in spellbook:
                if one_required_spell.api_ingredient_id == one_spell.api_ingredient_id:
                    isSpell = True
                    one_required_spell.charge_amount = ingredient.Ingredient.convert_amounts(one_required_spell.api_ingredient_id, one_spell.charge_amount, one_spell.charge_unit, one_required_spell.unit)
                    one_required_spell.charge_unit = one_required_spell.unit
                    # Converts the charge amount and charge unit from the spell to be read in an understandable way by the program
            one_required_spell.isSpell = isSpell
            if one_required_spell.isSpell == False:
                flash("Your " + one_required_spell.name + " spell lacks the required charges.")
            else:
                if one_required_spell.charge_amount <= 0:
                    one_required_spell.charge_amount = 0.01
                one_required_spell.charges_needed = one_required_spell.amount / one_required_spell.charge_amount
                if one_spell.current_charges >= one_required_spell.charges_needed:
                    isEnoughCharges = True
                else:
                    isEnoughCharges = False
            one_required_spell.isEnoughCharges = isEnoughCharges
        return list_of_required_spells
    
    
    
    @classmethod
    def defeat_boss(cls, boss_id):
        isBeaten = True
        one_boss = cls.get_one_boss_by_id(boss_id)
        spellbook = spell.Spell.get_spellbook_by_user_id(session['user_id'])
        list_of_required_spells = cls.check_for_required_spells(spellbook, one_boss.required_spells)
        for required_spell in list_of_required_spells:
            if required_spell.isEnoughCharges == False:
                isBeaten = False
            else:
                for one_spell in spellbook:
                    if one_spell.api_ingredient_id == required_spell.api_ingredient_id:
                        one_spell.current_charges -= required_spell.charges_needed
                        one_spell.update_charges(one_spell.id, one_spell.current_charges)
        if isBeaten == True:
            flash("Boss defeated! Gained " + str(one_boss.xp_value) + " experience points.")
            user.User.gain_xp(one_boss.xp_value)
        return isBeaten