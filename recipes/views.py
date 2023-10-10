from django.shortcuts import render

from recipes.forms import RecipeForm
from recipes.models import Recipe, RecipeIngredient


def select_recipe(request):
    ingredients_list = []
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            selected_recipe = form.cleaned_data['recipe']
            recipe_instance = Recipe.objects.get(id=selected_recipe.id)
            ingredients = RecipeIngredient.objects.filter(recipe=recipe_instance)
            for ingredient in ingredients:
                ingredients_list.append((ingredient.ingredient.name, ingredient.quantity))
    else:
        form = RecipeForm()

    return render(request, 'select_recipe.html', {
        'form': form,
        'ingredients_list': ingredients_list
    })