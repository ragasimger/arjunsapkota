import imp
from django.shortcuts import render
from apps.main.models import News, Page


def news(request):
    news = News.objects.all()

    context = {
        'news' : news
    }

    return render(request, "main/news_detail.html", context)

def page_detail(request, slug=None):
    
    page = Page.objects.get(slug=slug)

    context = {
        'page' : page
    }

    return render(request, "main/page_detail.html", context)

