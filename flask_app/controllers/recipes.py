from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, ingredient, recipe, spell
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
    one_recipe = recipe.Recipe.recipe_boss_conversion_handler_test(id)
    
    # This recieves the following data:
    # one_recipe:
    
    return render_template("test.html", one_recipe = one_recipe)