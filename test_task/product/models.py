from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    count_used = models.IntegerField(default=0, verbose_name='Количество использований в рецепте')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    products = models.ManyToManyField(
        Product,
        through='ProductInRecipe',
        verbose_name='Продукты'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class ProductInRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    weight_in_grams = models.IntegerField(verbose_name='Вес в граммах')

    class Meta:
        verbose_name = 'Продукт в рецепте'
        verbose_name_plural = 'Продукты в рецептах'

    def __str__(self):
        return f'{self.recipe} {self.product}'
