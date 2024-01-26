from django.shortcuts import render
from .models import ProductInRecipe
from django.http import HttpResponse


def add_product_to_recipe(_, recipe_id, product_id, weight):
    recipe, created = ProductInRecipe.objects.get_or_create(
        recipe_id=recipe_id,
        product_id=product_id,
        defaults={'weight_in_grams': weight}
    )
    if not created:
        recipe.weight_in_grams = weight
        recipe.save()
    return HttpResponse(status=200)


def cook_recipe(_, recipe_id):
    recipes = ProductInRecipe.objects.filter(
        recipe_id=recipe_id
    )
    for recipe in recipes:
        recipe.product.count_used += 1
        recipe.product.save()
    return HttpResponse(status=200)


def show_recipes_without_product(request, product_id):
    recipes = ProductInRecipe.objects.exclude(
        product_id=product_id, weight_in_grams__gte=10
    )
    return render(request, 'index.html', context={'recipes': recipes})
