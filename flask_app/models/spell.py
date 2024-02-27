
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, user
from datetime import date, timedelta
from flask import flash, session




class Spell:
    db = "kitchenquest" 
    def __init__(self, data):
        self.id = data['id']                        # ID for an ingredient in the pantry
        self.user_id = data['user_id']              # ID for the user whose pantry that ingredient is in
        self.api_ingredient_id = data['api_ingredient_id']  # ID for the actual ingredient data according to api
        self.name = data['name']
        self.charge_value = data['charge_value']
        self.charge_unit = data['charge_unit']
        self.current_charges = data['current_charges']
        self.max_charges = data['max_charges']
        self.expiration_date = data['expiration_date'] # created_at(day) minus expiration I know it's pseudo code, shut up.
        self.isFrozen = data['isFrozen']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']




    # Create Spell Model 
    @classmethod
    def create_spell(cls, data):                 # Returns TRUE or FALSE
        if data['isFrozen'] == "on":
            data['isFrozen'] = 1
        else:
            data['isFrozen'] = 0
        if not cls.validate_new_spell(data):
            return False
        query = """
            INSERT INTO spells 
                (
                    user_id, 
                    api_ingredient_id,
                    name,
                    current_charges,
                    max_charges,
                    charge_value,
                    charge_unit,
                    expiration_date,
                    isFrozen
                ) 
            VALUES 
                (
                    %(user_id)s,
                    %(api_ingredient_id)s,
                    %(name)s,
                    %(max_charges)s,
                    %(max_charges)s,
                    %(charge_value)s,
                    %(charge_unit)s,
                    %(expiration_date)s,
                    %(isFrozen)s
                )
            ;
            """
        if not connectToMySQL(cls.db).query_db(query, data):
            return False
        return True
    

    # Read Spell Models
    
    
    
    @classmethod
    def get_spell_by_id(cls,spell_id):
        data = {
            'id' : spell_id
        }
        query = """
        SELECT *
        FROM spells
        WHERE spells.id = %(id)s
        ;
        """
        one_spell = connectToMySQL(cls.db).query_db(query, data)
        if not one_spell:
            return False
        return one_spell
    
    @classmethod
    def get_spellbook_by_user_id(cls, user_id):
        data = {
            'user_id' : user_id
        }
        query = """
        SELECT *
        FROM spells
        WHERE user_id = %(user_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_spellbook = []
        for row in results:
            one_spellbook.append(cls(row))
        return one_spellbook

    @classmethod
    def get_spellbook_by_user_id_raw_data(cls, user_id):
        data = {
            'user_id' : user_id
        }
        query = """
        SELECT *
        FROM spells
        WHERE user_id = %(user_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_spellbook = []
        for row in results:
            one_spellbook.append(row)
        return one_spellbook
    
    # Update Spell Models
    @classmethod
    def reduce_charges(cls,hits,spell_id):
        if not cls.validate_hits(hits,spell_id):
            return False
        data = {
            'id' : spell_id,
            'hits' : hits
        }
        query = """
        UPDATE spells
        SET current_charges = (current_charges - %(hits)s)
        WHERE id = %(id)s
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    @classmethod
    def freeze_or_defrost_ingredient(cls, pantry_ingredient_id, isFrozen):
        if isFrozen:
            isFrozen = 0
        else:
            isFrozen = 1
        data = {
            'id' : pantry_ingredient_id,
            'isFrozen' : isFrozen
        }
        query = """
        UPDATE spells
        SET isFrozen = %(isFrozen)s
        WHERE id = %(id)s
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return


    # Delete Spell Models
    @classmethod
    def delete_spell_by_id(cls,spell_id):
        data = {
            'id' : spell_id
        }
        query = """
        DELETE FROM spells
        WHERE id = %(id)s
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)

    # Validation Methods
    @staticmethod
    def validate_new_spell(data):
        isValid = True
        today = str(date.today())
        if int(data['max_charges']) <= 0:
            flash("Your ingredient needs at least one charge before you can add it to your pantry deck. Try again.","new_spell")
            isValid = False
        if data['expiration_date'] < today:
            flash("Expiration date cannot be in the past.","new_spell")
            isValid = False
        return isValid
    
    @classmethod
    def validate_hits(cls, hits, spell_id):
        one_spell = cls.get_spell_by_id(spell_id)
        if one_spell.current_charges < hits:
            flash("Cannot perform, hits exceed number of charges.","cast_spell")
        
    
    

    # Lets save this for if we need it later....
    # @staticmethod
    # def conversion_route_method(starting_unit, initial_value, ending_unit):
    #     if starting_unit == "t" or starting_unit == "tsp" or starting_unit == "teaspoon":
    #         pass
    #         # TSP conversion method
    #     elif starting_unit == 'T' or starting_unit == 'TB' or starting_unit == 'Tbsp' or starting_unit == 'Tablespoon' or starting_unit == 'tablespoon':
    #         pass
    #     elif starting_unit == 'C' or starting_unit == 'Cup' or starting_unit == 'cup' or starting_unit == 'c':
    #         pass
    #     elif starting_unit == 'Pint' or starting_unit == 'pint' or starting_unit == 'p' or starting_unit == 'pt':
    #         pass
    #     elif starting_unit == 'Quart' or starting_unit == 'quart' or starting_unit == 'qt' or starting_unit == 'Qt':
    #         pass
    #     elif starting_unit == 'Gallon' or starting_unit == 'Gal' or starting_unit == 'gal' or starting_unit == 'gallon':
    #         pass
    #     elif starting_unit == 'Ounce' or starting_unit == 'ounce' or starting_unit == 'oz':
    #         pass
    #     elif starting_unit == 'Fluid ounce' or starting_unit == 'fluid ounce' or starting_unit == 'fl oz' or starting_unit == 'fl. oz.':
    #         pass
    #     elif starting_unit = 
    
    # @staticmethod
    # def dry_ingredient_conversion_method():
        
    # @staticmethod
    # def wet_ingredient_conversion_method():
    
    