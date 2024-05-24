from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, ingredient
import asyncio
import requests

# Create Users Controller
@app.post("/register")
def register_frontend():
    if not user.User.create_user(request.form):
        return render_template("login.html")
    return redirect("/dashboard")
    


# Read Users Controller

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect("/login")
    return redirect('/dashboard')

@app.route("/login")
def login_frontend():
    if 'user_id' not in session:
        return render_template("login.html")
    return redirect('/dashboard')

@app.route("/login/process", methods=['POST'])
def login_process():
    one_user = user.User.login(request.form)
    if not one_user:
        return redirect('/login')
    return redirect('/dashboard')

@app.route("/dashboard")
async def dashboard_frontend():
    if 'user_id' not in session:
        return redirect('/login')
    one_user = await user.User.get_user_by_id(session['user_id'])
    return render_template("dashboard.html", one_user = one_user, spellbook = one_user.spellbook)

@app.route('/logout')
def logout_frontend():
    session.clear()
    return redirect('/')

@app.route('/test')
def test_route():
    return render_template("test.html")
    