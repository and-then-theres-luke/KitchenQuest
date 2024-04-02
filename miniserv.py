from flask_app.test.models import ingredient, required_spell, spell, boss
from datetime import date, timedelta
from flask_app.api_key import API_KEY
import asyncio
    
if __name__ == "__main__":
    async def testing_stuff():
        # spellbook = []
        # list_of_required_spells = [required_spell.Required_Spell(api_ingredient_id=1, name="Spell 1", amount=10, unit="grams"), required_spell.Required_Spell(api_ingredient_id=2, name="Spell 2", amount=20, unit="grams")]
        spellbook = []
        data = [
            {
                "id" : "1",
                "boss_id" : "1",
                "api_ingredient_id" : "1",
                "name" : "Spell 1",
                "amount" : "10",
                "unit" : "grams"
            },
            {
                "id" : "2",
                "boss_id" : "1",
                "api_ingredient_id" : "2",
                "name" : "Spell 2",
                "amount" : "20",
                "unit" : "cups"
            }
            
        ]
        list_of_required_spells = []
        for item in data:
            list_of_required_spells.append(required_spell.Required_Spell(item))
        result = await boss.Boss.check_for_required_spells(spellbook, list_of_required_spells)
        print(len(result))
        print(result[0].isSpell)
        print(result[1].isSpell)
        
    asyncio.run(testing_stuff())