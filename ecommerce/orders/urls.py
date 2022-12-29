from django.urls import path
from orders.views import OrderGetApi, ExportXLSX

urlpatterns = [
    path("get/<int:order_id>", OrderGetApi.as_view()),
    path(
        "export/",
        ExportXLSX.as_view(),
    ),
]
