from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Blog, Article


def index(request):
    return render(request, "index.html")


def blog(request):
    blogs = Blog.objects.all()
    ctx = {
        "blogs": blogs
    }
    return render(request, 'index.html', ctx)


def article(request):
    article = Article.objects.all()
    context = {
        "article": article
    }

    return render(request, "blog.html", context)