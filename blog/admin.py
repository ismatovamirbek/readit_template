from django.contrib import admin
from .models import Blog, Article, Author, Blog_info,Comment, Tags, Categories



admin.site.register(Blog)
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Blog_info)
admin.site.register(Tags)
admin.site.register(Categories)