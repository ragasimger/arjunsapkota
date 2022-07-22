from django.urls import path
from apps.main import views

urlpatterns = [
    path("news/", views.news, name = "index"),
    
    path("<slug:slug>/", views.page_detail, name = "index"),
]