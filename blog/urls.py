from django.urls import path
from .views import index, article, detail

urlpatterns = [
    path('', index, name="index"),
    path("blog/detail/<int:pk>/", detail, name="blog_detail"),
    path('article/', article, name="article"),
]
