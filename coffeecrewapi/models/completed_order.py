from django.db import models

class CompletedOrder(models.Model):
    """Model for completed order entries from Square API"""
    
    order_id = models.CharField(max_length=50, )