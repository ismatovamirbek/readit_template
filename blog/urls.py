from django.urls import path
from .views import index, blog,article

urlpatterns = [
    path("", index),
    path('blog/', blog),
    path('article/', article)
]