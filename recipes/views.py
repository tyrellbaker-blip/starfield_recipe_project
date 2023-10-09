from django.shortcuts import render


# Create your views here.
def get_all_ingredients(recipe):
    all_ingredients = []
    direct_ingredients = recipe.ingredients.all()
    for ingredient in direct_ingredients:
        all_ingredients.append(ingredient)
        if ingredient.crafted_from:
            all_ingredients.extend(get_all_ingredients(ingredient.crafted_from))
    return all_ingredients
