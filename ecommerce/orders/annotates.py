def current_price(details):
    details.annotate(current_price=F("article__price"))
