from django.urls import path
from hello.views import HelloWorldAPI


urlpatterns = [
    path("", HelloWorldAPI.as_view()),
]
