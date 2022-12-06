from articles.models import Article
from articles.selectors import get_article

def update_article(id, title = None, description = None, price = None):
    article = get_article(id)

    if not article:
        raise Exception(f"Article {id} not found")
    
    if price < 0:
        raise Exception("Price should be ge 0.")

    if title is not None:
        article.title = title
    if description is not None:
        article.description = description
    
    article.price = price

    article.save()

    return article