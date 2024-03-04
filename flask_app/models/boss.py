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
        self.required_spells = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    
    
    # Create Boss Method
    @classmethod
    def create_boss_with_required_spells(cls, inputs):
        cleaned_inputs = []
        for item in inputs:
            cleaned_inputs.append(inputs[item])
        xp_value = 0
        for row in inputs:
            xp_value += 1
        xp_value = (xp_value / 6) * 25
        boss_data = {
            'user_id' : session['user_id'],
            'api_recipe_id' : inputs['api_recipe_id'], # Index 0
            'title' : inputs['title'], # Index 1
            'image_url' : inputs['image_url'], # Index 2
            'xp_value' : xp_value
        }
        boss_id = cls.create_boss(boss_data)
        ingredient_data = {
            'boss_id' : boss_id,
        }
        index = 3
        while (index < len(cleaned_inputs)-1):
            ingredient_data['api_ingredient_id'] = cleaned_inputs[index]
            ingredient_data['name'] = cleaned_inputs[index+1]
            ingredient_data['amount'] = cleaned_inputs[index+2]
            ingredient_data['unit'] = cleaned_inputs[index+3]
            index += 4
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
        JOIN required_spells
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
            list_of_required_spells.append(required_spells.Required_Spells(required_spell_data))
        spellbook = spell.Spell.get_spellbook_by_user_id(session['user_id'])
        for one_required_spell in list_of_required_spells:
            print("Running loop for required spell", one_required_spell.name)
            isSpell = False
            isEnoughCharges = False
            for one_spell in spellbook:
                if one_required_spell.api_ingredient_id == one_spell.api_ingredient_id:
                    isSpell = True
                    one_required_spell.charge_amount = ingredient.Ingredient.convert_amounts(one_required_spell.api_ingredient_id, one_spell.charge_amount, one_spell.charge_unit, one_required_spell.unit)
                    one_required_spell.charge_unit = one_required_spell.unit
                    # Converts the charge amount and charge unit from the spell to be read in an understandable way by the program
                    if one_required_spell.charge_amount <= 0:
                        one_required_spell.charge_amount = 0.01
                    one_required_spell.charges_needed = one_required_spell.amount / one_required_spell.charge_amount
                    if one_spell.current_charges >= one_required_spell.charges_needed:
                        isEnoughCharges = True
            one_required_spell.isSpell = isSpell
            one_required_spell.isEnoughCharges = isEnoughCharges
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
    
    @classmethod
    def defeat_boss(cls, boss_id):
        isBeaten = True
        one_boss = cls.get_one_boss_by_id(boss_id)
        spellbook = spell.Spell.get_spellbook_by_user_id(session['user_id'])
        for one_required_spell in one_boss.required_spells:
            print(one_required_spell)
            for one_spell in spellbook:
                print(one_spell)
                if one_spell.api_ingredient_id == one_required_spell.api_ingredient_id:
                    print("Match!")
                    if one_required_spell.charges_needed < one_spell.current_charges:
                        flash("Missing spells, cannot perform.")
                        isBeaten = False
                    else:
                        if not spell.Spell.reduce_charges(one_spell.id, one_spell.current_charges, one_required_spell.charges_needed):
                            flash("Not enough charges in your " + one_spell.name + " spell.")
                            isBeaten = False
                    break
                else:
                    print("no match found...")
        if isBeaten == True:
            print("have some experience points!")
            user.User.gain_xp(one_boss.xp_value)
        return isBeaten
        
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