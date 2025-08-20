from django.db import models

from .ingredient import Ingredient


class IngredientAmount(models.Model):
  """Model for amount per ingredient by recipe size

    Joins Recipe and Ingredient entities
  """
  
  recipe = models.ForeignKey("Recipe", on_delete=models.DO_NOTHING)
  size = models.CharField(max_length=50)
  ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
  amount = models.CharField(max_length=50)
