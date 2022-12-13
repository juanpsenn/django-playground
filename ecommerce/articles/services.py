from articles.models import Article, Author
from articles.selectors import get_article, get_author_by_name

def create_author(name):
    return Author.objects.create(name=name)


def update_article(id, title=None, description=None, price=None):
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


def create_article(*, title, description, price, author):
    # create_article("HP", "Un Libro", 100.50) X
    # create_article(title="HP", description="Un Libro", price=100.50) ✓
    _author = get_author_by_name(author)
    if _author is None:
        _author = create_author(author)
    
    article = Article.objects.create(
        title=title,
        description=description,
        price=price,
        author=_author
    )
    return article
