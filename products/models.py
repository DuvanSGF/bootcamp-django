from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=25)
    description = models.TextField()
    price       = models.CharField(max_length=50)
