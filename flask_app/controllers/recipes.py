from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import recipe, spell
import pandas as pd
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
    one_recipe = recipe.Recipe.get_recipe_by_api_recipe_id(id)
    spellkeys = spell.Spell.get_spellbook_apis_by_user_id(session['user_id'])
    required_spells = pd.DataFrame(one_recipe.extendedIngredients)
    required_spells['isSpell'] = False
    print(spellkeys)
    for x in range(0,len(required_spells.index)):
        if required_spells.loc[x,'id'] in spellkeys:
            required_spells.loc[x,'isSpell'] = True
        else:
            print(x, "not a spell.")
    # return render_template("hold.html")
    return render_template("one_recipe.html", one_recipe = one_recipe, required_spells = required_spells, len = len(required_spells))