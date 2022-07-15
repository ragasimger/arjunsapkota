from django.urls import path
from apps.main import views

urlpatterns = [
    path("news/", views.index, name = "index"),
    
    path("<slug:slug>/", views.about, name = "index"),
]