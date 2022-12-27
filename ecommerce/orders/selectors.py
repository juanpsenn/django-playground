from articles.models import Article, Author
from django.db.models import Q
from articles.filters import title_or_description_contains, author_name_contains

# orders = OrderDetail.objects.filter(article_id__in=[1, 7]).values_list("order", flat=True)
# orders = Order.objects.filter(id__in=orders)

# details = OrderDetail.objects.filter(article_id__in=[1, 7])
# orders = []
# for detail in details:
#     if not detail.order in orders:
#         orders.append(detail.order)
