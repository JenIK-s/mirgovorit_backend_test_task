from django.contrib import admin
from .models import Product, Recipe, ProductInRecipe


class ProductInRecipeInline(admin.TabularInline):
    model = ProductInRecipe
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    inlines = (ProductInRecipeInline,)
