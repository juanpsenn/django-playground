from orders.models import OrderDetail
from django.db.models import Q, F, Sum

# orders = OrderDetail.objects.filter(article_id__in=[1, 7]).values_list("order", flat=True)
# orders = Order.objects.filter(id__in=orders)

# details = OrderDetail.objects.filter(article_id__in=[1, 7])
# orders = []
# for detail in details:
#     if not detail.order in orders:
#         orders.append(detail.order)


def get_order_details(order):
    details = OrderDetail.objects.filter(order_id=order)
    return current_price(details)


def list_articles_sold():
    return (
        OrderDetail.objects.values("article__title", "price")
        .annotate(sold=Sum("quantity"))
        .values_list("article__title", "sold", "price")
    )
    
