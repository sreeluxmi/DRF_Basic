from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField(blank=True)
    description = models.CharField(max_length=700,null=True,blank=True)

    def __str__(self):
        return self.name
