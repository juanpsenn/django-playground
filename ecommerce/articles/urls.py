from django.urls import path
from articles.views import (
    CreateArticleApi, 
    UpdateArticleApi, 
    ListArticlesApi, 
    GetArticleApi,
)


urlpatterns = [
    path('create/', CreateArticleApi.as_view()),
    path('update/<int:article_id>/', UpdateArticleApi.as_view()),
    path('list/', ListArticlesApi.as_view()),
    path('get/<int:article_id>', GetArticleApi.as_view()),
]