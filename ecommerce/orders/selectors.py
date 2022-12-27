from orders.models import OrderDetail
from django.db.models import Q, F

# orders = OrderDetail.objects.filter(article_id__in=[1, 7]).values_list("order", flat=True)
# orders = Order.objects.filter(id__in=orders)

# details = OrderDetail.objects.filter(article_id__in=[1, 7])
# orders = []
# for detail in details:
#     if not detail.order in orders:
#         orders.append(detail.order)

def get_order_details(order):
    return OrderDetail.objects.filter(order_id=order).annotate(
        current_price=F("article__price")
    )