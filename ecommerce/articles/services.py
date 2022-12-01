from articles.models import Article
from articles.selectors import get_article

def update_article(id, title = None, description = None, price = None):
    article = get_article(id)

    if not article:
        return Response(status=404)
    
    if price < 0:
        return Response({"error": "Price should be ge 0."}, status=400)

    if title is not None:
        article.title = title
    if description is not None:
        article.description = description
    
    article.price = price

    article.save()

    return article