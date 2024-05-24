from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import boss, required_spell, spell
import requests, asyncio

# Create Boss Route

@app.post ("/bosses/create")
def create_boss_frontend():
    if 'user_id' not in session:
        return redirect("/login")
    print(request.form)
    boss.Boss.create_boss_with_required_spells(request.form)
    return redirect("/dashboard")

@app.route("/bosses/view/<int:boss_id>")
def render_one_boss_frontend(boss_id):
    if 'user_id' not in session:
        return redirect("/login")
    one_boss = asyncio.run(boss.Boss.detect_boss(boss_id))
    return render_template("one_boss.html", one_boss = one_boss)

@app.route('/bosses/defeat/<int:boss_id>')
def defeat_boss_frontend(boss_id):
    if 'user_id' not in session:
        return redirect("/login")
    boss.Boss.defeat_boss(boss_id)
    return redirect("/dashboard")

@app.route('/bosses/delete/<int:boss_id>')
def delete_boss_frontend(boss_id):
    if 'user_id' not in session:
        return redirect("/login")
    boss.Boss.delete_boss(boss_id)
    return redirect('/dashboard')