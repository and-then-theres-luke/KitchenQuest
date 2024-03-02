from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session




class Required_Spells:
    db = "kitchenquest"
    def __init__(self, data):
        self.id = data['id']
        self.boss_id = data['boss_id']
        self.api_ingredient_id = data['api_ingredient_id']
        self.name = data['name']
        self.amount = data['amount']
        self.unit = data['unit']
        self.charge_amount = data['charge_amount']
        self.charge_unit = data['charge_unit']
        self.charges_needed = data['charges_needed']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.isSpell = None
        self.isEnoughCharges = None
        
        
    # Create
    @classmethod
    def create_required_spell(cls, data):
        query = """
        INSERT INTO required_spells (
            boss_id, 
            api_ingredient_id, 
            name, 
            amount, 
            unit, 
            charge_amount, 
            charge_unit, 
            charges_needed
        )
        VALUES (
            %(boss_id)s, 
            %(api_ingredient_id)s, 
            %(name)s, 
            %(amount)s, 
            %(unit)s, 
            %(charge_amount)s, 
            %(charge_unit)s, 
            %(charges_needed)s
        )
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
        
        # Read
        # Update
        # Delete