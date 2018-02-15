from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('<int:slug>', views.article_detail, name="article_detail"),
]
