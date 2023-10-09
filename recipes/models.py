from django.db import models


class Ingredient(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField()
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} units of {self.ingredient} in {self.recipe}"
