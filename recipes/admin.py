from django.contrib import admin
from.models import Recipe, Ingredient, RecipeIngredient, Category


class SubCategoryInline(admin.TabularInline):
    model = Category
    fk_name = 'parent_category'
    extra = 1
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    list_filter = ('parent_category',)
    inlines = [SubCategoryInline]
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(Category)

# Register your models here.
