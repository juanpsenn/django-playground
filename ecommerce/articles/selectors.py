from articles.models import Article

def get_article(id):
    try:
        return Article.objects.get(id=id)
    except Article.DoesNotExist:
        return None


def get_articles_values(id):
    return Article.objects.filter(id=id).values(
        "title",
        "description",
        "price",
    )
