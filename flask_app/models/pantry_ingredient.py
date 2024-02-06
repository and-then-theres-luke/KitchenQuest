
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ingredient, user
from datetime import date, timedelta
from flask import flash, session
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Pantry_Ingredient:
    db = "kitchenquest" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']                        # ID for an ingredient in the pantry
        self.user_id = data['user_id']              # ID for the user whose pantry that ingredient is in
        self.ingredient_id = data['ingredient_id']  # ID for the actual ingredient data
        self.current_hp = data['current_hp']
        self.max_hp = data['max_hp']
        self.expiration_date = data['created_on'] + timedelta(data['expires']) # created_at(day) minus expiration I know it's pseudo code, shut up.
        self.ingredient_model = None                # When we create the pantry_ingredient we will as part of the creation process be attaching a model of the "ideal" ingredient to the one in the pantry. This is where we will get our unit type, max hp, etc. 
        self.expires = None
        # What changes need to be made above for this project?
        #What needs to be added here for class association?
        # When a new pantry ingredient is created, we construct it using the same information from ingredients        


    # Create Pantry Ingredients Model 
    @classmethod
    def add_ingredient_to_pantry_by_id(cls, data):                 # Returns TRUE or FALSE
        query = """
            INSERT INTO pantry_ingredients 
                (
                    user_id, 
                    ingredient_id,
                    current_hp,
                    max_hp,
                    expiration_date
                ) 
            VALUES 
                (
                    %(user_id)s,
                    %(ingredient_id)s,
                    %(current_hp)s,
                    %(max_hp)s,
                    %(expiration_date)s
                )
            ;
            """
        model_ingredient = ingredient.Ingredient.get_ingredient_by_id(data['ingredient_id'])
        new_data = {
            'user_id' : data['user_id'],
            'ingredient_id' : data['ingredient_id'],
            'current_hp' : model_ingredient.max_hp,
            'max_hp' : model_ingredient.max_hp,
            'expiration_date' : date.today() + timedelta(model_ingredient.days_to_expire)
        }
        if not connectToMySQL(cls.db).query_db(query, new_data):
            return False
        return True
    
    @classmethod
    def add_ingredient_to_pantry_by_name(cls, data):                 # Returns TRUE or FALSE
        query = """
            INSERT INTO pantry_ingredients 
                (
                    user_id, 
                    ingredient_id,
                    current_hp,
                    max_hp,
                    expiration_date
                ) 
            VALUES 
                (
                    %(user_id)s,
                    %(ingredient_id)s,
                    %(current_hp)s,
                    %(max_hp)s,
                    %(expiration_date)s
                )
            ;
            """
        model_ingredient = ingredient.Ingredient.get_ingredient_by_id(data['ingredient_id'])
        new_data = {
            'user_id' : data['user_id'],
            'ingredient_id' : data['ingredient_id'],
            'current_hp' : model_ingredient.max_hp,
            'max_hp' : model_ingredient.max_hp,
            'expiration_date' : date.today() + timedelta(model_ingredient.days_to_expire)
        }
        if not connectToMySQL(cls.db).query_db(query, new_data):
            return False
        return True
    




    # Read Users Models
    
    @classmethod
    def get_pantry_ingredient_by_id(cls,pantry_ingredient_id):
        data = {
            'id' : pantry_ingredient_id
        }
        query = """
        SELECT *
        FROM pantry_ingredients
        WHERE id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        one_pantry_ingredient = cls(results[0])
        return one_pantry_ingredient
    
    @classmethod
    def get_pantry_deck_by_user_id(cls, user_id):
        data = {
            'user_id' : user_id
        }
        query = """
        SELECT *
        FROM pantry_ingredients
        WHERE pantry_ingredients.user_id = %(user_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_pantry_deck = []
        for row in results:
            one_pantry_deck.append(cls(row))
        return one_pantry_deck


    # Update Users Models
    @classmethod
    def reduce_hit_points(cls,hit_points,pantry_ingredient_id):
        current_hp = (cls.get_pantry_ingredient_by_id(pantry_ingredient_id)).current_hp - hit_points
        data = {
            'id' : pantry_ingredient_id,
            'current_hp' : current_hp
        }
        query = """
        UPDATE pantry_ingredients
        SET current_hp = %(current_hp)s
        WHERE id = %(id)s
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    @classmethod
    def update_pantry_ingredient_by_id(cls, pantry_ingredient_id):
        data = {
            'pantry_ingredient_id' : pantry_ingredient_id
        }
        query = """
        SELECT *
        FROM pantry_ingredients
        WHERE id = %(pantry_ingredient_id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_pantry_ingredient = cls(results[0])
        return one_pantry_ingredient


    # Delete Users Models
    @classmethod
    def delete_user(cls, data):     # Returns nothing
        query = """
            DELETE FROM users
            WHERE id = %(id)s;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    # Validation Methods
    @staticmethod
    def validate_new_user(new_user):
        is_valid = True
        if User.get_user_by_email(new_user['email']):
            flash("Email is already registered to another user.", "register")
            is_valid = False
        if len(new_user['first_name']) < 3:
            flash("First name must be three (3) characters or more.", "register")
            is_valid = False
        if len(new_user['last_name']) < 3:
            flash("Last name must be three (3) characters or more.", "register")
            is_valid = False
        if len(new_user['password']) < 8:
            flash("Password must be 8 characters or more.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(new_user['email']): 
            flash("Invalid email address! Use less weird characters. Weirdo. So weird!", "register")
            is_valid = False
        if new_user['password'] != new_user['confirm_password']:
            flash("The passwords don't match! Try again.", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def login(data):
        one_user = None
        if not data['email']:
            flash("Please input a valid email.", 'login')
            return False
        if not data['password']:
            flash("Please input a valid password.", 'login')
            return False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", 'login')
            return False
        one_user = User.get_user_by_email(data['email']) # Changed my login validation a little so it returns either a class object or False
        if one_user:
            if not bcrypt.check_password_hash(one_user.password, data['password']):
                flash("Invalid email/password", "login")
                return False
        elif not one_user:
            flash("Invalid email/password", "login")
            return False
        session['user_id'] = one_user.id
        session['name'] = f"""{one_user.first_name} {one_user.last_name}"""
        return one_user
    
    @staticmethod
    def check_is_logged_in():
        is_valid = True
        if 'user_id' not in session:
            flash("Please login to access this page.", "access")
            is_valid = False
        return is_valid