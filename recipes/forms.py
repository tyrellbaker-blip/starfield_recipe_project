from django import forms
from .models import Category, Recipe


class RecipeForm(forms.Form):
    class RecipeForm(forms.Form):
        category = forms.ModelChoiceField(queryset=Category.objects.all())
        recipe = forms.ModelChoiceField(queryset=Recipe.objects.all())  # Populate with all recipes for now