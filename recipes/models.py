from django.db import models

#TODO: I want to add in some functionality. Ideally, I want to be able to choose an item from an alphabetized
# dropdown menu and have the ingredients used to make the item displayed. If the ingredients are not organic or
# inorganic material, then I want to be able to link to the recipes for the items to see what they need to be
# crafted. It would be nice to code in the functionality to make some kind of 'cart.' You say all of the things you
# want to build, and the website snaps you to a page where you can see the ingredients, what planets you can find
# them on, how much total power/storage you'll need to create them, etc. Continue with the idea from here,
# implement bit by bit. CHANGE THE BRANCH!!!
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    crafted_from = models.ForeignKey('Recipe', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='recipes', null=True, blank=True, on_delete=models.SET_NULL)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} units of {self.ingredient} in {self.recipe}"
