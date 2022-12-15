from django.db.models import Q


def title_or_description_contains(query_text):
    return Q(title__icontains=query_text) | Q(description__icontains=query_text)


def author_name_contains(query_text):
    return Q(author__name__icontains=query_text)
