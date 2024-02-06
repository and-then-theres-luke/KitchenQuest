from flask_app.config.mysqlconnection import connectToMySQL

class Comment:
    db = "kitchenquest"
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.recipe_id = data['recipe_id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    
    # Create Method
    @classmethod
    def create_comment(cls,data):
        query = """
        INSERT INTO comments
        (
            user_id,
            recipe_id,
            comment
        )
        VALUES
        (
            %(user_id)s,
            %(recipe_id)s,
            %(comment)s
        )
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    # Read Method
    @classmethod
    def get_comment_by_id(cls, comment_id):
        data = {
            'id' : comment_id
        }
        query = """
        SELECT *
        FROM comments
        WHERE id = %(id)s
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return
    
    @classmethod
    def get_all_comments_by_recipe(cls, recipe_id):
        data = {
            'id' : recipe_id
        }
        query = """
        SELECT *
        FROM recipes
        LEFT JOIN comments
        ON recipes.id = comments.user_id
        WHERE recipes.id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return