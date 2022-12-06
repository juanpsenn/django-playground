from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from articles.models import Article
from articles.services import update_article
from articles.selectors import get_article
from articles.serializers import ArticleSerializer

# Create your views here.


class CreateArticleApi(APIView):
    def post(self, request):
        title = request.data.get("title")
        description = request.data.get("description")
        price = request.data.get("price")

        article = Article.objects.create(
            title=title,
            description=description,
            price=price,
        )

        return Response(f"Article: {title}, $ {price} created successfully!", status=201)


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
            return Response(f"Article: {article.title}, $ {price} updated successfully!", status=201)
        except Exception as err:
            return Response({"error": str(err)}, status=200)




class ListArticlesApi(APIView):
    def get(self, request):
        articles = Article.objects.all()
        
        return Response({"articles": ArticleSerializer(articles, many=True).data}, status=200)


class GetArticleApi(APIView):
    def get(self, request, article_id):
        article = get_article(article_id)

        return Response({"article": ArticleSerializer(article).data}, status=200)