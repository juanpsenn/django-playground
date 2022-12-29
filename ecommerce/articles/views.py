from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from articles.models import Article
from articles.services import update_article, create_article
from articles.selectors import get_article, list_articles
from articles.serializers import ArticleSerializer

# Create your views here.


class CreateArticleApi(APIView):
    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
        description = serializers.CharField()
        price = serializers.DecimalField(decimal_places=2, max_digits=15)
        author = serializers.CharField()

    def post(self, request):
        _serializer = self.InputSerializer(data=request.data)
        _serializer.is_valid(raise_exception=True)

        article = create_article(**_serializer.validated_data)

        return Response(
            f"Article: {article.title}, $ {article.price} created successfully!",
            status=201,
        )


class UpdateArticleApi(APIView):
    def put(self, request, article_id):
        title = request.data.get("title")
        description = request.data.get("description")
        price = request.data.get("price")

        article = update_article(article_id, title, description, price)

        return Response(f"Article: {title}, $ {price} updated successfully!", status=201)


class UpdatePriceArticleApi(APIView):
    def put(self, request, article_id):
        price = request.data.get("price")

        try:
            article = update_article(article_id, price=price)
            return Response(
                f"Article: {article.title}, $ {price} updated successfully!",
                status=201,
            )
        except Exception as err:
            return Response({"error": str(err)}, status=200)


class ListArticlesApi(APIView):
    def get(self, request):
        query_text = request.query_params.get("query_text")
        price_a = request.query_params.get("price_a")
        price_b = request.query_params.get("price_b")
        is_active = request.query_params.get("is_active", True)  # 1 or 0

        articles = list_articles(query_text, price_a, price_b, is_active)

        return Response(
            {"articles": ArticleSerializer(articles, many=True).data},
            status=200,
        )


class GetArticleApi(APIView):
    def get(self, request, article_id):
        article = get_article(article_id)

        return Response({"article": ArticleSerializer(article).data}, status=200)
