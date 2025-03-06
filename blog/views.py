from django.shortcuts import render, redirect
from .models import Blog, Article, Author, Blog_info
from .forms import CommentForm

def index(request):
   blog = Blog.objects.all()
   context = {
       "blog": blog
   }
   return render(request, "index.html", context)


def detail(request, pk):
    blog = Blog.objects.get(id=pk)
    blog_info = Blog_info.objects.all()
    author = Author.objects.all()

    comment = CommentForm(request.POST or None)
    if comment.is_valid():
        com = comment.save(commit=False)
        com.blog = blog
        com.save()
        return redirect(".")

    context = {
        "blog": blog,
        "blog_info": blog_info,
        "author": author,
        "comment": comment
    }

    return render(request, "blog-single.html", context)


def article(request):
    article = Article.objects.all()

    context = {
        "article": article,
    }

    return render(request, "blog.html", context)



