from django.db import models

from .ingredient import Ingredient


class IngredientAmount(models.Model):
  """Model for amount per ingredient by recipe size

    Joins Recipe and Ingredient entities
  """
  
  recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
  size = models.CharField(max_length=50)
  ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  amount = models.CharField(max_length=50)
  
  class Meta:
    unique_together = 'recipe', 'size', 'ingredient', 'amount'
