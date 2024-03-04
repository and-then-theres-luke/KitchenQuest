from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, ingredient, recipe, spell



@app.route('/spells/view/<int:id>')
def view_spell_frontend(id):
    if 'user_id' not in session:
        return redirect('/login')
    one_spell = spell.Spell.get_spell_by_id(id)
    return render_template('one_spell.html', one_spell = one_spell)

@app.route('/spells/edit/<int:id>')
def edit_spell_frontend(id):
    if 'user_id' not in session:
        return redirect('/login')
    one_spell = spell.Spell.get_spell_by_id(id)
    return render_template('edit_spell.html', one_spell = one_spell)
    
@app.route('/spells/delete/<int:id>')
def delete_spell_frontend(id):
    if 'user_id' not in session:
        return redirect('/login')
    spell.Spell.delete_spell_by_id(id)
    return redirect('/dashboard')

@app.post('/spells/edit/process')
def process_spell_edit_frontend():
    if 'user_id' not in session:
        return redirect('/login')
    print(request.form)
    # spell.Spell.update_spell(request.form)
    # redirect_string = f"""/spells/view/{request.form['id']}"""
    # return redirect(redirect_string)
    return redirect('/dashboard')