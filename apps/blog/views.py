from django.shortcuts import render
from apps.blog.models import Post, Category
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
import datetime
from django.http import Http404
from django.db.models import Count
from django.db.models.query_utils import Q


class ArticleCategory(ListView):
    
    context_object_name = 'post'
    model = Post
    template_name = "blog/list.html"
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        category = Category.objects.get(slug=slug)
        category = category.category

        if self.request.user.is_staff or self.request.user.is_superuser:

            category = get_object_or_404(Category, slug = slug)
            posts = Post.objects.filter(category = category)

        else:

            category = get_object_or_404(Category, slug = slug, draft=False)
            posts = Post.objects.filter(category = category, draft = False)

        count = Post.objects.filter(category = category, draft = False).count()

        context = {
            'category_name':category,
            'post' : posts,
            'count' : count,
        }
        return context

def article_detail(request, cat_slug=None, slug=None):

    post = get_object_or_404(Post, category__slug = cat_slug, slug = slug)
    print(post.category.draft)
    if (
            post.draft or post.created_date > datetime.datetime.now().date() or post.category.draft == True
        ) and (
            not request.user.is_staff or not request.user.is_superuser
        ):

        raise Http404

    category = Category.objects.all()

    count = Category.objects.filter(draft=False).annotate(
        post_count=Count('post', filter=Q(post__draft=False))
    )


    blog = Post.objects.filter(draft=False).order_by('-created_date')
    category = zip(category,count)
    context = {
        'post':post, 
        'category': category, 
        'blog': blog,
    }

    return render(request, "blog/detail.html", context)
