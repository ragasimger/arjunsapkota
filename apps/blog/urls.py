from django.urls import path
from apps.blog import views

urlpatterns = [
    path('<slug:slug>/', views.ArticleCategory.as_view(), name='category'),
    path('<slug:cat_slug>/<slug:slug>/', views.article_detail, name='article_detail'),
]