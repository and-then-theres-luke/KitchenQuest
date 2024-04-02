from flask_app import app
from flask_app.controllers import users, ingredients, recipes, bosses, spells, required_spells
import unittest


if __name__=="__main__":   
    app.run(debug=True)
    # app.run(debug=True, port=5500) 
    # Above is how you can change the port number.

# Debug needs to be set to False when deployed. This will avoid giving out sensitive information that could be used to hack your site.
