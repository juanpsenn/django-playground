from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from articles.models import Article

# Create your views here.


class CreateArticleApi(APIView):
    def post(self, request):
        title = request.data.get("title")
        description = request.data.get("description")
        price = request.data.get("price")

        article = Article.objects.create(
            title=title,
            description=description,
            price=price
        )

        return Response(f"Article: {title}, $ {price} created successfully!", status=201)


class UpdateArticleApi(APIView):
    def put(self, request, article_id):
        title = request.data.get("title")
        description = request.data.get("description")
        price = request.data.get("price")

        article = Article.objects.get(id=article_id)
        article.title=title
        article.description=description
        article.price=price

        article.save()

        return Response(f"Article: {title}, $ {price} updated successfully!", status=201)


class ListArticlesApi(APIView):
    def get(self, request):
        articles = Article.objects.all().values(
            "id",
            "title", 
            "description", 
            "price", 
        )
        
        return Response({"articles": articles}, status=200)


class GetArticleApi(APIView):
    def get(self, request, article_id):
        article = Article.objects.filter(id=article_id).values(
            "title", 
            "description", 
            "price",
        )

        return Response({"article": article[0]}, status=200)