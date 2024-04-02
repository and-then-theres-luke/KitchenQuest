import unittest
from unittest.mock import patch, AsyncMock
from flask_app.models import boss, ingredient  # Import the class containing your method
import asyncio

class Test_Spell_Checker(unittest.TestCase):

    # Test Case 1: Required spell found with sufficient charges
    @patch('asyncio.create_task')
    @patch('ingredient.Ingredient.convert_amounts')
    def test_spell_found_sufficient_charges(self, mock_convert):
        mock_convert.return_value = AsyncMock()
        spellbook = [{'api_ingredient_id': 1, 'charge_amount': 5, 'charge_unit': 'g', 'current_charges':10}]
        required_spells = [{'api_ingredient_id': 1, 'amount': 2, 'unit': 'g'}]
        result = asyncio.run(boss.Boss.check_for_required_spells(spellbook, required_spells))
        self.assertTrue(result[0].isSpell)
        self.assertTrue(result[0].isEnoughCharges)
        
    # Test Case 2: Required spell not found
    def test_spell_not_found(self):
        spellbook = [{'api_ingredient_id': 1, 'charge_amount': 5, 'charge_unit': 'g'}]
        required_spells = [{'api_ingredient_id': 2, 'amount': 2, 'unit': 'g'}]
        result = asyncio.run(boss.Boss.check_for_required_spells(spellbook, required_spells))
        self.assertFalse(result[0].isSpell)

    # Test Case 3: Required spell found with insufficient charges
    def test_spell_found_insufficient_charges(self):
        spellbook = [{'api_ingredient_id': 1, 'charge_amount': 1, 'charge_unit': 'g', 'current_charges':1}]
        required_spells = [{'api_ingredient_id': 1, 'amount': 2, 'unit': 'g'}]
        result = asyncio.run(boss.Boss.check_for_required_spells(spellbook, required_spells))
        self.assertTrue(result[0].isSpell)
        self.assertFalse(result[0].isEnoughCharges)

    # Test Case 4: Check if conversion is called when units don't match
    @patch('ingredient.Ingredient.convert_amounts')
    def test_conversion_called(self, mock_convert):
        spellbook = [{'api_ingredient_id': 1, 'charge_amount': 10, 'charge_unit': 'mL'}]
        required_spells = [{'api_ingredient_id': 1, 'amount': 1, 'unit': 'tsp'}]
        asyncio.run(boss.Boss.check_for_required_spells(spellbook, required_spells))
        mock_convert.assert_called_once()

# **Replace `your_module` with the actual name of your module and `boss.Boss` with the name of the class where `check_for_required_spells` lives**

if __name__ == "__main__":
    unittest.main()