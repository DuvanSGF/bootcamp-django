from django.db import models

# Create your models here.
class Product(models.Model):
    id_products = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField()


#Prueba final
