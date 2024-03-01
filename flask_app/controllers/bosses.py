from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, ingredient, recipe, spell, boss
import requests

# Create Boss Route

@app.post ("/bosses/create")
def create_boss_frontend():
    if 'user_id' not in session:
        return redirect("/login")
    boss.Boss.create_boss_with_required_spells(request.form)
    return redirect("/dashboard")