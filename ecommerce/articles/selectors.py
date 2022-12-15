from articles.models import Article, Author
from django.db.models import Q

def get_article(id):
    try:
        return Article.objects.get(id=id)
    except Article.DoesNotExist:
        return None


def list_articles(query_text, price_a, price_b, is_active=True):
    return Article.objects.filter()


def get_author_by_name(name):
    try:
        return Author.objects.get(name=name) # SELECT * FROM Authors WHERE name = "...."
    except Author.DoesNotExist:
        return None
