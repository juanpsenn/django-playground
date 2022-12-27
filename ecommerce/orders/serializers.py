from rest_framework import serializers
from articles.models import Article, Author
from orders.models import Order, OrderDetail
from django.db.models import Sum


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ["article_id", "quantity", "price", "order"]


class OrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True, read_only=True)

    total = serializers.SerializerMethodField()

    def get_total(self, order):
        # OrderDetail.object. -> order.details.
        return order.details.aggregate(Sum("price"))["price__sum"]

    class Meta:
        model = Order
        fields = ["client", "details", "total", ""]
