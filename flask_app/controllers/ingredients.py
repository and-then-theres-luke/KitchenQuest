from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, ingredient
import requests

# Ingredient Search

@app.route('/ingredient/show_one/<string:ingredient_id>')
def show_one_ingredient(ingredient_id):
    one_ingredient = ingredient.Ingredient.get_ingredient_by_id_test(ingredient_id)
    return render_template("one_ingredient.html", one_ingredient = one_ingredient)

@app.route("/ingredient/search")
def ingredient_search_frontend():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("ingredient_search.html")