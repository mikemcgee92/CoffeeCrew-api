from django.db import models

from .category import Category
from .ingredient_amount import IngredientAmount


class Recipe(models.Model):
  """Model for recipe entities"""
  
  label = models.CharField(max_length=50, on_delete=models.DO_NOTHING)
  category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
  steps = models.TextField(max_length=500, on_delete=models.DO_NOTHING)
  notes = models.TextField(max_length=500, on_delete=models.DO_NOTHING)
  image_url = models.TextField(max_length=500, on_delete=models.DO_NOTHING)
  creator_id = models.CharField(max_length=50, on_delete=models.DO_NOTHING)
  created_date = models.DateTimeField(on_delete=models.DO_NOTHING)
  
  @property
  def ingredient_amounts(self):
    """All ingredients with amounts by size"""
    ingredient_amounts = IngredientAmount.objects.filter(recipe=self)
    return list(ingredient_amounts.values('size', 'ingredient', 'amount'))
