from django.db import models


class Ingredient(models.Model):
  """Model for ingredient entities"""
  
  label = models.CharField(max_length=50)
