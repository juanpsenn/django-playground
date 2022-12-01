from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=15)