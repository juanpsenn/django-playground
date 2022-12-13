from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey("Author", on_delete=models.DO_NOTHING, null=True)

class Author(models.Model):
    name= models.CharField(max_length=128)