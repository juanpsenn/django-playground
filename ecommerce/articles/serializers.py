from rest_framework.serializers import ModelSerializer
from articles.models import Article, Author

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["__all__"]


class ArticleSerializer(ModelSerializer):
    author = AuthorSerializer(many=False)
    # SerializerMethodField()

    class Meta:
        model = Article
        # exclude = ["id", "is_active"] 
        fields = ["title", "description", "price", "is_active", "author"]