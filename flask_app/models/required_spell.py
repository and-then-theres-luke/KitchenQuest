from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session




class Required_Spell:
    db = "kitchenquest"
    def __init__(self, data):
        self.id = data['id']
        self.boss_id = data['boss_id']
        self.api_ingredient_id = data['api_ingredient_id']
        self.name = data['name']
        self.amount = data['amount']
        self.unit = data['unit']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.charge_value = None
        self.charge_amount = None
        self.charges_needed = None
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
            unit
        )
        VALUES (
            %(boss_id)s, 
            %(api_ingredient_id)s, 
            %(name)s, 
            %(amount)s, 
            %(unit)s
        )
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
        
    # Read
    @classmethod
    def get_required_spell(cls, required_spell_id):
        
        data = {
            'id' : required_spell_id
        }
        query = """
        SELECT *
        FROM required_spells
        WHERE id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    # Update
    # Delete
    
    @classmethod
    def delete_required_spell(cls, id):
        data = {
            'id' : id
        }
        query = """
        DELETE FROM required_spells
        WHERE id = %(id)s
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return