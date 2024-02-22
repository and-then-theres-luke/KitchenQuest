from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, ingredient, recipe
import requests

# Create Recipe Controller

@app.route('/recipes/create')
def recipe_create_frontend():
    if 'user_id' not in session:
        return redirect("/login")
    return render_template("create_recipe.html")


# Read Recipe Controller

@app.route('/recipes/search')
def recipe_search_frontend():
    if 'user_id' not in session:
        return redirect("/login")
    return render_template("recipe_search.html")

@app.route('/recipes/show_one/<int:id>')
def show_one_recipe_frontend(id):
    if 'user_id' not in session:
        return redirect("/login")
    one_recipe = recipe.Recipe.get_recipe_by_id(id)
    return render_template("one_recipe.html", one_recipe = one_recipe)
    



    

# Update Recipe Controller



# Delete Recipe Controller


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')                                   The variable must be in the path within angle brackets
# def index(id):                                            It must also be passed into the function as an argument/parameter
#     user_info = user.User.get_user_by_id(id)              The it will be able to be used within the function for that route
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.

# Render template is a function that takes in a template name in the form of a string, then any number of named arguments containing data to pass to that template where it will be integrated via the use of jinja
# Redirect redirects from one route to another, this should always be done following a form submission. Don't render on a form submission.