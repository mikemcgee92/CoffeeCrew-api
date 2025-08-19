from django.db import models


class Category(models.Model):
  """Model for recipe category entities"""
  label = models.CharField(max_length=50, on_delete=models.DO_NOTHING)
