from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Article, Author, Blog_info, Comment
from .forms import CommentForm
from django.core.paginator import Paginator

def index(request):
    blog_list = Blog.objects.all().order_by('-create_at')  # Order blogs by latest
    paginator = Paginator(blog_list, 5)  # Show 5 posts per page

    page_number = request.GET.get('page')  # Get the page number from URL
    page_obj = paginator.get_page(page_number)  # Get the correct page

    context = {
        "page_obj": page_obj,  # Pass paginated blog list
    }
    return render(request, "index.html", context)

def detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)  # Fetch blog or return 404
    blog_info = blog.blog_infos.all()  # Use related_name to get related blog info
    author = Author.objects.all()  # Only related author
    comments = blog.comments.all()  # Fetch related comments

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            com = comment_form.save(commit=False)
            com.blog = blog  # Associate comment with blog
            com.save()
            return redirect("detail", pk=pk)  # Redirect to the same detail page to clear form
    else:
        comment_form = CommentForm()  # Empty form on GET request

    context = {
        "blog": blog,
        "blog_info": blog_info,
        "author": author,
        "comment_form": comment_form,
        "comments": comments
    }

    return render(request, "blog-single.html", context)


def article(request):
    article_list = Article.objects.all().order_by('-create_at')  # Order articles by latest
    paginator = Paginator(article_list, 5)  # Show 5 articles per page

    page_number = request.GET.get('page')  # Get the page number from URL
    page_obj = paginator.get_page(page_number)  # Get the correct page

    context = {
        "page_obj": page_obj,  # Pass paginated articles
    }

    return render(request, "blog.html", context)
