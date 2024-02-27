from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, ingredient, spell
import requests

# Show One Ingredient
@app.route('/ingredients/show_one/<string:ingredient_id>')
def show_one_ingredient(ingredient_id):
    one_ingredient = ingredient.Ingredient.get_ingredient_by_api_ingredient_id(ingredient_id)
    return render_template("one_ingredient.html", one_ingredient = one_ingredient)

# Ingredient Search
@app.route("/ingredients/search")
def ingredient_search_frontend():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("ingredient_search.html")

@app.route("/ingredients/make_spell/", methods=["POST"])
def make_spell_frontend():
    print(request.form)
    data = {}
    for item in request.form:
        data[item] = request.form[item]
    if 'isFrozen' not in data:
        data['isFrozen'] = 0
    if not spell.Spell.create_spell(data):
        print("Whoops, redirect")
        return redirect("/ingredients/show_one/" + request.form['api_ingredient_id'])
    print("good job!")
    return redirect("/dashboard")

