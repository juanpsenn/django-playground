from articles.models import Article

def get_article(id):
    return Article.objects.get(id=id)


def get_articles_values(id):
    return Article.objects.filter(id=id).values(
        "title",
        "description",
        "price",
    )
