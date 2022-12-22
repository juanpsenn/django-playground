from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from articles.models import Article
from articles.services import update_article, create_article
from articles.selectors import get_article, list_articles
from articles.serializers import ArticleSerializer

# Create your views here.
