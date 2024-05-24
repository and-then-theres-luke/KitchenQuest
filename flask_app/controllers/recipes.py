from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import recipe, spell, ingredient
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
async def show_one_recipe_frontend(id):
    if 'user_id' not in session:
        return redirect("/login")
    one_recipe = recipe.Recipe.get_recipe_by_api_recipe_id(id)
    spellbook = spell.Spell.get_spellbook_by_user_id(session['user_id'])
    recipe.Recipe.create_recipe_table(one_recipe, spellbook)
    return render_template("hold.html")