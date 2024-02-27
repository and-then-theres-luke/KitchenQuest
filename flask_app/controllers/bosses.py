from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, ingredient, recipe, spell
import requests

# Create Boss Route

@app.post ("/bosses/create")
def create_boss_frontend():
    if 'user_id' not in session:
        return redirect("/login")
    print(request.form)
    return render_template("test2.html")