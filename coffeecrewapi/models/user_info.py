from django.db import models


class UserInfo(models.Model):
  """Model used to store user data"""
  
  firebase_key = models.CharField(max_length=50, unique=True)
  display_name = models.CharField(max_length=50,)
  is_manager = models.BooleanField()
