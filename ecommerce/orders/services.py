from articles.models import Article, Author
from orders.models import Order, OrderDetail


def create_order():
    articles = (Article.objects.last(), Article.objects.first())

    order = Order.objects.create(client=1, total_amount=100.50)
    details = []

    for article in articles:
        details.append(
            OrderDetail(
                article=article, quantity=1, price=article.price, order=order
            )
        )

    OrderDetail.objects.bulk_create(details)

    return order
