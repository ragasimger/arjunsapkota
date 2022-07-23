from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.urls import reverse
import datetime

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(created_date__lte=datetime.datetime.now())


class Category(models.Model):
    category = models.CharField(max_length=50, default='', unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    draft = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("category", kwargs={'slug' : self.slug})

class Post(models.Model):
    title = models.CharField(max_length=160, default='', null=False)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    content = models.TextField(default="")
    description = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    draft = models.BooleanField(default=False)
    created_date = models.DateField(null=True, auto_now_add=True)
    updated = models.DateField(blank=True, null=True)
    featured_image = models.ImageField(upload_to="img/featured_image", default="")
    objects = PostManager()
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={
                        "cat_slug": self.category.slug, 
                        "slug": self.slug
            }
        )