from __future__ import unicode_literals



# Create your models here.

from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=38)
    description = models.CharField(max_length= 200)
    weight = models.IntegerField()
    price = models.IntegerField()
    cost = models.IntegerField()
    category = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
