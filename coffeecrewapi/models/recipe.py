from django.db import models

from .category import Category
from .ingredient_amount import IngredientAmount


class Recipe(models.Model):
  """Model for recipe entities"""
  
  label = models.CharField(max_length=50, )
  category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  steps = models.TextField(max_length=500, )
  notes = models.TextField(max_length=500, )
  image_url = models.TextField(max_length=500, )
  creator_id = models.CharField(max_length=50, )
  created_date = models.DateTimeField()
  
  @property
  def ingredient_amounts(self):
    """All ingredients with amounts by size"""
    ingredient_amounts = IngredientAmount.objects.filter(recipe=self)
    return ingredient_amounts
