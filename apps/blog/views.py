from apps.blog.models import Post, Category
from django.shortcuts import get_object_or_404, render
import datetime
from django.http import Http404
from django.db.models import Count
from django.db.models.query_utils import Q
from django.core.paginator import Paginator

def article_category(request, slug=None):
    category = Category.objects.get(slug=slug)
    category = category.category

    if request.user.is_staff or request.user.is_superuser:
        category = get_object_or_404(Category, slug = slug)
        posts = Post.objects.filter(category = category)

    else:
        category = get_object_or_404(Category, slug = slug, draft=False)
        posts = Post.objects.filter(category = category, draft = False)

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'category': category
    }
    return render(request, "blog/list.html", context)


def article_detail(request, cat_slug=None, slug=None):

    post = get_object_or_404(Post, category__slug = cat_slug, slug = slug)
    if (
            post.draft or post.created_date > datetime.datetime.now().date() or post.category.draft == True
        ) and (
            not request.user.is_staff or not request.user.is_superuser
        ):

        raise Http404

    category = Category.objects.all()[:10]

    count = Category.objects.filter(draft=False).annotate(
        post_count=Count('post', filter=Q(post__draft=False))
    )
    blog = Post.objects.filter(draft=False).order_by('created_date').exclude(id=post.id)[:4]
    category = zip(category,count)
    context = {
        'post':post, 
        'category': category,
        'blog': blog,
    }
    return render(request, "blog/detail.html", context)