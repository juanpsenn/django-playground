from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.http import HttpResponse


from .serializers import OrderSerializer
from .models import Order, OrderDetail
from .utils import export_excel_report
from .selectors import list_articles_sold


class OrderGetApi(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        return Response({"data": serializer.data})


class ExportXLSX(APIView):
    def get(self, request):
        header = ["Articulo", "Cantidad vendida", "Precio venta"]
        sold_articles = list(list_articles_sold())
        total_amount = 0
        for article in sold_articles:
            total_amount += article[2]*article[1]
        sold_articles.append(["TOTAL: ", " ", str(total_amount)])
        excel = export_excel_report("Ventas", header, sold_articles)
        # Return the file as an HttpResponse
        response = HttpResponse(
            excel,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            status=201
        )
        response["Content-Disposition"] = "attachment; filename=Reporte Ventas.xlsx"
        return response
