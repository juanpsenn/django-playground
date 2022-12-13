from articles.models import Article, Author

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


def get_author_by_name(name):
    try:
        return Author.objects.get(name=name)
    except Author.DoesNotExist:
        return None
