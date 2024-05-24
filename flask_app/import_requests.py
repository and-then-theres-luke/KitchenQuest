import requests
import pandas as pd

def get_recipe_by_api_recipe_id(api_recipe_id):
    api_key = 'e5435bd9712a45208d0da9ad28db16b2'
    res = requests.get(
        'https://api.spoonacular.com/recipes/' +
        str(api_recipe_id) +
        '/information?includeNutrition=false&apiKey=' + 
        api_key)
    one_recipe = res.json()
    data = {
        'id' : one_recipe['id'], 
        'title' : one_recipe['title'], 
        'image' : one_recipe['image'], 
        'imageType' : one_recipe['imageType'], 
        'servings' : one_recipe['servings'], 
        'readyInMinutes' : one_recipe['readyInMinutes'], 
        'extendedIngredients' : one_recipe['extendedIngredients'],
        'summary' : one_recipe['summary']
    }
    return data

def recipe_to_dataframe(recipe):
    # This function assumes that extendedIngredients is a list of dictionaries
    ingredients = recipe['extendedIngredients']
    ingredient_df = pd.DataFrame(ingredients)
    
    # The rest of the recipe data can be put in a separate dataframe
    recipe_df = pd.DataFrame([recipe])
    
    return ingredient_df, recipe_df

# Example usage:
recipe_id = 123456  # replace with your recipe id
recipe_data = get_recipe_by_api_recipe_id(recipe_id)
ingredient_df, recipe_df = recipe_to_dataframe(recipe_data)

print(ingredient_df)
print(recipe_df)