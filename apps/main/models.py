from django.db import models
import datetime

# Create your models here.

class News(models.Model):

    news_title = models.CharField(max_length=250, verbose_name="News Title")
    description = models.CharField(max_length=400, verbose_name="Description")
    link = models.CharField(max_length=400, verbose_name="Link")
    image = models.ImageField(blank=True, null=True, verbose_name="Image")

    def __str__(self):
        return self.news_title

class Page(models.Model):

    title = models.CharField(max_length=70, default='', verbose_name="News Title")
    content = models.TextField(default="", verbose_name="News Title")
    featured_image = models.ImageField(upload_to="img/featured_image", default="")
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title