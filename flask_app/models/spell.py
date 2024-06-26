
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
        self.current_charges = data['current_charges']
        self.charge_amount = data['charge_amount']
        self.charge_unit = data['charge_unit']
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
                    charge_amount,
                    charge_unit,
                    expiration_date,
                    isFrozen
                ) 
            VALUES 
                (
                    %(user_id)s,
                    %(api_ingredient_id)s,
                    %(name)s,
                    %(current_charges)s,
                    %(charge_amount)s,
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
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
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
    def get_spellbook_apis_by_user_id(cls, user_id):
        data = {
            'user_id' : user_id
        }
        query = """
        SELECT api_ingredient_id
        FROM spells
        WHERE user_id = %(user_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        pure_list = []
        for item in results:
            pure_list.append(item['api_ingredient_id'])
        return pure_list
    
    # Update Spell Models
    @classmethod
    def update_spell(cls, data):
        if not cls.validate_new_spell(data):
            return False
        query = """
        UPDATE spells 
        SET 
            name = %(name)s,
            current_charges = %(current_charges)s, 
            charge_amount = %(charge_amount)s, 
            expiration_date = %(expiration_date)s
        WHERE id = %(id)s
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    
    
    @classmethod
    def update_charges(cls, spell_id, current_charges):
        data = {
            'id' : spell_id,
            'current_charges' : current_charges
        }
        query = """
        UPDATE spells
        SET current_charges = %(current_charges)s
        WHERE id = %(id)s
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    @classmethod
    def reduce_charges(cls, spell_id, current_charges, charges_needed):
        if float(current_charges) - float(charges_needed) < 0:
            return False
        data = {
            'id' : spell_id,
            'current_charges' : float(current_charges) - float(charges_needed)
        }
        query = """
        UPDATE spells
        SET current_charges = %(current_charges)s
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
        if int(data['current_charges']) <= 0:
            flash("Your ingredient needs at least one charge before you can add it to your pantry deck. Try again.","new_spell")
            isValid = False
        if data['expiration_date'] < today:
            flash("Expiration date cannot be in the past.","new_spell")
            isValid = False
        return isValid