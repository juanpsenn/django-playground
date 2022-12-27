from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from .serializers import OrderSerializer
from .models import Order, OrderDetail


class OrderGetApi(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        return Response({"data": serializer.data})
