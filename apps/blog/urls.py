from django.urls import path
from apps.blog import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<slug:slug>/', views.article_category, name='category'),
    path('<slug:cat_slug>/<slug:slug>/', views.article_detail, name='article_detail'),
]