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

@app.route('/async_test')
async def async_test():
    loop = asyncio.get_event_loop()
    for i in range(10):
        print(i)
        await asyncio.sleep(1)
    return render_template("test.html")

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
def dashboard_frontend():
    if 'user_id' not in session:
        return redirect('/login')
    one_user = user.User.get_user_by_id(session['user_id'])
    return render_template("dashboard.html", one_user = one_user, spellbook = one_user.spellbook)

@app.route('/logout')
def logout_frontend():
    session.clear()
    return redirect('/')

@app.route('/test')
def test_route():
    return render_template("test.html")
    