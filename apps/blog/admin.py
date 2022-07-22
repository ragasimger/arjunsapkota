from django.contrib import admin
from apps.blog.models import Category, Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)