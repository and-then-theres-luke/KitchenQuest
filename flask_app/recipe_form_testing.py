new_inputs = ([('ingredient_index_1_api_ingredient_id', '10120129'), ('ingredient_index_1_name', 'bread flour'), ('ingredient_index_1_amount', '100.0'), ('ingredient_index_1_unit', 'grams'), ('ingredient_index_1_charge_unit', 'grams'), ('ingredient_index_1_charge_amount', '1'), ('ingredient_index_2_api_ingredient_id', '10120129'), ('ingredient_index_2_name', 'bread flour'), ('ingredient_index_2_amount', '400.0'), 
('ingredient_index_2_unit', 'grams'), ('ingredient_index_2_charge_unit', 'grams'), ('ingredient_index_2_charge_amount', '1'), ('ingredient_index_3_api_ingredient_id', '1001'), ('ingredient_index_3_name', 'butter'), ('ingredient_index_3_amount', '100.0'), ('ingredient_index_3_unit', 'grams'), ('ingredient_index_3_charge_unit', 'grams'), ('ingredient_index_3_charge_amount', '14.79'), ('ingredient_index_4_api_ingredient_id', '18374'), ('ingredient_index_4_name', 'fresh yeast'), ('ingredient_index_4_amount', '1.0'), ('ingredient_index_4_unit', 'gram'), ('ingredient_index_4_charge_unit', 'gram'), ('ingredient_index_4_charge_amount', '1'), ('ingredient_index_5_api_ingredient_id', '18374'), ('ingredient_index_5_name', 'fresh yeast'), ('ingredient_index_5_amount', '20.0'), ('ingredient_index_5_unit', 'grams'), ('ingredient_index_5_charge_unit', 'grams'), ('ingredient_index_5_charge_amount', '1'), ('ingredient_index_6_api_ingredient_id', '14311'), ('ingredient_index_6_name', 'malted milk powder'), ('ingredient_index_6_amount', '50.0'), ('ingredient_index_6_unit', 'grams'), ('ingredient_index_6_charge_unit', 'grams'), ('ingredient_index_6_charge_amount', '1'), ('ingredient_index_7_api_ingredient_id', '2047'), ('ingredient_index_7_name', 'table salt'), ('ingredient_index_7_amount', '15.0'), ('ingredient_index_7_unit', 'grams'), ('ingredient_index_7_charge_unit', 'grams'), ('ingredient_index_7_charge_amount', '1'), ('ingredient_index_8_api_ingredient_id', '4584'), 
('ingredient_index_8_name', 'sunflower oil'), ('ingredient_index_8_amount', '6.0'), ('ingredient_index_8_unit', 'servings'), ('ingredient_index_8_charge_unit', 'servings'), ('ingredient_index_8_charge_amount', '1'), ('ingredient_index_9_api_ingredient_id', '14412'), ('ingredient_index_9_name', 'water'), ('ingredient_index_9_amount', '100.0'), ('ingredient_index_9_unit', 'milliliters'), ('ingredient_index_9_charge_unit', 'milliliters'), ('ingredient_index_9_charge_amount', '1'), ('ingredient_index_10_api_ingredient_id', '14412'), ('ingredient_index_10_name', 'water'), ('ingredient_index_10_amount', '200.0'), ('ingredient_index_10_unit', 'milliliters'), ('ingredient_index_10_charge_unit', 'milliliters'), ('ingredient_index_10_charge_amount', '1')])

def function(inputs):
    # create boss here, get the value back
    data_to_send = {
        'boss_id' : 1,
    }
    index = 0
    while (index < len(inputs)-1):
        print("Index is " + str(index))
        data_to_send['api_ingredient_id'] = inputs[index][1]
        data_to_send['name'] = inputs[index+1][1]
        data_to_send['amount'] = inputs[index+2][1]
        data_to_send['unit'] = inputs[index+3][1]
        data_to_send['charge_unit'] = inputs[index+4][1]
        data_to_send['charge_amount'] = inputs[index+5][1]
        data_to_send['charges_needed'] = float(inputs[index+2][1]) / float(inputs[index+5][1])
        print("#############")
        print(data_to_send)
        print("#############")
        index += 6
        

function(new_inputs)
"""
for item in thing:
    i need to do this thing, and i'm going to do it kinda like this
    
    
    i don't know what to do here, ask J
    i know i need a for loo
    
    
    ('ingredient_index_2_api_ingredient_id', '10120129'), 
        ('ingredient_index_2_name', 'bread flour'), ('ingredient_index_2_amount', '400.0'), 
('ingredient_index_2_unit', 'grams'), ('ingredient_index_2_charge_unit', 'grams'), ('ingredient_index_2_charge_amount', '1'), ('ingredient_index_3_api_ingredient_id', '1001'), ('ingredient_index_3_name', 'butter'), ('ingredient_index_3_amount', '100.0'), ('ingredient_index_3_unit', 'grams'), ('ingredient_index_3_charge_unit', 'grams'), ('ingredient_index_3_charge_amount', '14.79'), ('ingredient_index_4_api_ingredient_id', '18374'), ('ingredient_index_4_name', 'fresh yeast'), ('ingredient_index_4_amount', '1.0'), ('ingredient_index_4_unit', 'gram'), ('ingredient_index_4_charge_unit', 'gram'), ('ingredient_index_4_charge_amount', '1'), ('ingredient_index_5_api_ingredient_id', '18374'), ('ingredient_index_5_name', 'fresh yeast'), ('ingredient_index_5_amount', '20.0'), ('ingredient_index_5_unit', 'grams'), ('ingredient_index_5_charge_unit', 'grams'), ('ingredient_index_5_charge_amount', '1'), ('ingredient_index_6_api_ingredient_id', '14311'), ('ingredient_index_6_name', 'malted milk powder'), ('ingredient_index_6_amount', '50.0'), ('ingredient_index_6_unit', 'grams'), ('ingredient_index_6_charge_unit', 'grams'), ('ingredient_index_6_charge_amount', '1'), ('ingredient_index_7_api_ingredient_id', '2047'), ('ingredient_index_7_name', 'table salt'), ('ingredient_index_7_amount', '15.0'), ('ingredient_index_7_unit', 'grams'), ('ingredient_index_7_charge_unit', 'grams'), ('ingredient_index_7_charge_amount', '1'), ('ingredient_index_8_api_ingredient_id', '4584'), 
('ingredient_index_8_name', 'sunflower oil'), ('ingredient_index_8_amount', '6.0'), ('ingredient_index_8_unit', 'servings'), ('ingredient_index_8_charge_unit', 'servings'), ('ingredient_index_8_charge_amount', '1'), ('ingredient_index_9_api_ingredient_id', '14412'), ('ingredient_index_9_name', 'water'), ('ingredient_index_9_amount', '100.0'), ('ingredient_index_9_unit', 'milliliters'), ('ingredient_index_9_charge_unit', 'milliliters'), ('ingredient_index_9_charge_amount', '1'), ('ingredient_index_10_api_ingredient_id', '14412'), ('ingredient_index_10_name', 'water'), ('ingredient_index_10_amount', '200.0'), ('ingredient_index_10_unit', 'milliliters'), ('ingredient_index_10_charge_unit', 'milliliters'), ('ingredient_index_10_charge_amount', '1')]) 
    
"""
    
    
    
    
    
    
    
    
    
    
            # query - """
            # INSERT INTO required_spells 
            # (
            #     boss_id,
            #     api_ingredient_id,
            #     charge_value,
            #     charge_unit,
            #     charges_needed
            # )
            # VALUES 
            # (
            #     %(boss_id)s
            #     %(api_ingredient_id)s
            #     %(charge_value)s
            #     %(charge_unit)s
            #     %(charges_needed)s
            # )
            # """

