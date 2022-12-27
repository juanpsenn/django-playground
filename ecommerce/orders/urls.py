from django.urls import path
from orders.views import OrderGetApi

urlpatterns = [
    path("get/<int:order_id>", OrderGetApi.as_view()),
]
