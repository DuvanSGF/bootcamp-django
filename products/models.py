from django.db import models

# Create your models here.
class Product(models.Model):
    id_products = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=25)
    description = models.TextField()
    price       = models.CharField(max_length=50)
    summary     = models.TextField(default='This is cool!')

#Prueba de ssh
