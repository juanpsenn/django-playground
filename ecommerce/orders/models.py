from django.db import models

# Create your models here.
class Order(models.Model):
    client = models.BigIntegerField()
    total_amount = models.DecimalField(decimal_places=2, max_digits=15)


class OrderDetail(models.Model):
    article = models.ForeignKey("articles.Article", on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=15)
    order = models.ForeignKey(
        Order, on_delete=models.DO_NOTHING, related_name="details"
    )


# Article -> Detalle -> Venta
