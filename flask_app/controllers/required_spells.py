from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import required_spell, boss

@app.route ('/required_spells/delete/<int:required_spell_id>/<int:boss_id>')
def remove_required_spell_frontend(required_spell_id, boss_id):
    if 'user_id' not in session:
        return redirect('/login')
    one_required_spell = required_spell.Required_Spell.get_required_spell(required_spell_id)
    one_boss = boss.Boss.get_one_boss_by_id(one_required_spell.boss_id)
    if one_boss.user_id != session['user_id']:
        flash("You don't have permission to do that.")
        return redirect('/dashboard')
    required_spell.Required_Spell.delete_required_spell(one_required_spell.id)
    return redirect("/bosses/view/" + str(boss_id))