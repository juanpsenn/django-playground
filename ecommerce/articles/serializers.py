from rest_framework.serializers import ModelSerializer
from articles.models import Article

class ArticleSerializer(ModelSerializer):

    # SerializerMethodField()

    class Meta:
        model = Article
        # exclude = ["id", "is_active"] 
        fields = ["title", "description", "price", "is_active"]