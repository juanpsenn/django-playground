from articles.models import Article, Author
from django.db.models import Q, Avg
from articles.filters import title_or_description_contains, author_name_contains


def get_article(id):
    try:
        return Article.objects.get(id=id)
    except Article.DoesNotExist:
        return None


def list_articles(query_text, price_a, price_b, is_active=True):
    return Article.objects.filter(
        (
            title_or_description_contains(query_text)
            | author_name_contains(query_text)
        )
        & Q(is_active=is_active)
        & (
            Q(price__gte=price_a) & Q(price__lte=price_b)
        )  # price__lt / price__gt / __lte / __gte
    )
    # or and


def get_author_by_name(name):
    try:
        # SELECT * FROM Authors WHERE name = "...."
        return Author.objects.get(name=name)
    except Author.DoesNotExist:
        return None


def average_price(articles):
    # In : average_price([1, 7, 4, 5])
    # Out: {'price__avg': Decimal('2049.5')}

    # In : average_price([1, 7, 4, 5]).get("price__avg")
    # Out: Decimal('2049.5')

    # In : average_price([1, 7, 4, 5])["price__avg"]
    # Out: Decimal('2049.5')
    return Article.objects.filter(id__in=articles).aggregate(Min("price"))
