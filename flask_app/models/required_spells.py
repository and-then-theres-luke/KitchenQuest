from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session




class Required_Spells:
    db = "kitchenquest"
    def __init__(self, data):
        [
            id, 
            boss_id, 
            api_ingredient_id, 
            name, 
            amount, 
            unit, 
            charge_amount, 
            charge_unit, 
            charges_needed, 
            created_at, 
            updated_at ] = data
        self.id = id, 
        self.boss_id = boss_id, 
        self.api_ingredient_id = api_ingredient_id, 
        self.name = name, 
        self.amount = amount, 
        self.unit = unit, 
        self.charge_amount = charge_amount, 
        self.charge_unit = charge_unit, 
        self.charges_needed = charges_needed, 
        self.created_at = created_at, 
        self.updated_at = updated_at
        
        
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